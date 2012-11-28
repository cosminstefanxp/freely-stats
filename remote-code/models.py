'''
Created on Nov 24, 2012

@author: cosmin
'''
from google.appengine.ext import db

TopJobs = [('PHP', 1972), ('Website Design', 1313), ('Graphic Design', 1233),
('HTML', 1163), ('Software Architecture', 811), ('MySQL', 778), ('SEO', 525),
('Mobile Phone', 454), ('Software Testing', 407), ('CSS', 373), ('Wordpress',
367), ('Link Building', 344), ('Web Hosting', 317), ('iPhone', 315),
('Javascript', 309), ('Website Management', 309), ('Website Testing', 300),
('Android', 254), ('Logo Design', 248), ('Photoshop', 240), ('Facebook', 210),
('Social Networking', 204), ('eCommerce', 191), ('.NET', 188), ('HTML5', 185),
('User Interface / IA', 170), ('C Programming', 168), ('AJAX', 167), ('jQuery \
Prototype', 161), ('Java', 160), ('C# Programming', 154), ('Joomla', 154),
('Windows Desktop', 154), ('Shopping Carts', 151), ('Amazon Web Services', 141),
('Linux', 132), ('Flash', 124), ('Web Scraping', 119), ('Word', 115), ('iPad',
114), ('SQL', 113), ('3D Animation', 108), ('Animation', 105), ('ASP', 102),
('Illustrator', 102), ('Video Services', 102), ('Illustration', 100), ('Script \
Install', 97), ('XML', 96), ('C++ Programming', 92), ('3D Modelling', 90),
('Objective C', 86), ('Visual Basic', 86), ('Magento', 85), ('Twitter', 77),
('3D Rendering', 71), ('Banner Design', 71), ('Database Administration', 67),
('Templates', 66), ('Shell Script', 63), ('Arts &amp; Crafts', 60), ('Icon \
Design', 60), ('Embedded Software', 55), ('Game Design', 55), ('PSD to HTML', 55),
('YouTube', 53), ('Python', 51), ('After Effects', 49), ('Paypal API', 48), 
('Blog Design', 44), ('Videography', 44), ('System Admin', 43), ('UNIX', 43),
('Drupal', 40), ('Microsoft', 40), ('Brochure Design', 40), ('Visual Arts', 40),
('Mac OS', 38), ('Microsoft Access', 36), ('Caricature &amp; Cartoons', 36),
('Cocoa', 35), ('3ds Max', 34), ('Photoshop Design', 34), ('Audio Services',
33), ('Corporate Identity', 33), ('Blackberry', 32), ('ActionScript', 32),
('Game Consoles', 30), ('Voice Talent', 30), ('CMS', 29), ('Usability Testing',
28), ('Ruby &amp; Ruby on Rails', 27), ('VoIP', 27), ('Web Security', 26),
('Cisco', 25), ('Prestashop', 25), ('Advertisement Design', 25), ('Delphi', 24),
('Print', 24), ('Perl', 23)]



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
    
        
