from flask import Flask
from flask import render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Curie')

@app.route('/another-page')
def another_page():
    return 'This is another web page' 

# /users/profile/123
# users/gocodeup
@app.route('/hello/<name>')
def sayhello(name):
    return f'Hello, {name}!'

# 6 sided dice roll number generator
@app.route('/roll-dice')
def roll():
    num = np.arange(1,7)
    roll = np.random.choice(num)
    return render_template('roll.html', roll=roll)

# roll 3 dice that are 6 sided
@app.route('/roll-3-dice')
def rolls():
    nums = np.arange(1,7)
    rolls = np.random.choice(nums, 3)
    rolls = np.array_str(rolls)
    rolls = rolls.strip('[]')
    return render_template('roll-3.html', rolls=rolls)

# rolling 12 100 sided die for your level 67 warlord in WoW
@app.route('/nerd-roll')
def nerdroll():
    nums = np.arange(1,101)
    rolls = np.random.choice(nums, 12)
    rolls = np.array_str(rolls)
    rolls = rolls.strip('[]')
    return rolls

