import json
import sys
import boto3
from boto3.dynamodb.conditions import Key
from boto3 import resource
import math
from decimal import Decimal
import random

def main():
	file_directory=open("directory.json", "r")
	str_directory=file_directory.read()

	print("str_directory: " + str_directory)

	dict_directory=json.loads(str_directory)

	sys.stdout.write("Writing " + str(len(dict_directory)) + " items")

	str_dynamo_table="vue-poster-shop-array"
	dynamodb_resource=boto3.resource('dynamodb')
	table = dynamodb_resource.Table(str_dynamo_table)

	dict_row={}

	# print(json.dumps(dict_row))

	for item in dict_directory:
		print("Processing tags: " + str(item['tags']))
		id=item['id']
		print(id)
		str_price=str( item['price'])

		# decimal has a problem casting directly from a float, so we cast from string instead
		decimal_price=Decimal(str_price)
		response=table.put_item(Item={
			'id': item['id'],
			'title': item['title'],
			'thumb': 'https://new.dixonaws.com/images/' + item['thumb'],
			'price': decimal_price,
			"tags": str(item['tags'])
		})



main()