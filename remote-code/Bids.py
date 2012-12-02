'''
Created on Dec 1, 2012

@author: cosmin
'''
from google.appengine.ext import webapp
import logging as log
import jinja2
import os
from models import AcceptedBidderBehavior



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class SplitAcceptedBidders:
    def __init__(self, behavior):
        self.country = behavior.country
        self.bids_count = behavior.bids_count
        self.accepted = []
        accepted_split = behavior.accepted.split(";")
        for accepted_entry in accepted_split:
            a_country, a_count = accepted_entry.split(":", 2)
            self.accepted.append((a_country, a_count))
    
    def __str__(self):
        return "%s [%d]: %s" % (self.country, self.bids_count, self.accepted)  

class Bids(webapp.RequestHandler):
    
    def __init__(self, *args, **kwargs):
        webapp.RequestHandler.__init__(self, *args, **kwargs)
    
    def get(self):
        '''
        The class serving the page for information about bids
        '''
        # Init selectable countries
        selectable_countries = ["United States", "Australia", "United Kingdom", "Canada",
        "India", "Germany", "Pakistan", "Bangladesh", "Netherlands", "France",
        "Italy", "Singapore", "Spain", "Sweden", "Denmark", "Israel", "Norway",
        "Malaysia", "Hong Kong"];
        selectable_countries.sort();
        
        # Get countries for biddings
        countries = self.request.get_all("country")
        countries = [j for j in countries if j in selectable_countries]
        log.info("Bids for countries: " + ",".join(countries))
        
        #Get the behaviors from the database
        behaviors = AcceptedBidderBehavior.all()
        behaviors.filter("country IN", countries)
        split_behaviors = []
        for b in behaviors:
            s = SplitAcceptedBidders(b)
            split_behaviors.append(s)
            log.info(s);
        countries = [c.country for c in split_behaviors]
                
        # Generate the page
        template_values = { "countries": countries, 'selectable_countries': selectable_countries, 'accepted_bids': split_behaviors }
        
        template = jinja_environment.get_template('templates/bids.html')
        self.response.out.write(template.render(template_values))
        
        
