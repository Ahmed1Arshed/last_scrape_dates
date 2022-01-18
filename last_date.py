import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["utilities-scraper-competitors"]
mydb_comp = mydb["competitorproducts"]
mydb_comp_product = mydb_comp.find(
    {
    "their_name" : { "$exists": True}
    },
    {
    "competitor":1,
    "captured_at":1
    }
).sort("captured_at" , -1)

compitator = []
output_Restult = []
mydb_comp_product = list(mydb_comp_product)
for data in mydb_comp_product:
    if data.get("competitor") not in compitator:
        compitator.append(data.get("competitor"))
        output_Restult.append(data)
print(output_Restult)

# print()
# for data in mydb_comp_product:
    # print(data)