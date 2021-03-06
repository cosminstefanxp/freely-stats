import webapp2

import jinja2
import os
from Jobs import Jobs
from Trends import Trends
from Bids import Bids
from CountriesStats import CountriesStats
from Networks import Networks
from Recommendations import Recommendations
from ClustersP import ClustersP
from EarningsP import EarningsP
import logging
 
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Home(webapp2.RequestHandler):
    def get(self):
        try:
            logging.info("New request from %s: %s/%s - %s " %(self.request.remote_addr,self.request.headers.get('X-AppEngine-Country'),self.request.headers.get('X-AppEngine-Country'), str(self.request.headers)))
        except KeyError:
            logging.info("New request from %s" %(self.request.url))
        template = jinja_environment.get_template('templates/home.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', Home),
                               ('/index.html', Home),
                               ('/trends.html', Trends),
                               ('/jobs.html', Jobs),
                               ('/bids.html', Bids),
                               ('/country_stats.html', CountriesStats),
                               ('/networks.html', Networks),
                               ('/clusters.html', ClustersP),
                               ('/recommendations.html', Recommendations),
                               ('/earnings.html', EarningsP)],
                              debug=True)
