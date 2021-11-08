from flask import Flask, jsonify, request

app = Flask(__name__)



from user import user

app.register_blueprint(user, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug=True)