'''
Created on Nov 24, 2012

@author: cosmin
'''
from google.appengine.ext import db, webapp
import jinja2
import os
import random



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class Jobs(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the jobs
        '''
        # Compute count
        countV = self.request.get("count")
        if len(countV)==0:
            count = 150;
        else:
            count=int(countV)
            
        #check if randomize
        if self.request.get("randomize",default_value=1) != '1':
            randomize=False;
        else:
            randomize=True;
            
        # Get jobs
        q = db.GqlQuery("SELECT * FROM Job ORDER BY project_count DESC");
        jobs=q.fetch(count)
        
        if randomize:
            random.shuffle(jobs)
            
        #Generate the page
        template_values = { 'jobs': jobs, 'count': count, 'randomize':  randomize}
        
        template = jinja_environment.get_template('templates/jobs.html')
        self.response.out.write(template.render(template_values))


