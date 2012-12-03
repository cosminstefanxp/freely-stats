'''
Created on Dec 1, 2012

@author: cosmin
'''
from google.appengine.ext import webapp
import logging as log
import jinja2
import os
from models import AcceptedBidderBehavior, OutBidderBehavior



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

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
        expanded_behaviors = []
        for b in behaviors:
            b.expand()
            expanded_behaviors.append(b)
            log.info(b);
        expanded_behaviors.sort(key=lambda x: x.country)
        countries = [c.country for c in expanded_behaviors]
        
        #Get the outbound bids from the database
        bids = OutBidderBehavior.all()
        bids.filter("country IN", countries)
        expanded_bids = []
        for b in bids:
            b.expand()
            log.info(b);
            expanded_bids.append(b)
        expanded_bids.sort(key=lambda x: x.country)    
                
        # Generate the page
        template_values = { "countries": countries, 'selectable_countries': selectable_countries, 'accepted_bids': expanded_behaviors, 'out_bids': expanded_bids  }
        
        template = jinja_environment.get_template('templates/bids.html')
        self.response.out.write(template.render(template_values))
        
        
