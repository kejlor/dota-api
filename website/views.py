import requests as requests
from flask import render_template, request, Blueprint

views = Blueprint('views', __name__)


@views.route('/history', methods=['POST'])
def get_match_history():
    steam_id = request.form['steam_id']
    r = requests.get(
        'https://api.opendota.com/api/players/' + steam_id + '/matches')
    match_list = r.json()
    return render_template('history.html', match_list=match_list)


@views.route('/')
def index():
    return render_template('index.html')
