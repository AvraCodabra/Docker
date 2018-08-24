from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/avra", methods=['GET','POST'])
def avra():
    if request.method == 'GET':
        return jsonify({'message': 'Im alive!'})
    else:
        return jsonify({'message': 'Error! Wrong request'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)