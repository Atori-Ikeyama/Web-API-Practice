from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策


@app.route('/signin', methods=['POST'])
def post_json():
    data = request.json

    if data['userid'] == "atori" and "wakamatu" == data['password']:
        suc = {"login":"success"}
        return jsonify(suc)
    else:
        fai = {"login":"failure"}
        return jsonify(fai)


@app.route('/', methods=['GET'])
def get_json_from_dictionary():
    dic = {
        'post!': 'id',
        'post!!': 'pass'
    }
    return jsonify(dic)  # JSONをレスポンス


if __name__ == '__main__':
    app.run()
