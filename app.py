from flask import Flask , request, json ,jsonify
import pandas as pd
import numpy as np
import pickle




app = Flask(__name__)
data_load = pickle.load(open("iris.sav", "rb"))


@app.route("/", methods = ["POST"])
def prediction():
    user_input = request.json
    print(user_input)
    input_list = [user_input["sepal_length"], user_input["sepal_width"], user_input["petal_length"], user_input["petal_width"]]

    prediction = data_load.predict([input_list])
    confidence = data_load.predict_proba([input_list])
    response = {}
    response["prediction"] = str(prediction[0])
    response["confidence"] = str(round(np.amax(confidence[0]) *100,2))
    return jsonify(response)




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port  = "5000")