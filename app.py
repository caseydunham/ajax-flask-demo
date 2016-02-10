from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/say_name', methods=['POST'])
def say_name():
    json = request.get_json()
    first_name = json['first_name']
    last_name = json['last_name']
    return jsonify(first_name=first_name, last_name=last_name)


if __name__ == '__main__':
    app.run(debug=True)
