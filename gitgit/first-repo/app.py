from datetime import datetime

# Send request to facebook.com and print response
import requests

def sendrequest(url):
    response = requests.get(url)
    print(response.status_code)

print(sendrequest('https://www.facebook.com/'))

print("Hello world")
print(f"The current time is : {datetime.now()}")