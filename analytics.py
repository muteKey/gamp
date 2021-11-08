import requests
import uuid
from datetime import datetime

def send_rate():
	r1 = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
	response = r1.json()

	rate = response[26]['rate']

	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	print("date and time =", dt_string)

	client_id = uuid.uuid4()
	params = {'v': '1', 't': 'event', 'tid':'UA-39503949-2', 'cid': client_id, 'dp': '', 'ec': "Finance", "ea": "Action", "ev": str(rate)}
	headers = {'User-Agent': 'PythonClient'}
	r = requests.post('https://www.google-analytics.com/collect', params=params, headers=headers)
	print(r.status_code)


send_rate()
