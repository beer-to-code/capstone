import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
#print(client.list_databases_names())
dbs=client.list_database_names()[3]
print(dbs)
col = client[dbs].list_collection_names()


def validate(id,passw):
    try:
        idpass=client[dbs][col[0]].find_one({"uid":str(id),"pass":str(passw)})
        if idpass:
            return 1
            
        print(client[dbs][col[0]].find_one({"uid":str(id),"pass":str(passw)}))
        
    except:
        return 0
#print(validate("adas","1234"))
