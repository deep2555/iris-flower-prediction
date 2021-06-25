import json
import requests
from werkzeug.datastructures import Headers
from werkzeug.wrappers import response

sepal_length = float(input("enter the sepal length: "))
sepal_width = float(input("enter the sepal width: "))
petal_length = float(input("enter the petal length: "))
petal_width = float(input("enter the petal width: "))


url = "http://127.0.0.1:5000/"
data = {"sepal_length": sepal_length, "sepal_width":sepal_width, "petal_length":petal_length, "petal_width": petal_width}
dataJSon = json.dumps(data)
headers = {"content-type": "application/json"}
response = requests.post(url = url, data =dataJSon , headers=headers)
print(response)
output = json.loads(response.text)

prediction = output["prediction"]
print("your flower is: ", prediction)