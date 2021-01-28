from flask import Flask, request, jsonify


app = Flask(__name__)
app.config["DEBUG"] = True

ai_menu = [
    {
        "id": 1,
        "day of week": "Monday",
        "breakfast": ["tea", "oatmeal with butter"],
        "dinner": ["jelly", "cabbage soup", "mashed potatoes with a chop"],
        "lunch": ["tea", "ragout"]
    },
    {
        "id": 2,
        "day of week": "Tuesday",
        "breakfast": ["cocoa", "sandwiches"],
        "dinner": ["compote", "borscht", "braised cabbage"],
        "lunch": ["tea", "french meat"]
    },
    {
        "id": 3,
        "day of week": "Wednesday",
        "breakfast": ["orange juice", "omelet"],
        "dinner": ["jelly", "pea soup", "pasta with chicken fillet"],
        "lunch": ["tea", "mac and cheese"]
    },
    {
        "id": 4,
        "day of week": "Thursday",
        "breakfast": ["tea", "buckwheat porridge with sugar"],
        "dinner": ["jelly", "hodgepodge soup", "pilaf"],
        "lunch": ["fruit drink", "pizza"]
    },
    {
        "id": 5,
        "day of week": "Friday",
        "breakfast": ["cocoa", "cottage cheese casserole"],
        "dinner": ["compote", "meatball soup", "vitamin salad"],
        "lunch": ["tea", "potato casserole"]
    },
    {
        "id": 6,
        "day of week": "Saturday",
        "breakfast": ["tea", "porridge friendship"],
        "dinner": ["jelly", "milk soup", "buckwheat with sausages"],
        "lunch": ["cherry juice", "steamed vegetables"]
    },
    {
        "id": 7,
        "day of week": "Sunday",
        "breakfast": ["tea", "corn porridge"],
        "dinner": ["jelly", "potato soup", "meat with vegetables"],
        "lunch": ["apple juice", "burgers"]
    }
]


@app.route('/menu/all', methods=['GET'])
def api_all():
    return jsonify(ai_menu)


@app.route('/menu', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for menu in ai_menu:
        if (menu["id"] == id):
            results.append(menu)
    return jsonify(results)


@app.route('/menu', methods=['POST'])
def api_post():
    id = int(request.form['id'])
    day = request.form['day']
    breakfast = request.form['breakfast']
    lunch = request.form['lunch']
    dinner = request.form['dinner']
    for menu in ai_menu:
        if (id == menu["id"]):
            return f"Menu with id {id} already exists", 400
    menu = {
        "id": int(id),
        "day of week": day,
        "breakfast": breakfast,
        "dinner": lunch,
        "lunch": dinner
    }
    ai_menu.append(menu)
    return jsonify(ai_menu)


@app.route('/menu', methods=['PUT'])
def put():
    id = int(request.form['id'])
    day = request.form['day']
    breakfast = request.form['breakfast']
    lunch = request.form['lunch']
    dinner = request.form['dinner']
    for menu in ai_menu:
        if (id == menu["id"]):
            menu["day of week"] = day
            menu["breakfast"] = breakfast
            menu["dinner"] = lunch
            menu["lunch"] = dinner
            return jsonify(ai_menu)

    menu = {
        "id": int(id),
        "day of week": day,
        "breakfast": breakfast,
        "dinner": lunch,
        "lunch": dinner
    }
    ai_menu.append(menu)
    return jsonify(ai_menu)


@app.route('/menu', methods=['DELETE'])
def delete():
    id = int(request.form['id'])
    global ai_menu
    ai_menu = [menu for menu in ai_menu if menu["id"] != id]
    return jsonify(ai_menu)


app.run()
