import parse
from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/<hill>/<commons>/<kings>/<mcclelland>/')
def index(hill=None, commons=None, kings=None, mcclelland=None):
	# get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html")
	hill = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html")
	commons = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/1920-commons/1920-menu.html")
	kings = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/kings-court-english-house/daily-menu.html")
	mcclelland = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/cafe-at-mcclelland/daily-menu.html")
	return render_template('index.html', hill=hill, commons=commons, kings=kings, mcclelland=mcclelland)

@app.route('/default')
@app.route('/<hill>/<commons>/<kings>/<mcclelland>/')
def default(hill=None, commons=None, kings=None, mcclelland=None):
	# get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html")
	hill = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html")
	commons = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/1920-commons/1920-menu.html")
	kings = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/kings-court-english-house/daily-menu.html")
	mcclelland = parse.get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/cafe-at-mcclelland/daily-menu.html")
	return render_template('default.html', hill=hill, commons=commons, kings=kings, mcclelland=mcclelland)


if __name__ == '__main__':
    app.run(debug=True)
