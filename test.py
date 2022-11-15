from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "웹 페이지 만들기"

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)