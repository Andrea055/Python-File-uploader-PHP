import requests
import os
url = 'your-site/upload.php'                 #change with your server ip
file = input("Name of the file you want upload:")
while os.path.isfile(file) == False:
     file = input("File does not exist, please rewrite the name of the file you want upload:")
files = {'file': open(file, 'rb')}
print("if response is 200 the transfer is complete without error otherwise there is an error")
r = requests.post(url, files=files)
print("response:", r.status_code)
     

