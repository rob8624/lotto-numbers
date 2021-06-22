from flask import Flask, render_template
from random import randint



#create flask instance
app = Flask(__name__)

history=[]
lucky_history=[]


@app.route('/')
def index():
    random_int = []
    for num in range(1, 7):
        random_int.append(randint(1, 56))

    lucky_stars = []
    for num in range(1,3):
        lucky_stars.append(randint(1, 10))

    if len(history) == 0:
        print("no previous numbers")

    history.append(random_int)
    lucky_history.append(lucky_stars)
    print(lucky_history)


    return render_template('/index.html', random_int=random_int, lucky_stars=lucky_stars, history=history, lucky_history=lucky_history)

if __name__ == '__main__':
  app.run(debug=True)