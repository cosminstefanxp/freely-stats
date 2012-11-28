'''
Created on Nov 28, 2012

@author: cosmin
'''
from google.appengine.ext import db, webapp
import logging
import jinja2
import os
from models import Trend
from models import TopJobs

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class SplitTrend:
    def __init__(self, job, values):
        self.job=job
        self.values=values

class Trends(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the trends.
        '''
        months = ["2012-11", "2012-10", "2012-09", "2012-08", "2012-07",
        "2012-06", "2012-05", "2012-04", "2012-03", "2012-02", "2012-01",
        "2011-12", "2011-11", "2011-10", "2011-09", "2011-08", "2011-07",
        "2011-06", "2011-05", "2011-04", "2011-03", "2011-02", "2011-01",
        "2010-12", "2010-11", "2010-10", "2010-09", "2010-08", "2010-07",
        "2010-06", "2010-05", "2010-04", "2010-03", "2010-02", "2010-01",
        "2009-12", "2009-11", "2009-10", "2009-09", "2009-08", "2009-07",
        "2009-06", "2009-05", "2009-04", "2009-03", "2009-02", "2009-01",
        "2008-12", "2008-11", "2008-10", "2008-09", "2008-08", "2008-07",
        "2008-06", "2008-05", "2008-04", "2008-03", "2008-02", "2008-01"]
        months.reverse()

        #Get jobs for trends
        jobs = self.request.get_all("job")
        jobs = [j for j in jobs if len(j) > 0]
        logging.info("Trends for jobs: " + ','.join(jobs))
        
        #Get the trends from the database
        trends=Trend.all()
        trends.filter("job IN",jobs)
        split_trends=[]
        for t in trends:
            nt=SplitTrend(t.job, t.monthly_count.split(';'))
            split_trends.append(nt)
            logging.info(t);
        trends_names=[t.job for t in trends]
        
        #Generate the page
        template_values = { 'jobs': TopJobs, 'trends': split_trends, 'trends_names': trends_names, 'count': 0, 'months': months}
        
        template = jinja_environment.get_template('templates/trends.html')
        self.response.out.write(template.render(template_values))
