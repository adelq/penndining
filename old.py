import parse
from flask import Blueprint, render_template

bpp = Blueprint('old', __name__)

HALL_URLS = [
    "http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html",
    "http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/1920-commons/1920-menu.html",
    "http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/english-house/daily-menu.html",
    "http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/mcclelland-express/daily-menu.html"
]

@bpp.route('/old/')
@bpp.route('/<hill>/<commons>/<kings>/<mcclelland>/')
def index(hill=None, commons=None, kings=None, mcclelland=None):
    hill = parse.get_all_meals(HALL_URLS[0])
    commons = parse.get_all_meals(HALL_URLS[1])
    kings = parse.get_all_meals(HALL_URLS[2])
    mcclelland = parse.get_all_meals(HALL_URLS[3])
    return render_template('default.html', hill=hill, commons=commons, kings=kings, mcclelland=mcclelland)


@bpp.route('/')
@bpp.route('/<hill>/<commons>/<kings>/<mcclelland>/')
def default(hill=None, commons=None, kings=None, mcclelland=None):
    hill, commons, kings, mcclelland = parse.get_all_meals_concurrent(HALL_URLS)
    return render_template('default.html', hill=hill, commons=commons, kings=kings, mcclelland=mcclelland)
