from flask import Flask
from flask import request
import random
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World !"


@app.route('/status')
def status():
    return {'server_status': "Alive!"}


@app.route('/sum/<int:number1>/<int:number2>')
def user(number1, number2):
    return f"sum = {number1 + number2}!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        content = request.get_json()
        return f"Login success for user {content['user']} with password from length: {len(content['password'])}!"
    else:
        return {"method": "GET"}


@app.route('/predict/<int:seller_avaible>/<string:month>/<int:customer_visiting_website>')
def predict(seller_avaible, month, customer_visiting_website):
    return f"Prediction for {month} : {random.randint(2000, 5000)}"


if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
