import hashlib
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    count = 0
    if request.method == 'POST':
        password = request.form['password']
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5_char, tail = sha1_password[:5], sha1_password[5:]

        url = f'https://api.pwnedpasswords.com/range/{first5_char}'
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')

        hashes = (line.split(':') for line in res.text.splitlines())
        count = next((int(count) for h, count in hashes if h == tail), 0)

    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(debug=True)