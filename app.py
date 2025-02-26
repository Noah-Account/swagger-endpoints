from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from

app = Flask(__name__)
api = Api(app)

# Configuring Swagger
app.config['SWAGGER'] = {
    'title': 'My API',
    'uiversion': 3
}
swagger = Swagger(app)

items = ['Item 1', 'Item 2', 'Item 3']

class Items(Resource):
    @swag_from('swagger/items.yml')
    def get(self):
        "This endpoint returns a list of items"
        return {'items': items}, 200

class AddItem(Resource):
    @swag_from('swagger/add_items.yml')
    def post(self, item_name):
        if not item_name:
            return {'message': 'No item provided'}, 400
        
        if item_name in items:
            return {'message': 'Item already present in Array'}, 400
        
        items.append(item_name)
        items.sort()
        return {'message': 'Item added successfully'}, 200

class RemoveItem(Resource):
    @swag_from('swagger/remove_items.yml')
    def delete(self, item_name):
        if not item_name:
            return {'message': 'No item provided'}, 400
        
        if item_name not in items:
            return {'message': 'Item not present in array'}, 400
        
        items.remove(item_name)
        return {'message': 'Item removed successfully'}, 200
    
class UpdateItems(Resource):
    @swag_from('swagger/update_items.yml')
    def put(self):
        data = request.get_json()

        old_value = data.get('old_value')
        new_value = data.get('new_value')

        if not old_value or not new_value:
            return {'message': 'Both old_value and new_value must be provided'}, 400

        if old_value not in items:
            return {'message': f'Item "{old_value}" not found in the list'}, 404
        
        index = items.index(old_value)
        items[index] = new_value
        
        return {'message': 'Item updated successfully'}, 200

api.add_resource(Items, '/items')
api.add_resource(AddItem, '/items/add/<string:item_name>')
api.add_resource(RemoveItem, '/items/remove/<string:item_name>')
api.add_resource(UpdateItems, '/items/update')

if __name__ == '__main__':
    app.run(debug=True)
