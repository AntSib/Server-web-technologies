from flask import Flask

app = Flask(__name__)


@app.route('/<path:url>')
def send_date_json(url):
    login = '1149817'
    date = '-'.join([url[:2], url[2:4], "20"+url[4:6]])
    return {'date': date, 'login': login}

@app.route('/api/rv/<path:url>')
def send_reversed_path(url):
    return url[::-1]

if __name__ == '__main__':
    app.run('localhost', 8080)
