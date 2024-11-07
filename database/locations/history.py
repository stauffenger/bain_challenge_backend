import datetime
from datetime import datetime, timezone

from utils import log
from database.utils import get_collection

def get():
    collection_name = "locations_history"
    collection = get_collection(collection_name)
    history = list(collection.find({}, { "_id": False }))

    return history

def insert(source_address, destination_address, distance_km):
    collection_name = "locations_history"
    collection = get_collection(collection_name)
    current_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S%z")
    result = collection.insert_one(
        {
            "source_address": source_address,
            "destination_address": destination_address,
            "distance": distance_km,
            "timestamp": current_date
        })
    log.write(result)
    if result.acknowledged:
        return True
    else:
        return False
