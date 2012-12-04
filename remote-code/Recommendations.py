from google.appengine.ext import webapp
import jinja2
import logging as log
import os
from compute_recommendations import Compute_Recommendations
from models import RecommendationPatterns


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Recommendations(webapp.RequestHandler):
    
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
        
        # Read patterns from database
        pattern_db = RecommendationPatterns.all()
        patterns = pattern_db.get()
        patterns.expand()
        
        # Get the selected selected_jobs
        selected_jobs = self.request.get_all("job")
        selected_jobs = [j for j in selected_jobs if j in top_jobs]
        selected_jobs.sort()
        log.info("Recommendations for selected_jobs: " + str(selected_jobs))
        
        recommendations = []
        top_matches = None   
        if len(selected_jobs) > 0:
            recommendation_computer = Compute_Recommendations()

            # Compute user's pattern
            my_pattern = recommendation_computer.compute_pattern(selected_jobs)

            # Run the recommendations computer
            top_matches = recommendation_computer.topMatches(patterns.patterns_expanded, my_pattern, patterns.projects_count)
            log.info("Top matches: " + str(top_matches));
            
            recommendations = recommendation_computer.getRecommendations(patterns.patterns_expanded, my_pattern)
            rec_enabled = True
            log.info("User's recommendations: " + str(recommendations))
        else:
            rec_enabled = False
            log.info("No valid selected jobs. Not running recommendations alghoritms")
         
        #Generate the page
        template_values = { 'selected_jobs': selected_jobs, 'jobs': top_jobs, 'top_matches': top_matches, 'recommendations': recommendations, 'rec_enabled': rec_enabled}
        
        template = jinja_environment.get_template('templates/recommendations.html')
        self.response.out.write(template.render(template_values))
        
