'''
Created on Nov 28, 2012

@author: cosmin
'''
from google.appengine.ext import webapp, db
import jinja2
import os
import logging as log

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class ClustersP(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the clusters
        '''
        
        # Get the selected clusters_count
        clusters_count = self.request.get("clusters_count")
        log.info("K-means clusters for %s clusters." % clusters_count)

        #Get the clusters from the database    
        if clusters_count!='':
            clusters =db.GqlQuery("SELECT * "
                                "FROM Clusters "
                                "WHERE count = :1",
                                int(clusters_count))
            clusters=clusters.get()
            if clusters!=None:
                clusters.expand()
            log.info(str(clusters))
        
        #Generate the page
        template_values = { 'clusters': clusters}    
        template = jinja_environment.get_template('templates/clusters.html')
        self.response.out.write(template.render(template_values))
