from flask import request, jsonify, abort #type: ignore
from Model.user import User
from Model.country import Country
from Model.city import City
from Model.amenity import Amenity
from Model.place import Place
from Model.review import Review
from Persistence.DataManager import DataManager


def route_manager(app, file):

    """User Management Enpoints"""
    @app.route('/')
    def home():
        return "HBnb"

    @app.route('/users', methods=['POST', 'GET'])
    def create_users():

        if request.method == 'POST':
            data = request.get_json()
            if data is None:
                abort(400, "Not a json")
            
            # if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
            #     abort(400, "Missing data")
            user = User(data['email'], data['first_name'], data['last_name'])
            if user.unique_user(file.storage['User'], user.email) == True:
                if user.name_validation() == True:
                    file.save(user)

                    return jsonify({"message": "Successfully created new user"}), 201
                else:
                    return jsonify({"message": "failed to create user"}), 409
            else:
                return jsonify({"message": "failed to create user"}), 409
        else:
            return jsonify(file.storage["User"]), 200

    @app.route('/users/<user_id>', methods=['GET'])
    def user_details(user_id):
        return jsonify(file.storage['User'][user_id]), 200

    @app.route('/users/<user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")

        user = User(data['email'], data['first_name'], data['last_name'])
        user.id = user_id
        user.update()
        file.update(user)
        return jsonify({"message": "Successfully updated user"}), 201

    @app.route('/users/<user_id>', methods=['DELETE'])
    def delete_user(user_id):
        file.delete(str(user_id), 'User')
        return jsonify({"message": "Successfully deleted user"}), 204

    @app.route('/countries', methods=['GET'])
    def get_all_countries():
        return jsonify(file.storage['Country']), 200
    
    @app.route('/countries/<country_code>', methods=['GET'])
    def get_country(country_code):
        return jsonify(file.storage['Country'][country_code]), 200
    
    @app.route('/countries/<country_code>/cities')
    def get_cities_in_country(country_code):
        return jsonify(file.storage['Country']), 200

    @app.route('/cities', methods=['POST', 'GET'])
    def create_city():
        if request.method == 'POST':
            data = request.get_json()
            if data is None:
                abort(400, "Not a json")

            city = City(data['name'], data['country_code'])

            file.save(city)
            return jsonify({"message": "Successfully created city"}), 201
        else:
            return jsonify(file.storage['City'])
    
    @app.route('/cities/<city_id>', methods=['GET'])
    def get_city(city_id):
        return jsonify(file.storage['City'][str(city_id)]), 200

    @app.route('/cities/<city_id>', methods=['PUT'])
    def update_city(city_id):
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")

        city = City(data['name'], data['country_code'])
        city.id = city_id
        city.update()
        file.update(city)

        return jsonify({"message": "Successfully updated city"}), 201

    @app.route('/cities/<city_id>', methods=['DELETE'])
    def delete_city(city_id):
        file.delete(str(city_id), 'City')
        return jsonify({"message": "Successfully deleted city"}), 204

    @app.route('/amenities', methods=['POST', 'GET'])
    def create_amenity():
        if request.method == 'POST':
            data = request.get_json()
            if data is None:
                abort(400, "Not a json")

            amenity = Amenity(data['name'])

            file.save(amenity)
            return jsonify({"message": "Successfully created amenity"}), 201
        else:
            return jsonify(file.storage['Amenity'])

    
    @app.route('/amenities/<amenity_id>', methods=['GET'])
    def get_amenity(amenity_id):
        return jsonify(file.storage['Amenity'][amenity_id])
    
    @app.route('/amenities/<amenity_id>', methods=['PUT'])
    def update_amenity(amenity_id):
        data = request.get_json()
        if data is None:
            abort(400, "Not a JSON")

        amenity = Amenity(data['name'])
        amenity.id = amenity_id
        amenity.update()
        file.update(amenity)

        return jsonify({"message": "Successfully updated amenity"}), 201

    @app.route('/amenities/<amenity_id>', methods=['DELETE'])
    def delete_amenity(amenity_id):
        file.delete(str(amenity_id), "Amenity")
        return jsonify({"message": "Successfully deleted amenity"}), 204

    @app.route('/places', methods=['POST', 'GET'])
    def create_place():
        if request.method == 'POST':
            data = request.get_json()
            if data is None:
                abort(400, "Not a json")

            place = Place(data['host_id'], data['city_id'], data['amenity_id'],\
                        data['name'], data['description'], data['number_rooms'],\
                        data['number_bathrooms'], data['max_guest'], data['price_by_night'],\
                        data['latitude'], data['longitude'])

            file.save(place)
            return jsonify({"message": "Successfully created place"}), 201
        else:
            return jsonify(file.storage['Place'])
    
    @app.route('/places/<place_id>', methods=['GET'])
    def place(place_id):
        return jsonify(file.storage['Place'][place_id])

    @app.route('/places/<place_id>', methods=['PUT'])
    def update_place(place_id):
        data = request.get_json()
        if data is None:
            abort(400, "Not a json")

        place = Place(data['host_id'], data['city_id'], data['amenity_id'],\
                        data['name'], data['description'], data['number_rooms'],\
                        data['number_bathrooms'], data['max_guest'], data['price_by_night'],\
                        data['latitude'], data['longitude'])
        place.id = place_id
        place.update()
        file.update(place)

        return jsonify({"message": "Successfully updated place"}), 201
    
    @app.route('/places/<place_id>', methods=['DELETE'])
    def delete_place(place_id):
        file.delete(str(place_id), 'Place')
        return jsonify({"message": "Successfully deleted place"}), 204

    @app.route('/places/<place_id>/reviews', methods=['POST', 'GET'])
    def create_place_reviews(place_id):
        data = request.get_json()
        if data is None:
            abort(400, "Not a json")
        
        review = Review(data[place_id], data['user_id'], data['rating'], data['comment'])

        file.save(review)

        return jsonify({"message": "Successfully created place review"})
    

    @app.route('/users/<user_id>/reviews', methods=['GET'])
    def get_user_reviews(user_id):
        pass

    @app.route('/reviews/<review_id>', methods=['GET'])
    def get_review(review_id):
        return jsonify(file.storage['Review'][review_id])

    @app.route('/reviews/<review_id>', methods=['PUT'])
    def update_review(review_id):
        data = request.get_json()
        if data is None:
            abort(400, "Not a json")

        review = Review(data['place_id'], data['user_id'], data['rating'], data['comment'])

        review.id = review_id
        review.update()
        file.update(review)

    @app.route('/reviews/<review_id>', methods=['DELETE'])
    def delete_review(review_id):
        file.delete(str(review_id), 'Review')
        return jsonify({"message": "Successfully deleted review"}), 204