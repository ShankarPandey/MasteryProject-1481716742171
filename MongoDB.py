# -----Code begins ----------
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('mongodb://admin:LTNXICNOWCHKTICH@bluemix-sandbox-dal-9-portal.4.dblayer.com:20691,bluemix-sandbox-dal-9-portal.0.dblayer.com:20691/admin?ssl=true')
print client

db = client.Prototypes
print db

ReadData = db.Data_train_bpk
ReadData_bpk = ReadData.find()
for doc in ReadData_bpk:
    print doc

# --------Code ends ------------