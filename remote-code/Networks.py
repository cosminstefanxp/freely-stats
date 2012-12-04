'''
Created on Nov 28, 2012

@author: cosmin
'''
from google.appengine.ext import webapp
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class Networks(webapp.RequestHandler):
    
    def get(self):
        '''
        The class serving the page for the trends.
        '''
        template = jinja_environment.get_template('templates/networks.html')
        self.response.out.write(template.render([]))
