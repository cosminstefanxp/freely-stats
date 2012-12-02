class Compute_Recommendations:
    def __init__(self):
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
        
    def get_jobs(self, vector): 
        jobs = []
        for i in range(200):
            if(vector[i] == 1):
                jobs.append(self.top_200[i])
        return jobs
    
    def sim_distance(self, v1, v2):
        '''
        # Get the list of shared_items
        print v1.hamming_distance(v2)
        print v1
        print v2
        print " ================ \n\n"
        si={}
        for item in v1:
            if item in v2:
                si[item]=1
        # if they have no ratings in common, return 0
        if len(si)==0: return 0
        # Add up the squares of all the differences
        sum_of_squares=sum([pow(v1[item]-v2[item],2)
                          for item in v1 if item in v2])
        '''
        return 1.0/(1.0 + v1.hamming_distance(v2)*1.0)
    
    def topMatches(self, vectors,person_vector, counts, n=5):
        scores=[(self.sim_distance(person_vector,other),other)
            for other in vectors]
        # Sort the list so the highest scores appear at the top 
        scores.sort( )
        scores.reverse( )
        job_scores = []
        for score in scores:
            count = counts[score[1].intValue()]
            jobs = self.get_jobs(score[1])
            job_scores.append((count, jobs))
        job_scores = job_scores[0:n]
        job_scores.sort( key=lambda x : x[0], reverse=True)
        return job_scores
    
    
    # Gets recommendations for a person by using a weighted average
         # of every other user's rankings
    def getRecommendations(self, vectors,person):
        totals={}
        simSums={}
        for other in vectors:
            if (other&person).intValue() == 0: 
                continue
            sim=self.sim_distance(person,other)
            # ignore scores of zero or lower
            if sim<0: continue
            differences = other & ~person
            jobs = self.get_jobs(differences)

            for job in jobs:
                print job
                # Similarity * Score 
                totals.setdefault(job,0.0)
                totals[job]+= sim 
                # Sum of similarities 
               # simSums.setdefault(job,0.0) 
                #simSums[job]+=sim
                # Create the normalized list
        rankings=[(total,job)  for job,total in totals.items()]
        # Return the sorted list 
        rankings.sort( ) 
        rankings.reverse( ) 
        return rankings[:10]