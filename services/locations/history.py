import datetime
from datetime import datetime, timezone

from utils import log
from database.locations import history

def get():
    try:
        locations_history = history.get()
        log.write("Successfully got the locations history.")

        return locations_history
    except Exception as error:
        log.write(f"Error while trying to get the locations history.")
        log.error(error)
        raise NameError(error)

def insert():
    try:
        result = collection.insert_one(
            {
                "latitude_source": 111,
                "longitude_source": 111,
                "latitude_destination": 111,
                "longitude_destination": 111,
                "distance": 11,
                "timestamp ": current_date
            })
        log.write(result)
        if result:
            log.write(f"Successfully inserted the locations into the database.")
            return True
        else:
            return False
    except Exception as e:
        log.write(f"Error while trying to insert the locations into the database.")
        log.error(error)
        raise NameError(error)