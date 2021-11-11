import requests as requests
from flask import render_template, request, Blueprint

views = Blueprint('views', __name__)

BASE = "https://api.opendota.com/api/"


@views.route('/history', methods=['POST'])
def get_match_history():
    steam_id = request.form['steam_id']
    user_request = requests.get(
        BASE + 'players/' + steam_id + '/matches')
    match_list = user_request.json()
    return render_template('history.html', match_list=match_list)


@views.route('/match-details/<match_id>', methods=['GET'])
def get_match_details(match_id):
    user_request = requests.get(BASE + '/matches/' + match_id)
    match_details = user_request.json()
    return render_template('match_details.html', match_details=match_details)


@views.route('/')
def index():
    return render_template('index.html')
