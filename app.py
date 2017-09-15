#!/usr/bin/env python3
from flask import Flask, session, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Something very secret and hard to guess!'


@app.route("/")
def index():
    if session.get('minne'):
        text = 'Hej, jag känner igen dig.'
    else:
        session['minne'] = True
        text = 'Hej!'

    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run(debug=True)
