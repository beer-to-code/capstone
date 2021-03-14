from flask import Flask, jsonify
import pymongo

hostDB="mongodb+srv://akash404:akash@cluster0.2n7ot.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-o0czh6-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
client = pymongo.MongoClient(hostDB)

class Users:
    con = client['users']

    user_information = 'user_information'

    

    def __init__(self,):
        pass
    
    def __getitem__(self,name)->pymongo.collection.Collection:
        return self.con[name]

    def add_one(self,data):
        """
        {
            "userid":aka404,
            "password":akash404
            "user_type":"manager",
            "f_name":"Akash",
            "s_name":"",
            "l_name":"Gupta",
            "email":"akash.28.2011@gmail.com",
            "address":"Happynest Apartment"
        }
        """
        self['user_information'].insert_one(data).inserted_id

    def add_many(self, data):
        self['user_information'].insert_many(data)

    def del_one(self,query):
        self['user_information'].delete_one(query)

    def del_all(self):
        self['user_information'].delete_many({})

    def get_all(self,):
        return list(self[self.user_information].find({}))

    def get_n(self,n):
        c = self['user_information'].count_documents({})
        return list(self[self.user_information].find().skip(c-n))

    def get_if(self,query):
        return list(self[self.user_information].find(query))

    def get_collection_info(self):
        col_names = self.con.list_collection_names()
        return col_names

        """
        for col_name in col_names:
            print(col_name)
            co = self[self.col_name].count_documents({})
            print('name:',col_name, 'size:',co)
            """

        


if __name__ == '__main__':
    users = Users()
    """
    users.add_one({
        "userid":"adas",
        "password":"1234",
        "user_type":"manager",
        "f_name":"Akash",
        "s_name":"",
        "l_name":"Gupta",
        "email":"akash.28.2011@gmail.com",
        "address":"Happynest Apartment"
    })
    """
    #users.del_one({'userid':'ad'})
    #print (users.get_all())
    #print(users.get_if({'password':'1234'}))
    #print(users.get_collection_info())

