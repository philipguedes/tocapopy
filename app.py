from flask import Flask, jsonify, Blueprint, make_response


app = Flask(__name__)

# app.config['SWAGGER'] = {
#     'title': 'PyVerde',
#     'uiversion': 2
# }

# print("oi")

# app.register_blueprint(champion_mastery)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return make_response("OK", 200)