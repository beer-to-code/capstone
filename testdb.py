import pymongo
hostDB="mongodb+srv://akash404:akash@cluster0.2n7ot.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-o0czh6-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
#client = pymongo.MongoClient("mongodb://localhost:27017/")
client = pymongo.MongoClient(hostDB)
#print(client.list_database_names())
#print(client.list_databases_names())
dbs=client.list_database_names()[0]
#print(dbs)
col = client[dbs].list_collection_names()
#print(col)
#print(client[dbs][col[0]].find_one())
def validate(id,passw):
    try:
        idpass=client[dbs][col[0]].find_one({"uid":str(id),"pass":str(passw)})
        #idpass=client[dbs][col[0]].find_one({"uid":str(id),"pass":str(passw)})
        #print(idpass)
        if idpass:
            return 1
            
        #print(client[dbs][col[0]].find_one({"uid":str(id),"pass":str(passw)}))
        
    except:
        return 0
print(validate("adas","12345"))
