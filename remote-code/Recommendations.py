from google.appengine.ext import webapp, db
import jinja2
import logging as log
import os
from compute_recommendations import Compute_Recommendations
from BitVector import *
from models import RecommendationPatterns


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Recommendations(webapp.RequestHandler):
    
    def compute_pattern(self, job_list):
        bitVector = BitVector(size=200)
        ids = []
        for job in job_list:
            if(job in self.top_200):
                _id = self.top_200.index(job)
                ids.append(_id)
        for _id in ids:
            bitVector[_id] = 1
        return bitVector
    
    def get(self):
        top_jobs = ['PHP', 'Website Design', 'Graphic Design', 'HTML',
            'Software Architecture', 'MySQL', 'Software Testing', 'SEO', 'Mobile Phone',
            'Website Management', 'Website Testing', 'Web Hosting', 'CSS',
            'Wordpress', 'Javascript', 'Link Building', 'iPhone', 'Logo Design',
            'Photoshop', 'Social Networking', 'Facebook', 'Amazon Web Services',
            'eCommerce', 'Windows Desktop', 'C Programming', 'Android', '.NET',
            'AJAX', 'User Interface / IA', 'Java', 'C# Programming', 'Shopping Carts',
            'Joomla', 'Linux', 'Script Install', 'Flash', 'jQuery / Prototype',
            'XML', 'SQL', 'Web Scraping', 'Video Services', 'C++ Programming',
            'Animation', 'Shell Script', 'Magento', 'iPad',
            'Objective C', 'ASP', '3D Animation', 'Templates', 'Illustration',
            'Icon Design', 'Visual Basic', 'Twitter', '3D Modelling', 'Banner Design',
            'Arts & Crafts', 'Database Administration', 'Game Design',
            'Blog Design', 'Embedded Software', 'Illustrator', 'System Admin',
            'Visual Arts', 'UNIX', '3D Rendering', 'Drupal', 'Mac OS', 'Microsoft',
            'Python', 'PSD to HTML', 'Videography', 'Cocoa', 'YouTube', 'Paypal API',
            'ActionScript', 'Photoshop Design', 'Audio Services', 'Prestashop',
            'Ruby & Ruby on Rails', 'Usability Testing', 'Brochure Design',
            'Voice Talent', 'CMS', 'Photo Editing', 'Word', 'Web Security',
            'Advertisement Design', 'Music', 'Delphi', 'Microsoft Access',
            'Blackberry', 'Corporate Identity', 'Perl', 'Photography',
            'Chrome OS', 'Flyer Design', 'Business Cards', 'XSLT', 'Microsoft Exchange',
            'OSCommerce', 'T-Shirts', 'Virtuemart']
        top_jobs.sort(key=lambda x:x.lower())
        self.top_200 = [ 'PHP', 'Website Design', 'Graphic Design', 'HTML', 'Software Architecture', 'MySQL', 'Software Testing', 'SEO',
            'Mobile Phone', 'Website Management', 'Website Testing', 'Web Hosting', 'CSS', 'Wordpress', 'Javascript',
            'Link Building', 'iPhone', 'Logo Design', 'Photoshop', 'Social Networking', 'Facebook', 'Amazon Web Services',
            'eCommerce', 'Windows Desktop', 'C Programming', 'Android', '.NET', 'AJAX', 'User Interface / IA', 'Java',
            'C# Programming', 'HTML5', 'Shopping Carts', 'Joomla', 'Linux', 'Script Install', 'Flash', 'jQuery / Prototype',
            'XML', 'SQL', 'Web Scraping', 'Video Services', 'C++ Programming', 'Animation', 'Shell Script', 'Magento',
            'iPad', 'Objective C', 'ASP', '3D Animation', 'Templates', 'Illustration', 'Icon Design', 'Visual Basic',
            'Twitter', '3D Modelling', 'Banner Design', 'Arts & Crafts', 'Database Administration', 'Game Design',
            'Blog Design', 'Embedded Software', 'Illustrator', 'System Admin', 'Visual Arts', 'UNIX', '3D Rendering',
            'Drupal', 'Mac OS', 'Microsoft', 'Python', 'PSD to HTML', 'Videography', 'Cocoa', 'YouTube', 'After Effects',
            'VoIP', 'Paypal API', 'ActionScript', 'Photoshop Design', 'Audio Services', 'Game Consoles', 'Cisco',
            'Prestashop', 'Ruby & Ruby on Rails', 'Usability Testing', 'Brochure Design', 'Voice Talent', 'CMS',
            'Photo Editing', 'Caricature & Cartoons', 'Word', 'Web Security', '3ds Max', 'Advertisement Design', 'Music',
            'Delphi', 'Print', 'Microsoft Access', 'Blackberry', 'Corporate Identity', 'Open Cart', 'Perl',
            'Visual Basic for Applications', 'Photography', 'Chrome OS', 'Google App Engine', 'Flyer Design',
            'Business Cards', 'Video Broadcasting', 'Asterisk PBX', 'Computer Security', 'XSLT', 'Microsoft Exchange',
            'OSCommerce', 'Covers & Packaging', 'Flash 3D', 'Presentations', 'T-Shirts', 'Apache', 'Oracle',
            'Building Architecture', 'Stationery Design', 'Assembly', 'Google Analytics', 'J2EE', 'node.js', 'Poster Design',
            'Silverlight', 'Unity 3D', 'Windows Server', 'Zen Cart', 'Amazon Kindle', 'Flex', 'Invitation Design', 'Maya',
            'Motion Graphics', 'Apple Safari', 'JSP', 'Concept Design', 'CakePHP', 'Google Chrome', 'OpenGL', 'Smarty PHP',
            'Social Engine', 'Fashion Design', 'Fashion Modeling', 'InDesign', 'Big Data', 'Codeigniter', 'Forum Software',
            'Linkedin', 'Metatrader', 'MMORPG', 'Moodle', 'Virtuemart', 'Volusion', 'Interior Design', 'Post-Production',
            'Google Web Toolkit', 'Pinterest', 'SAP', 'Sharepoint', 'SugarCRM', 'UML Design', 'vTiger', 'WHMCS', 'Windows API',
            'WPF', 'Android Honeycomb', 'Blog Install', 'Django', 'DNS', 'Google Earth', 'PhoneGap', 'Photoshop Coding',
            'TaoBao API', 'VPS', 'Zend', 'Geolocation', 'Windows Mobile', 'Final Cut Pro', 'Format & Layout',
            'Industrial Design', 'Infographics', 'Cloud Computing', 'Cold Fusion', 'Dynamics', 'eLearning', 'FileMaker', 'Kinect',
            'NoSQL Couch & Mongo', 'x86/x64 Assembler', '3D Printing', 'Dreamweaver', 'Landing Pages', 'Typography',
            'Agile Development', 'BigCommerce', 'Boonex Dolphin']
        
        # Read patterns from database
        pattern_db = RecommendationPatterns.all()
        patterns = pattern_db.get()
        patterns.expand()
        
        # Get the selected selected_jobs
        selected_jobs = self.request.get_all("job")
        selected_jobs = [j for j in selected_jobs if j in top_jobs]
        selected_jobs.sort()
        log.info("Recommendations for selected_jobs: " + str(selected_jobs))
        
        recommendations = None
        top_matches = None
        if len(selected_jobs) > 0:
            # Compute user's pattern
            my_pattern = self.compute_pattern(selected_jobs)
            
            # Run the recommendations computer
            recommendation_computer = Compute_Recommendations()
            top_matches = recommendation_computer.topMatches(patterns.patterns_expanded, my_pattern, patterns.projects_count)
            log.info("Top matches: " + str(top_matches));
            
            recommendations = recommendation_computer.getRecommendations(patterns.patterns_expanded, my_pattern)
            log.info("User's recommendations: " + str(recommendations))
        else:
            log.info("No valid selected jobs. Not running recommendations alghoritms")
         
        #Generate the page
        template_values = { 'selected_jobs': selected_jobs, 'jobs': top_jobs, 'top_matches': top_matches, 'recommendations': recommendations}
        
        template = jinja_environment.get_template('templates/recommendations.html')
        self.response.out.write(template.render(template_values))
        
