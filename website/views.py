import requests as requests
from flask import render_template, request, Blueprint

views = Blueprint('views', __name__)

BASE = "https://api.opendota.com/api/"


@views.route('/history', methods=['POST'])
def get_match_history():
    steam_id = request.form['steam_id']
    r = requests.get(
        BASE + 'players/' + steam_id + '/matches')
    match_list = r.json()
    return render_template('history.html', match_list=match_list)


@views.route('/match-details', methods=['POST'])
def get_match_details():
    pass


@views.route('/')
def index():
    return render_template('index.html')
