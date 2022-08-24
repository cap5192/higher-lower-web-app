from flask import Flask
import random
app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="400">' \
           f'random number is : {random_number}'

@app.route('/<int:num>')
def guess(num):
    if num > random_number:
        return "<h1 style='color:blue;'>Too high, try again</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='400'>"
    elif num < random_number:
        return "<h1 style='color:red;'>Too Low, try again</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='400'>"
    else:
        return "<h1 style='color:green;'>You Found Me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='400'>"

if __name__ == "__main__":
    app.run(debug=True)