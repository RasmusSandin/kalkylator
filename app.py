#!/usr/bin/env python3
from flask import Flask, session, render_template
from random import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Something very secret and hard to guess!'

BOMB_PROBABILITY = 20

def generate_map():
    m = [[random() < 1/BOMB_PROBABILITY for x in range(20)] for y in range(10)]

    # Same as above double list comprehension.
    #
    # m = []
    # for y in range(10):
    #     row = []
    #     for x in range(20):
    #         row.append( random() < 1/BOMB_PROBABILITY )
    #     m.append(row)

    return m


@app.route("/")
def index():
    if not session.get('map'):
        session['map'] = generate_map()

    return render_template('index.html', map=session['map'])


if __name__ == "__main__":
    app.run(debug=True)
