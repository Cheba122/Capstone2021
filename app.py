from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/convert_temp/<temp>")
def convert_temp(temp):

    input_temp = float(temp)
    # conversion
    f_to_c = ((input_temp - 32) * (5.0 / 9.0))

    # print the conversion from F to C using 1 decimal place
    return "{:.1f}".format(input_temp) + " degrees F is " + "{:.1f}".format(f_to_c) + " degrees C"

