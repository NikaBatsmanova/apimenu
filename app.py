from flask import Flask, request, jsonify
from flask_restful import reqparse

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
    if results == []:
        return f"Menu with id {id} does not exist", 400
    return jsonify(results)


@app.route('/menu', methods=['POST'])
def api_post():
    parser = reqparse.RequestParser()
    parser.add_argument("day")
    parser.add_argument("breakfast")
    parser.add_argument("lunch")
    parser.add_argument("dinner")
    params = parser.parse_args()
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    for menu in ai_menu:
        if (id == menu["id"]):
            return f"Menu with id {id} already exists", 400
    menu = {
        "id": int(id),
        "day of week": params["day"],
        "breakfast": params["breakfast"],
        "lunch": params["lunch"],
        "dinner": params["dinner"]
    }
    ai_menu.append(menu)
    return menu, 201


@app.route('/menu', methods=['PUT'])
def put():
    parser = reqparse.RequestParser()
    parser.add_argument("day")
    parser.add_argument("breakfast")
    parser.add_argument("lunch")
    parser.add_argument("dinner")
    params = parser.parse_args()
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    for menu in ai_menu:
        if (id == menu["id"]):
            menu["day of week"] = params["day"]
            menu["breakfast"] = params["breakfast"]
            menu["dinner"] = params["dinner"]
            menu["lunch"] = params["lunch"]
            return menu, 200

    menu = {
        "id": int(id),
        "day of week": params["day"],
        "breakfast": params["breakfast"],
        "lunch": params["lunch"],
        "dinner": params["dinner"]
    }
    ai_menu.append(menu)
    return menu, 201


@app.route('/menu', methods=['DELETE'])
def delete():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    global ai_menu
    ai_menu1 = [menu for menu in ai_menu if menu["id"] != id]
    if (ai_menu1 == ai_menu):
        return f"Menu with id {id} does not exist", 400
    else:
        ai_menu = ai_menu1
        return f"Menu with id {id} is deleted.", 200


app.run(host="192.168.1.105")
