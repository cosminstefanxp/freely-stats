import json
import re
import BitVector
from BitVector import *
import compute_recommendations
from compute_recommendations import Compute_Recommendations

class Recommendations:#(webapp.RequestHandler):
    
    def compute_pattern(self, job_list):
        bitVector = BitVector( size = 200 )
        ids = []
        for job in job_list:
            if(job in self.top_200):
                id = self.top_200.index(job)
                ids.append(id)
        for id in ids:
            bitVector[id] = 1
        #print bitVector
        return bitVector
    
    def get(self):
        self.top_200 = [ 'PHP', 'Website Design', 'Graphic Design', 'HTML', 'Software Architecture', 'MySQL', 'Software Testing', 'SEO',
            'Mobile Phone', 'Website Management', 'Website Testing', 'Web Hosting', 'CSS', 'Wordpress', 'Javascript',
            'Link Building', 'iPhone', 'Logo Design', 'Photoshop', 'Social Networking', 'Facebook', 'Amazon Web Services',
            'eCommerce', 'Windows Desktop', 'C Programming', 'Android', '.NET', 'AJAX', 'User Interface / IA', 'Java',
            'C# Programming', 'HTML5', 'Shopping Carts', 'Joomla', 'Linux', 'Script Install', 'Flash', 'jQuery / Prototype',
            'XML', 'SQL', 'Web Scraping', 'Video Services', 'C++ Programming', 'Animation', 'Shell Script', 'Magento',
            'iPad', 'Objective C', 'ASP', '3D Animation', 'Templates', 'Illustration', 'Icon Design', 'Visual Basic',
            'Twitter', '3D Modelling', 'Banner Design', 'Arts &amp; Crafts', 'Database Administration', 'Game Design',
            'Blog Design', 'Embedded Software', 'Illustrator', 'System Admin', 'Visual Arts', 'UNIX', '3D Rendering',
            'Drupal', 'Mac OS', 'Microsoft', 'Python', 'PSD to HTML', 'Videography', 'Cocoa', 'YouTube', 'After Effects',
            'VoIP', 'Paypal API', 'ActionScript', 'Photoshop Design', 'Audio Services', 'Game Consoles', 'Cisco',
            'Prestashop', 'Ruby &amp; Ruby on Rails', 'Usability Testing', 'Brochure Design', 'Voice Talent', 'CMS',
            'Photo Editing', 'Caricature &amp; Cartoons', 'Word', 'Web Security', '3ds Max', 'Advertisement Design', 'Music',
            'Delphi', 'Print', 'Microsoft Access', 'Blackberry', 'Corporate Identity', 'Open Cart', 'Perl',
            'Visual Basic for Applications', 'Photography', 'Chrome OS', 'Google App Engine', 'Flyer Design',
            'Business Cards', 'Video Broadcasting', 'Asterisk PBX', 'Computer Security', 'XSLT', 'Microsoft Exchange',
            'OSCommerce', 'Covers &amp; Packaging', 'Flash 3D', 'Presentations', 'T-Shirts', 'Apache', 'Oracle',
            'Building Architecture', 'Stationery Design', 'Assembly', 'Google Analytics', 'J2EE', 'node.js', 'Poster Design',
            'Silverlight', 'Unity 3D', 'Windows Server', 'Zen Cart', 'Amazon Kindle', 'Flex', 'Invitation Design', 'Maya',
            'Motion Graphics', 'Apple Safari', 'JSP', 'Concept Design', 'CakePHP', 'Google Chrome', 'OpenGL', 'Smarty PHP',
            'Social Engine', 'Fashion Design', 'Fashion Modeling', 'InDesign', 'Big Data', 'Codeigniter', 'Forum Software',
            'Linkedin', 'Metatrader', 'MMORPG', 'Moodle', 'Virtuemart', 'Volusion', 'Interior Design', 'Post-Production',
            'Google Web Toolkit', 'Pinterest', 'SAP', 'Sharepoint', 'SugarCRM', 'UML Design', 'vTiger', 'WHMCS', 'Windows API',
            'WPF', 'Android Honeycomb', 'Blog Install', 'Django', 'DNS', 'Google Earth', 'PhoneGap', 'Photoshop Coding',
            'TaoBao API', 'VPS', 'Zend', 'Geolocation', 'Windows Mobile', 'Final Cut Pro', 'Format &amp; Layout',
            'Industrial Design', 'Infographics', 'Cloud Computing', 'Cold Fusion', 'Dynamics', 'eLearning', 'FileMaker', 'Kinect',
            'NoSQL Couch &amp; Mongo', 'x86/x64 Assembler', '3D Printing', 'Dreamweaver', 'Landing Pages', 'Typography',
            'Agile Development', 'BigCommerce', 'Boonex Dolphin']
        
        #TODO: all_jobs_int
        all_jobs = []
        job_count = {}
        fin = open("patterns_400.dict", "r")
        for line in fin.readlines():
            line = line.split(":")
            all_jobs.append(BitVector(intVal = int(line[0]), size = 200))
            job_count[int(line[0])] = int(line[1][:-2])
        
        #TODO:
        my_jobs = ["PHP", "SQL"]
        my_vector = self.compute_pattern(my_jobs)
        
        recommendation_computer = Compute_Recommendations()
        
        #scores = recommendation_computer.topMatches(all_jobs, my_vector, job_count)
        #print scores
        
        recommendation = recommendation_computer.getRecommendations(all_jobs, my_vector)
        print recommendation
        
rec = Recommendations()
rec.get()     
        