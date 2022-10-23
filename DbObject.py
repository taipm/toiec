from dataclasses import dataclass, field
from http import client

import pymongo
from urllib.parse import quote_plus


# cluster = '<clusterName>'
# authSource = '<authSource>'
# authMechanism = '<authMechanism>'


#uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism




@dataclass
class DbObject:
    username = quote_plus('dev')
    password = quote_plus('3i9yi3sP6xLXyzsU')
    uri = f'mongodb+srv://dev:{password}@cluster0.mwaxbi8.mongodb.net/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(uri)
    db = client['Toiec']
    
    def __init__(self) -> None:
        pass
    # def __init__(self) -> None:
    #     pass
    # def __init__(self, tb_name) -> None:        
    #     self.tb_name = tb_name
        
    # def save(self):
    #     self.db.Words.insert_one()