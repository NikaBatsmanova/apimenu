from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)
ai_menu = [
    {
        "id": 0,
        "day of week": "Monday",
        "breakfast": ["tea", "oatmeal with butter"],
        "dinner": ["jelly", "cabbage soup", "mashed potatoes with a chop"],
        "lunch": ["tea", "ragout"]
    },
    {
        "id": 1,
        "day of week": "Tuesday",
        "breakfast": ["cocoa", "sandwiches"],
        "dinner": ["compote", "borscht", "braised cabbage"],
        "lunch": ["tea", "french meat"]
    },
    {
        "id": 2,
        "day of week": "Wednesday",
        "breakfast": ["orange juice", "omelet"],
        "dinner": ["jelly", "pea soup", "pasta with chicken fillet"],
        "lunch": ["tea", "mac and cheese"]
    },
    {
        "id": 3,
        "day of week": "Thursday",
        "breakfast": ["tea", "buckwheat porridge with sugar"],
        "dinner": ["jelly", "hodgepodge soup", "pilaf"],
        "lunch": ["fruit drink", "pizza"]
    },
    {
        "id": 4,
        "day of week": "Friday",
        "breakfast": ["cocoa", "cottage cheese casserole"],
        "dinner": ["compote", "meatball soup", "vitamin salad"],
        "lunch": ["tea", "potato casserole"]
    },
    {
        "id": 5,
        "day of week": "Saturday",
        "breakfast": ["tea", "porridge friendship"],
        "dinner": ["jelly", "milk soup", "buckwheat with sausages"],
        "lunch": ["cherry juice", "steamed vegetables"]
    },
    {
        "id": 6,
        "day of week": "Sunday",
        "breakfast": ["tea", "corn porridge"],
        "dinner": ["jelly", "potato soup", "meat with vegetables"],
        "lunch": ["apple juice", "burgers"]
    }
]


class Menu(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(ai_menu), 200
        for menu in ai_menu:
            if (menu["id"] == id):
                return menu, 200
        return "Menu not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("day of week")
        parser.add_argument("breakfast")
        parser.add_argument("dinner")
        parser.add_argument("lunch")
        params = parser.parse_args()
        for menu in ai_menu:
            if (id == menu["id"]):
                return f"Menu with id {id} already exists", 400
        menu = {
            "id": int(id),
            "day of week": params["day of week"],
            "breakfast": params["breakfast"],
            "dinner": params["dinner"],
            "lunch": params["lunch"]
        }
        ai_menu.append(menu)
        return menu, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("day of week")
        parser.add_argument("breakfast")
        parser.add_argument("dinner")
        parser.add_argument("lunch")
        params = parser.parse_args()
        for menu in ai_menu:
            if (id == menu["id"]):
                menu["day of week"] = params["day of week"]
                menu["breakfast"] = params["breakfast"]
                menu["dinner"] = params["dinner"]
                menu["lunch"] = params["lunch"]
                return menu, 200

        menu = {
            "id": int(id),
            "day of week": params["day of week"],
            "breakfast": params["breakfast"],
            "dinner": params["dinner"],
            "lunch": params["lunch"]
        }

        ai_menu.append(menu)
        return menu, 201

    def delete(self, id):
        global ai_menu
        ai_menu = [menu for menu in ai_menu if menu["id"] != id]
        return f"Menu with id {id} is deleted.", 200


api.add_resource(Menu, "/ai-menu", "/ai-menu/", "/ai-menu/", "/ai-menu/", "/ai-menu/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
