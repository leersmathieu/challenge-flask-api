from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
   return 'Hello World'

@app.route('/sum/<int:number1>/<int:number2>')
def user(number1, number2):
   return f"sum = {number1 + number2}!"

@app.route('/create/<user>', methods=['POST'])
def test(user):
   return f"POST {user}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"

# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }

if __name__ == '__main__':
   app.run("127.0.0.1", port=5000, debug=True)