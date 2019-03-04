from chalice import Chalice

app = Chalice(app_name='poster-shop-inventory')


@app.route('/')
def index():
	return {'hello': 'world'}


@app.route('/search/{term}', methods=['GET'], cors=True)
def search(term):
	# return {'search': term}
	if (term == "cat"):
		return ([{"id": 1, "title": "Calico Cat", "thumb": "/public/images/cat1.jpg", "price": 19.95},
				 {"id": 2, "title": "Cat Close Up", "thumb": "/public/images/cat2.jpg", "price": 23.95},
				 {"id": 3, "title": "Grey Kitten", "thumb": "/public/images/cat3.jpg", "price": 17.95},
				 {"id": 4, "title": "Cat Outdoors", "thumb": "/public/images/cat4.jpg", "price": 17.95},
				 {"id": 5, "title": "Sneaky Cat", "thumb": "/public/images/cat5.jpg", "price": 19.95},
				 {"id": 6, "title": "Fluffy Cat", "thumb": "/public/images/cat6.jpg", "price": 23.95},
				 {"id": 7, "title": "Blue-Eyed Cat", "thumb": "/public/images/cat7.jpg", "price": 19.95},
				 {"id": 8, "title": "White Cat", "thumb": "/public/images/cat8.jpg", "price": 23.95},
				 {"id": 9, "title": "Orange Cat", "thumb": "/public/images/cat9.jpg", "price": 19.95},
				 {"id": 10, "title": "Cat Pile", "thumb": "/public/images/cat10.jpg", "price": 27.95},
				 {"id": 11, "title": "Black Cat", "thumb": "/public/images/cat11.jpg", "price": 27.95}]
		)

	if (term == "dog"):
		return ({"id": 12, "title": "Rottweiler", "thumb": "/public/images/dog1.jpg", "price": 18.95},
				{"id": 13, "title": "Grey dog", "thumb": "/public/images/dog2.jpg", "price": 23.95},
				{"id": 14, "title": "Dog on grass", "thumb": "/public/images/dog3.jpg", "price": 23.95},
				{"id": 15, "title": "Sad puppy", "thumb": "/public/images/dog4.jpg", "price": 23.95},
				{"id": 16, "title": "Boxer", "thumb": "/public/images/dog5.jpg", "price": 22.95},
				{"id": 17, "title": "Looking sideways", "thumb": "/public/images/dog6.jpg", "price": 19.95},
				{"id": 18, "title": "German shepard", "thumb": "/public/images/dog7.jpg", "price": 19.95},
				{"id": 19, "title": "Sleepy dog", "thumb": "/public/images/dog8.jpg", "price": 18.95},
				{"id": 20, "title": "Happy dog", "thumb": "/public/images/dog9.jpg", "price": 23.95}
				)

	if (term == "flower"):
		return ({"id": 21, "title": "Pink Lily", "thumb": "/public/images/flower1.jpg", "price": 23.95},
				{"id": 22, "title": "Orchid", "thumb": "/public/images/flower2.jpg", "price": 24.95},
				{"id": 23, "title": "Dandelion", "thumb": "/public/images/flower3.jpg", "price": 15.95},
				{"id": 24, "title": "Orange flower", "thumb": "/public/images/flower4.jpg", "price": 24.95},
				{"id": 25, "title": "Water lily", "thumb": "/public/images/flower5.jpg", "price": 17.95},
				{"id": 25, "title": "Red tulip", "thumb": "/public/images/flower6.jpg", "price": 18.95},
				{"id": 26, "title": "Red poppy", "thumb": "/public/images/flower7.jpg", "price": 22.95}
				)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
