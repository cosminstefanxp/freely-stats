'''
Created on Nov 24, 2012

@author: cosmin
'''
from google.appengine.ext import db
from BitVector import BitVector
import logging

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
        return self.job + ": " + self.monthly_count;
    
class AcceptedBidderBehavior(db.Model):
    ''' 
    Class used to store info about how the accepted bidders are chosen for projects, 
    based on their nationality, in the Appengine datastore.
    '''
    country = db.StringProperty()
    bids_count = db.IntegerProperty()
    accepted = db.StringProperty()
    
    def __str__(self):
        return "%s [%d]: %s" % (self.country, self.bids_count, str(self.accepted_expanded))
    
    def expand(self):
        ''' Expands the serialized data in the object '''
        self.accepted_expanded = []
        accepted_split = self.accepted.split(";")
        left = self.bids_count
        for accepted_entry in accepted_split:
            a_country, a_count = accepted_entry.split(":", 2)
            self.accepted_expanded.append((a_country, int(a_count)))
            left -= int(a_count)
        if left > 0:
            self.accepted_expanded.append(('Others', left))    

class OutBidderBehavior(db.Model):
    '''
    Class used to store info about the project's countries to which a particular nationality bids most,
    in the Appengine datastore.
    '''
    country = db.StringProperty()
    bids_count = db.IntegerProperty()
    bids = db.StringProperty()
    
    def __str__(self):
        return "%s [%d]: %s" % (self.country, self.bids_count, str(self.bids_expanded))
    
    def expand(self):
        ''' Expands the serialized data in the object '''
        split_bids = self.bids.split(";")
        self.bids_expanded = []
        left = self.bids_count
        for bid in split_bids:
            b_country, b_count = bid.split(":", 2)
            self.bids_expanded.append((b_country, int(b_count)))
            left -= int(b_count)
        if left > 0:
            self.bids_expanded.append(('Others', left))
    
class CountryStats(db.Model):
    '''
    Class used to store statistics about a particular country, in the Appengine datastore.
    ''' 
    country = db.StringProperty()
    bids_count = db.IntegerProperty()
    frequent_words = db.TextProperty()
    word_count = db.IntegerProperty()
    unique_word_count = db.IntegerProperty()
    average_rating = db.FloatProperty() # Can be 0 if no user in that country has received a rating

    def __str__(self):
        return "%s [%d]: %d/%d (%s), %f - %s" % (self.country, self.bids_count, self.unique_word_count,
             self.word_count, str(self.lexical_diversity), self.average_rating, str(self.frequent_words_expanded))   
    
    def expand(self):
        ''' Expands the serialized data in the object '''
        self.lexical_diversity = self.word_count * 1.0 / self.unique_word_count
        words = self.frequent_words.split(";")
        self.frequent_words_expanded = []
        for w in words:
            word, count = w.split(':', 2)
            self.frequent_words_expanded.append((word, int(count)))

class RecommendationPatterns(db.Model):
    ''' 
    Class used to store the patterns used for recommendations, in the Appengine datastore.
    '''
    patterns = db.TextProperty()
    
    def expand(self):
        ''' Expands the serialized data in the object '''
        patterns = self.patterns.split(';')
        self.patterns_expanded = []
        self.projects_count = {}
        for line in patterns:
            patInt, count = line.split(":")
            bv = BitVector(intVal=int(patInt), size=200)
            self.patterns_expanded.append(bv)
            self.projects_count[int(patInt)] = int(count)
   
    def __str__(self):
        return "%s: %d" % (self.patterns_expanded[0], self.projects_count[self.patterns_expanded[0].intValue()])

class Clusters(db.Model):
    '''
    Class used to store the clusters resulted from k-means clustering, in the Appengine datastore.
    '''
    count = db.IntegerProperty()
    clusters = db.TextProperty()
    
    def expand(self):
        ''' Expands the serialized data in the object '''
        clusters_s = self.clusters.split(';')
        self.clusters_expanded = []
        for clust in clusters_s:
            self.clusters_expanded.append(clust.split('~'))
    
    def __str__(self):
        out = str(self.count) + ": "
        for clust in self.clusters_expanded:
            out += str(clust)
        return out 

class Earnings(db.Model):
    '''
    Class used to store information about earnings, in the Appengine datastore.
    '''
    data = db.TextProperty()
    
    def expand(self):
        ''' Expands the serialized data in the object '''
        data_s = self.data.split('~')
        self.data_expanded = []
        logging.info(data_s)
        for s in data_s:
            logging.info(s)
            cost, pattern = s.split(':',2)
            self.data_expanded.append((cost,pattern))
    
    def __str__(self):
        return str(self.data_expanded)
