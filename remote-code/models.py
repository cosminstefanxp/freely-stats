'''
Created on Nov 24, 2012

@author: cosmin
'''
from google.appengine.ext import db

class Job(db.Model):
    '''
    Class used to store info about the Jobs (Categories) in the Appengine datastore.
    '''
    id = db.IntegerProperty()
    name = db.StringProperty()
    seo_url = db.StringProperty(indexed=False)
    project_count = db.IntegerProperty()
    
class Trend(db.Model):
    '''
    Class used to store info about the Monthly trends per Job in the Appengine datastore.
    '''
    job = db.StringProperty();
    monthly_count = db.StringProperty(indexed=False);
    
    def __str__(self, *args, **kwargs):
        return self.job+": "+self.monthly_count;
    
        
