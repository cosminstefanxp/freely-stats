'''
Created on Nov 28, 2012

@author: cosmin
'''
from google.appengine.ext import webapp, db
import jinja2
import os
import logging as log
from models import TopJobs, Earnings

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class EarningsP(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the earnings
        '''
        selectable=[j[0] for j in TopJobs]
        selectable.sort(key=lambda x: x.lower())

        # Get the selected selected_jobs
        selected_jobs = self.request.get_all("job")
        selected_jobs = [j for j in selected_jobs if j in selectable]
        log.info("Earnings for selected jobs: " + str(selected_jobs))
        
        #Build the list of matching patterns
        matching=None
        searched=False
        if len(selected_jobs)>0:
            searched=True
            # Read patterns from database
            earnings_db = Earnings.all()
            earnings1, earnings2 = earnings_db.fetch(2)
            earnings1.expand()
            earnings2.expand()
    
            # Find out matching patterns
            matching_temp=[]
            for data in earnings1.data_expanded:
                valid=True
                for j in selected_jobs:
                    if not j in data[1]:
                        valid=False;
                        break;
                if valid:
                    matching_temp.append(data)
            #Split and prepare the matching elements
            if len(matching_temp)>0:
                matching=[(int(count), jobs.split(';')) for count, jobs in matching_temp]
                log.info("Found %d matches: %s" %(len(matching),str(matching)))
            else:
                log.info("No matches found...")
                    
        #Generate the page
        template_values = { 'selectable': selectable, 'selected_jobs':selected_jobs, 'matching':matching, 'searched':searched}
            
        template = jinja_environment.get_template('templates/earnings.html')
        self.response.out.write(template.render(template_values))
