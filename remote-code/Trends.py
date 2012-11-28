'''
Created on Nov 28, 2012

@author: cosmin
'''
from google.appengine.ext import db, webapp
import logging
import jinja2
import os
from models import Trend

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Trends(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the trends.
        '''
        #Get jobs for trends
        jobs = self.request.get_all("job")
        jobs = [j for j in jobs if len(j) > 0]
        logging.info("Trends for jobs: " + ','.join(jobs))
        
        #Get the trends from the database
        trends=Trend.all()
        trends.filter("job IN",['Delphi','Flash'])
        for t in trends:
            logging.info(t);
                
        #Generate the page
        template_values = { 'jobs': [], 'count': 0}
        
        template = jinja_environment.get_template('templates/trends.html')
        self.response.out.write(template.render(template_values))
