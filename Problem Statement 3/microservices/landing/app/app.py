from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


''' class Add(Resource):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def get() '''


def add(n1, n2):
    print(n1, '-', type(n1))
    return int(n1)+int(n2)


def minus(n1, n2):
    return int(n1)-int(n2)


def multiply(n1, n2):
    return int(n1)*int(n2)


def divide(n1, n2):
    if n2 == "0":
        return 'Division by Zero exception'
    return int(n1)/int(n2)


@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = requests.get('http://addition:5049/add/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == 'minus':
        result = requests.get('http://minus:5048/minus/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == 'multiply':
        result = requests.get('http://multiply:5047/multiply/' +
                              str(number_1) + '&' + str(number_2)).text
    elif operation == 'divide':
        result = requests.get('http://divide:5046/divide/' +
                              str(number_1) + '&' + str(number_2)).text
    elif operation == "bitwise_or":
        result = requests.get('http://bitwise_or:5045/or/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == "maximum":
        result = requests.get('http://maximum:5044/maximum/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == "minimum":
        result = requests.get('http://minimum:5043/minimum/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == "average":
        result = requests.get('http://average:5042/average/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == "exponential":
        result = requests.get('http://exponential:5041/exponential/' +
                              str(number_1)+'&'+str(number_2)).text
    flash(
        f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
