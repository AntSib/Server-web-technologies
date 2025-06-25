from app import app
import requests


@app.route('/')
def index():
    return "Root page"


@app.route('/login')
def login():
    author = '1149817'
    return author


@app.route('/id/<id>')
def id(id):
    url = f"https://nd.kodaktor.ru/users/{id}"
    login = None

    resp = requests.get(url).json()

    try:
        login = resp['login']
        print(login)
        return login
    except Exception as e:
        print(e)
        return "Not found"
