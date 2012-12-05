'''
Created on Nov 28, 2012

@author: cosmin
'''
from google.appengine.ext import webapp, db
import jinja2
import os
import logging as log
from models import TopJobs

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class EarningsP(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the earnings
        '''
        
#        # Get the selected clusters_count
#        clusters_count = self.request.get("clusters_count")
#        log.info("K-means clusters for %s clusters." % clusters_count)
#
#        #Get the clusters from the database
#        clusters=None   
#        if clusters_count!='':
#            clusters_count=int(clusters_count)
#            clusters =db.GqlQuery("SELECT * "
#                                "FROM Clusters "
#                                "WHERE count = :1",
#                                clusters_count)
#            clusters=clusters.get()
#            if clusters!=None:
#                clusters.expand()
#            log.info(str(clusters))
#        else:
#            clusters_count=-1 
        selectable=[j[0] for j in TopJobs]
        selectable.sort(key=lambda x: x.lower())
        log.info("s"+str(selectable))
        
        #Generate the page
        template_values = { 'selectable': selectable}
            
        template = jinja_environment.get_template('templates/earnings.html')
        self.response.out.write(template.render(template_values))
