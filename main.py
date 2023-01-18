from flask import Flask, render_template, request
from models import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    try:
        userName = request.form.get('userID')
        user = User(userName)
        return render_template('index.html', user_name=user.basic_info()['name'], user_picture=user.basic_info()['picture'], user_region=user.basic_info()['region'], user_id=user.basic_info()['id'])
    except:
        return '<h1>Não existe</h1>'

@app.route('/players/<player>')
def player_detail(player):
    user = User(player)
    return render_template('player_details.html', user_name=user.basic_info()['name'], user_picture=user.basic_info()['picture'], user_region=user.basic_info()['region'],
                           time_played=user.time_played(), combat_info=user.combat_info(), matches_info=user.matches_info())


if __name__ == '__main__':
    app.run(debug=True)