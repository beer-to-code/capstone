import pymongo
hostDB="mongodb+srv://akash404:akash@cluster0.2n7ot.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-o0czh6-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
client = pymongo.MongoClient("mongodb://localhost:27017/")
dbs=client.list_database_names()[3]
print(dbs)
col = client[dbs].list_collection_names()


def validate_local(id,passw):
    try:
        idpass=client[dbs][col[0]].find_one({"uid":str(id),"pass":str(passw)})
        if idpass:
            return 1,'offline'
            
        print(client[dbs][col[0]].find_one({"uid":str(id),"pass":str(passw)}))
        
    except:
        return 0

hostDB="mongodb+srv://akash404:akash@cluster0.2n7ot.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-o0czh6-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
client_ON = pymongo.MongoClient(hostDB)
dbs_ON=client_ON.list_database_names()[0]
col_ON = client_ON[dbs_ON].list_collection_names()
def validate_online(id,passw):
    try:
        idpass_ON=client_ON[dbs_ON][col_ON[0]].find_one({"uid":str(id),"pass":str(passw)})
        if idpass_ON:
            return 1,"online"
    except:
        return 0
