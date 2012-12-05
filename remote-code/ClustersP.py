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
        selectable_counts=[10,11,12,13,14,15,16,18,20,22,24,26]
        
        # Get the selected clusters_count
        clusters_count = self.request.get("clusters_count")
        log.info("K-means clusters for %s clusters." % clusters_count)

        #Get the clusters from the database
        clusters=None   
        if clusters_count!='':
            clusters_count=int(clusters_count)
            clusters =db.GqlQuery("SELECT * "
                                "FROM Clusters "
                                "WHERE count = :1",
                                clusters_count)
            clusters=clusters.get()
            if clusters!=None:
                clusters.expand()
            log.info(str(clusters))
        else:
            clusters_count=-1 
        
        #Generate the page
        template_values = { 'selectable': selectable_counts, 'clusters_count': clusters_count, 'clusters': clusters}    
        template = jinja_environment.get_template('templates/clusters.html')
        self.response.out.write(template.render(template_values))
