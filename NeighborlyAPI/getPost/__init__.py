import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborly-from-raj:HrqKdTYrgVEMjl2JDxGEjYWsqv5rOTR8BSViWI483g83WHFseKRIOU46CuDQFVU9QknHaEHtfudObFRUXB9xeA==@neighborly-from-raj.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-from-raj@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighborlydb']
            collection = database['posts']

            # query = {'_id': ObjectId(id)} # THIS LINE OF CODE IS NOT WORKING SO COMMENTING IT OUT
            query = {'_id': id}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)