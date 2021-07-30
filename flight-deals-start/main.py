# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"
flight_link = "https://www.google.co.uk/flights?hl=en#flt="


search = FlightSearch()
manager = DataManager()
notification = NotificationManager()


sheet_data = manager.city_data

for data in sheet_data:
    if data['iataCode'] == "":
        data['iataCode'] = search.search_flight(data['city'])
        search.search_flight(data['city'])

manager.city_data = sheet_data
# manager.update_city_data()
print(sheet_data)
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        # print(f"{flight.destination_city}: £{flight.price}")
        message = f"{flight.destination_city}: £{flight.price}\n"
        if flight.stop_overs > 0:
            # print(
            #     f"The Flight has {flight.stop_overs} stop "
            #     f"overs via {flight.via_city}")
            message += (f"The Flight has {flight.stop_overs} stop "
                        f"overs via {flight.via_city}\n")
        message += (f"{flight_link}{flight.origin_airport}."
                    f"{flight.destination_airport}.{flight.out_date}*"
                    f"{flight.destination_airport}.{flight.origin_airport}."
                    f"{flight.return_date}")
        if int(flight.price) < int(destination["lowestPrice"]):
            # print(destination["city"])
            print(message)
            notification.send_mails(message)
    except AttributeError:
        print("No Flights to This Region")
