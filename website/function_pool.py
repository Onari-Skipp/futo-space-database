from flask import jsonify
import random
import datetime as dt
from datetime import datetime, timedelta, date
from .DictDB import dictdb

dbORM = dictdb.DictDB()


def getContractCode() -> str:
	return "7208450356"

def getAPIKey() -> str:
	return "MK_TEST_DBQQF0A5P5"

def getSecretKey() -> str:
	return "Z16JHXZY89TXQS8QFF4YJ44HLCS0YHEG"

def get_time_of_day(current_time: str) -> str:
    # Extract the hour from the time string
    hour = int(current_time.split(":")[0])

    # Determine the time of day
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"
    
def list_to_string(list_item: list) -> str:
    if not list_item: 
        return ""
    
    if len(list_item) == 1:  
        return list_item[0]
    
    if len(list_item) == 2:  
        return f"{list_item[0]} & {list_item[1]}"
    
    # If there are three or more items
    return ", ".join(list_item[:-1]) + f" {random.choice(['&', 'and', 'with'])} " + list_item[-1]

def getDateTime():
	# Getting Date-Time Info
	current_date = dt.date.today()
	current_time = datetime.now().strftime("%H:%M:%S")

	# Date Format: "YYYY-MM-DD"
	formatted_date = current_date.strftime("%Y-%m-%d")
	date = formatted_date
	time = current_time

	return [date, time]

def returnJSONData(title, content):
	return jsonify({
		"message": {title: content}
	})
 
def loopAppendAndReverse(a, b):
	try:
		for k, v in a.items():
			b.append(v)
		return b[::-1]
	except Exception as e:
		return f"Error occured\nError: {e}"