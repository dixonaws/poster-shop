from chalice import Chalice
import boto3
import json
import os

app = Chalice(app_name='poster-shop-inventory')

dynamodb_resource = boto3.resource('dynamodb')


@app.route('/')
def index():
	return {'hello': 'world'}


@app.route('/dynamo/{term}', methods=['GET'], cors=True)
def scan_dynamo(term):
	# scan dynamo table

	str_dynamo_table = "vue-poster-shop"
	table = dynamodb_resource.Table(str_dynamo_table)

	response = table.scan()

	return (response['Items'])


@app.route('/search/{term}', methods=['GET'], cors=True)
def search(term):
	# str_search_endpoint = "http://search-vue-poster-shop-array-n7dslnnkd5jlulytqwvijxahde.us-east-1.cloudsearch.amazonaws.com"
	str_search_endpoint=os.environ['str_search_endpoint']
	cloudsearch_client = boto3.client('cloudsearchdomain', endpoint_url=str_search_endpoint)

	str_term = term

	dict_response = cloudsearch_client.search(query=str_term)

	# if we don't have any hits, then just return an empty object
	int_hits = dict_response["hits"]["found"]
	if(int_hits==0): return({})

	dict_response_hits = dict_response["hits"]["hit"]

	# create a new empty dictionary to return as our response
	lst_transformed_response = []

	# get the list of keys
	lst_keys = dict_response_hits[0]["fields"].keys()



	for i in range(int_hits-1):
		dict_item = {}

		for key in lst_keys:
			dict_item[key] = str(dict_response_hits[i]["fields"][key][0])

			# special treatment for tags since they are returned from cloudsearch as a string
			if(key=="tags"):
				str_tags = str(dict_response_hits[i]["fields"]["tags"][0])
				str_tags = str_tags.replace("[", "")
				str_tags = str_tags.replace("]", "")
				str_tags = str_tags.replace("'", "")
				lst_tags = str_tags.split(",")

				# strip off whitespace from each tag
				for k in range(len(lst_tags)):
					lst_tags[k] = lst_tags[k].strip()

				dict_item["tags"]=lst_tags
			# if key==tags
		# for key

		lst_transformed_response.append(dict_item)

	return (lst_transformed_response)

# if (term == "dog"):
# 	return ({"id": 12, "title": "Rottweiler", "thumb": "/public/images/dog1.jpg", "price": 18.95},
# 			{"id": 13, "title": "Grey dog", "thumb": "/public/images/dog2.jpg", "price": 23.95},
# 			{"id": 14, "title": "Dog on grass", "thumb": "/public/images/dog3.jpg", "price": 23.95},
# 			{"id": 15, "title": "Sad puppy", "thumb": "/public/images/dog4.jpg", "price": 23.95},
# 			{"id": 16, "title": "Boxer", "thumb": "/public/images/dog5.jpg", "price": 22.95},
# 			{"id": 17, "title": "Looking sideways", "thumb": "/public/images/dog6.jpg", "price": 19.95},
# 			{"id": 18, "title": "German shepard", "thumb": "/public/images/dog7.jpg", "price": 19.95},
# 			{"id": 19, "title": "Sleepy dog", "thumb": "/public/images/dog8.jpg", "price": 18.95},
# 			{"id": 20, "title": "Happy dog", "thumb": "/public/images/dog9.jpg", "price": 23.95}
# 			)
