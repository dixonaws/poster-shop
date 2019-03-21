import boto3
import sys

str_search_endpoint = "http://search-vue-poster-shop-array-n7dslnnkd5jlulytqwvijxahde.us-east-1.cloudsearch.amazonaws.com"
client = boto3.client('cloudsearchdomain', endpoint_url=str_search_endpoint)

str_term="cat"

sys.stdout.write("Searching for term: '" + str_term + "'... ")

response = client.search(query=str_term)
print("done (" + str(response['hits']['found']) + " results).")

print(response['hits']['hit'])