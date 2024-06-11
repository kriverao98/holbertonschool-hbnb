from flask import request, jsonify, abort #type: ignore
from Model.user import User
from Persistence.data_manager import DataManager


def route_manager(app):

    users = {}

    """User Management Enpoints"""
    @app.route('/')
    def home():
        return "Hello World"

    @app.route('/users', methods=['POST', 'GET'])
    def create_users():
        
        if request.method == 'POST':
            data = request.get_json()
            if data is None:
                abort(400, "Not a json")
            user = User(data['email'], data['password'], data['first_name'], \
                        data['last_name'], data['id'])
           
            file = DataManager()
            output = file.save(user)

            return jsonify({"message": "Successfully created new user", "user": output}), 201

        elif request.method == 'GET':
            with open("file_storage.json", 'r') as f:
                

    @app.route('/users/<user_id>', methods=['GET'])
    def user_details():
        data = request.get_json()
        return jsonify(users[data['user']])

    @app.route('/users/<user_id>', methods=['PUT'])
    def update_user():
        pass

    @app.route('/users/<user_id>', methods=['DELETE'])
    def delete_user():
        pass

