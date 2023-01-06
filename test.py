from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydb = client["NIRF"]
coll = mydb["Ranks"]
cursor = coll.find({}, {"Institute Name": 1})
colleges = []
for col in cursor:
    colleges.append(col["Institute Name"])
print(colleges)