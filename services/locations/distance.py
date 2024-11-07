import datetime
from datetime import datetime, timezone

from geopy.distance import geodesic

from utils import log
from database.locations import history
from external.nominatim import get_latitude_longitude

def calculate_from_a_to_b(address_a, address_b):
    try:
        lat_a = 0
        lon_a = 0
        lat_b = 0
        lon_b = 0
        result = {}
        
        geolocation_a = get_latitude_longitude(address_a)
        geolocation_b = get_latitude_longitude(address_b)
        if len(geolocation_a) > 1:
            result['source_alternatives'] = [ item['display_name'] for item in geolocation_a ]
        if len(geolocation_b) > 1:
            result['destination_alternatives'] = [ item['display_name'] for item in geolocation_a ]
        
        if 'source_alternatives' in result or 'destination_alternatives' in result:
            return result

        if len(geolocation_a) == 0:
            result['not_found'] = [address_a]
        if len(geolocation_b) == 0:
            if 'not_found' in result:
                result['not_found'].append(address_b)
            else:
                result['not_found'] = [address_b]
        
        if 'not_found' in result:
            return result

        lat_a = geolocation_a[0]['lat']
        lon_a = geolocation_a[0]['lon']

        lat_b = geolocation_b[0]['lat']
        lon_b = geolocation_b[0]['lon']

        result['distance_km'] = geodesic((lat_a, lon_a), (lat_b, lon_b)).km
        log.write(f"Successfully got the distance between '{address_a}' and '{address_b}'. {result['distance_km']} km")

        history_updated = history.insert(address_a, address_b, result['distance_km'])
        if history_updated:
            log.write(f"Successfully added the query into the history.")
        else:
            log.write(f"It wasn't possible to add the query to the history.")

        return result
    except Exception as error:
        log.write(f"Error while trying to get the distance between '{address_a}' and '{address_b}'.")
        log.error(error)
        raise NameError(error)