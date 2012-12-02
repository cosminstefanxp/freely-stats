import webapp2

import jinja2
import os
from Jobs import Jobs
from Trends import Trends
from Bids import Bids
 
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Home(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/home.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', Home),
                               ('/index.html', Home),
                               ('/trends.html', Trends),
                               ('/jobs.html', Jobs),
                               ('/bids.html', Bids)],
                              debug=True)
