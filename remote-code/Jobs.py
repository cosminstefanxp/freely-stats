'''
Created on Nov 24, 2012

@author: cosmin
'''
from google.appengine.ext import db, webapp
import jinja2
import os
from models import Job



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class Jobs(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the jobs
        '''
        jobs = db.GqlQuery("SELECT * FROM Job ORDER BY project_count DESC");
        template_values = { 'jobs': jobs}
        
        template = jinja_environment.get_template('templates/jobs.html')
        self.response.out.write(template.render(template_values))


