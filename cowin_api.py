import requests,time
from win10toast import ToastNotifier
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=247667&date=20-05-2021"
while True:
	querystring = {}

	payload = ""
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
	print(response.text)
	if (str(response.content).split('[')[1] != "]}'"):
		toast = ToastNotifier()
		toast.show_toast("Cowin Notification",response.text,duration=5)
		print(response.text)
	else:
		time.sleep(10)