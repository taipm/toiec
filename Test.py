import pymongo
from urllib.parse import quote_plus

username = quote_plus('dev')
password = quote_plus('3i9yi3sP6xLXyzsU')
cluster = '<clusterName>'
authSource = '<authSource>'
authMechanism = '<authMechanism>'

uri = f'mongodb+srv://dev:{password}@cluster0.mwaxbi8.mongodb.net/?retryWrites=true&w=majority'
#uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism

client = pymongo.MongoClient(uri)
print(client.list_database_names())
#print(client.)
db_name = 'Toiec'
# db_table = 'Word'

result = client[db_name]#["<collName>"].find()
print(result.list_collections())

# print(result)
# for i in result:
#     print(i)
