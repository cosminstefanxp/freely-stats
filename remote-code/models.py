'''
Created on Nov 24, 2012

@author: cosmin
'''
from google.appengine.ext import db

TopJobs = [('PHP', 1855), ('Website Design', 1248), ('Graphic Design', 1132),
    ('HTML', 1081), ('Software Architecture', 875), ('MySQL', 750), ('Software Testing', 527),
    ('SEO', 444), ('Mobile Phone', 410), ('Website Management',
    409), ('Website Testing', 401), ('Web Hosting', 398), ('CSS', 384),
    ('Wordpress', 324), ('Javascript', 311), ('Link Building', 297), ('iPhone',
    269), ('Logo Design', 243), ('Photoshop', 218), ('Social Networking', 205),
    ('Facebook', 204), ('Amazon Web Services', 199), ('eCommerce', 197),
    ('Windows Desktop', 193), ('C Programming', 191), ('Android', 188), ('.NET',
    185), ('AJAX', 184), ('User Interface / IA', 172), ('Java', 163), ('C# Programming', 156),
    ('HTML5', 156), ('Shopping Carts', 152), ('Joomla', 141),
    ('Linux', 138), ('Script Install', 133), ('Flash', 132), ('jQuery / Prototype', 128),
    ('XML', 126), ('SQL', 117), ('Web Scraping', 112), ('Video Services', 107),
    ('C++ Programming', 104), ('Animation', 97), ('Shell Script', 96), ('Magento', 95),
    ('iPad', 95), ('Objective C', 89), ('ASP', 88), ('3D Animation', 86), ('Templates', 85),
    ('Illustration', 83), ('Icon Design', 79), ('Visual Basic', 77), ('Twitter', 76), ('3D Modelling', 73),
    ('Banner Design', 72), ('Arts & Crafts', 71), ('Database Administration',
    70), ('Game Design', 69), ('Blog Design', 64), ('Embedded Software', 62),
    ('Illustrator', 61), ('System Admin', 59), ('Visual Arts', 56), ('UNIX', 55),
    ('3D Rendering', 54), ('Drupal', 53), ('Mac OS', 46), ('Microsoft', 45),
    ('Python', 44), ('PSD to HTML', 43), ('Videography', 42), ('Cocoa', 41),
    ('YouTube', 39), ('After Effects', 39), ('VoIP', 37), ('Paypal API', 36),
    ('ActionScript', 36), ('Photoshop Design', 36), ('Audio Services', 34), ('Game Consoles', 33),
    ('Cisco', 30), ('Prestashop', 30), ('Ruby & Ruby on Rails', 29), ('Usability Testing', 28),
    ('Brochure Design', 28), ('Voice Talent', 28), ('CMS', 26), ('Photo Editing', 26), 
    ('Caricature & Cartoons', 25), ('Word', 24), ('Web Security', 23), ('3ds Max', 22),
    ('Advertisement Design', 22), ('Music', 22), ('Delphi', 21), ('Print', 21),
    ('Microsoft Access', 20), ('Blackberry', 20)];



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
    
        
