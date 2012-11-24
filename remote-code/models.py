'''
Created on Nov 24, 2012

@author: cosmin
'''
from google.appengine.ext import db

class Job(db.Model):
    '''
    Class used to store info about the Jobs (Categories).
    '''
    id = db.IntegerProperty()
    name = db.StringProperty()
    seo_url = db.StringProperty(indexed=False)
    project_count = db.IntegerProperty()
        
