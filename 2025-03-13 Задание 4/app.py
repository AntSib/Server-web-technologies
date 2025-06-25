from flask import Flask, request
from flask_cors import CORS, cross_origin
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def home():
    return "localhost server is running"

@app.route('/result4/', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
@cross_origin(origins='*', headers=['x-test', 'ngrok-skip-browser-warning', 'Content-Type', 'Accept', 'Access-Control-Allow-Headers'])
def result4():
    head_data = request.headers.get('x-test')
    body_data = (request.get_data()).decode('utf-8')
    # print(f"headers: {request.headers}", end='\n\n')
    # print(f'head_data: {head_data}, body_data: {body_data}')
    return {'message': '1149817',
            'x-result': head_data if head_data else 'None',
            'x-body': body_data if body_data else 'None'
    }


if __name__ == '__main__':
    app.run('localhost')
