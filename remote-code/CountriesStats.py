'''
Created on Dec 2, 2012

@author: cosmin
'''

from google.appengine.ext import webapp, db
import jinja2
import logging as log
import os
from models import CountryStats, OutBidderBehavior

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CountriesStats(webapp.RequestHandler):

    def get(self):
        '''
        The class serving the page for showing statistics about countries.
        '''
        # Init selectable countries
        selectable_countries = ['India', 'Pakistan', 'Bangladesh', 'United States', 'Vietnam', 'Romania',
            'United Kingdom', 'Philippines', 'China', 'Sri Lanka', 'Ukraine', 'Canada', 'Egypt', 'Australia',
            'Indonesia', 'Serbia and Montenegro', 'Bulgaria', 'Nepal', 'Poland', 'Russian Federation',
            'Argentina', 'Italy', 'Spain', 'Brazil', 'Portugal', 'Germany', 'Turkey', 'Malaysia', 'Kenya',
            'United Arab Emirates', 'Florida', 'Mexico', 'Nigeria', 'France', 'Greece', 'Morocco', 'Bolivia',
            'Moldova', 'Croatia', 'South Africa', 'Sweden', 'Iran', 'Bosnia and Herzegovina', 'Macedonia',
            'Singapore', 'Belarus', 'Hungary', 'Tunisia', 'Algeria', 'Peru', 'Netherlands', 'Hong Kong',
            'Saudi Arabia', 'Israel', 'New Zealand', 'Estonia', 'Colombia', 'Denmark', 'Lithuania', 'Thailand',
            'Armenia', 'Switzerland', 'Austria', 'Uruguay', 'Japan', 'Cyprus', 'Venezuela', 'Czech Republic',
            'Kazakhstan', 'Slovak Republic', 'Albania', 'Dominican Republic', 'Lebanon', 'Slovenia', 'Chile',
            'Mauritius', 'Ireland', 'Belgium', 'Latvia', 'Palestine', 'Jamaica', 'Georgia', 'Cameroon', 'Gambia',
            'Puerto Rico', 'Qatar', 'Jordan', 'Costa Rica', 'Finland', 'El Salvador', 'Panama', 'Ethiopia', 'Norway'];
        selectable_countries.sort();
        
        # Get the selected countries
        countries = self.request.get_all("country")
        countries = [j for j in countries if j in selectable_countries]
        log.info("Stats for countries: " + ",".join(countries))
        
        #Get the stats from the database
        stats = CountryStats.all()
        stats.filter("country IN", countries)
        expanded_stats = []
        for s in stats:
            s.expand()
            log.info(s);
            expanded_stats.append(s)
        countries = [c.country for c in stats]
        expanded_stats.sort(key=lambda x: x.country)
        
        #Get the outbound bids from the database
        bids = OutBidderBehavior.all()
        bids.filter("country IN", countries)
        expanded_bids = []
        for b in bids:
            b.expand()
            log.info(b);
            expanded_bids.append(b)
        expanded_bids.sort(key=lambda x: x.country)

        #Generate the page
        template_values = { 'selectable_countries': selectable_countries, 'countries':countries,
                'stats': expanded_stats, 'bids': expanded_bids }
        
        template = jinja_environment.get_template('templates/country_stats.html')
        self.response.out.write(template.render(template_values))

