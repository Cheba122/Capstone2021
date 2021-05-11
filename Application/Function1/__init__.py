import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    far = float(input("What is the temperature? "))

# conversion
f_to_c=((far-32) * (5.0/9.0))

# print the conversion from F to C using 1 decimal place
print("{:.1f}".format(far) + " degrees F is " + "{:.1f}".format(f_to_c) + " degrees C")

