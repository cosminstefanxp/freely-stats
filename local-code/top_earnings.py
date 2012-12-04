import json
import re
from BitVector import *
from foa import Foa

top_200 = [ 'PHP', 'Website Design', 'Graphic Design', 'HTML', 'Software Architecture', 'MySQL', 'Software Testing', 'SEO',
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
    
hash_jobs = {'XSLT': 112, 'Embedded Software': 61, 'OpenGL': 142, 'Delphi': 96, 'Flash': 36, 'J2EE': 125, 'Database Administration': 58,
             '3ds Max': 93, 'Video Broadcasting': 109, 'User Interface / IA': 28, 'Dreamweaver': 194, 'MySQL': 5, 'Blog Install': 170, 
             'Open Cart': 101, 'Final Cut Pro': 181, 'Smarty PHP': 143, 'Website Design': 1, 'Photography': 104, 'Javascript': 14, 
             'YouTube': 74, 'Moodle': 154, 'MMORPG': 153, 'Geolocation': 179, 'C++ Programming': 42, 'eLearning': 188, 'Apache': 119, 
             'Cloud Computing': 185, 'SAP': 161, 'Icon Design': 52, 'Silverlight': 128, 'Videography': 72, 'Illustrator': 62, 
             'Agile Development': 197, 'FileMaker': 189, 'Drupal': 67, 'Microsoft Exchange': 113, 'Script Install': 35, 'Stationery Design': 122, 
             'Unity 3D': 129, 'Django': 171, 'AJAX': 27, 'Google App Engine': 106, 'iPhone': 16, 'Mobile Phone': 8, 'CakePHP': 140, 
             'Social Engine': 144, 'node.js': 126, 'Cisco': 82, 'PhoneGap': 174, 'Google Chrome': 141, 'vTiger': 165, 'TaoBao API': 176, 
             'Poster Design': 127, 'Google Web Toolkit': 159, 'Magento': 45, 'SQL': 39, 'BigCommerce': 198, 'Music': 95, 'System Admin': 63, 
             'PHP': 0, 'Video Services': 41, 'iPad': 46, 'Java': 29, 'Pinterest': 160, 'Industrial Design': 183, 'Flash 3D': 116, 
             'Photoshop Coding': 175, 'Perl': 102, 'Kinect': 190, 'Visual Basic for Applications': 103, 'Print': 97, 'Android': 25, 'CMS': 88, 
             'Paypal API': 77, 'Interior Design': 157, 'Web Scraping': 40, 'HTML': 3, 'Facebook': 20, 'Forum Software': 150, 'Microsoft Access': 98, 
             'Apple Safari': 137, 'Shopping Carts': 32, 'Corporate Identity': 100, 'Word': 91, 'Business Cards': 108, 'Landing Pages': 195, 
             'Typography': 196, 'Presentations': 117, 'Web Hosting': 11, 'Game Consoles': 81, 'UNIX': 65, 'Game Design': 59, 'Windows Server': 130, 
             'OSCommerce': 114, 'Computer Security': 111, 'Assembly': 123, 'Social Networking': 19, 'Microsoft': 69, 'CSS': 12, 
             'Advertisement Design': 94, 'Big Data': 148, 'Post-Production': 158, 'Chrome OS': 105, 'Caricature &amp; Cartoons': 90, 'Software Testing': 6, 
             'Cocoa': 73, 'Virtuemart': 155, 'Invitation Design': 134, 'Android Honeycomb': 169, 'Google Earth': 173, 'Amazon Web Services': 21, 
             'Blackberry': 99, 'Codeigniter': 149, 'Voice Talent': 87, 'Sharepoint': 162, 'Prestashop': 83, 'Wordpress': 13, 'jQuery / Prototype': 37, 
             'Usability Testing': 85, 'Web Security': 92, 'After Effects': 75, 'UML Design': 164, 'ASP': 48, 'Building Architecture': 121, 
             'Amazon Kindle': 132, 'Arts &amp; Crafts': 57, 'Illustration': 51, 'Concept Design': 139, 'Logo Design': 17, 'JSP': 138, 
             'Cold Fusion': 186, 'SEO': 7, 'Dynamics': 187, 'WPF': 168, 'Ruby &amp; Ruby on Rails': 84, 'VoIP': 76, 'XML': 38, 'Photoshop': 18, 
             'Website Management': 9, 'Windows Mobile': 180, 'Graphic Design': 2, 'Metatrader': 152, 'Link Building': 15, 'DNS': 172, 'Oracle': 120, 
             'Photoshop Design': 79, 'NoSQL Couch &amp; Mongo': 191, 'Motion Graphics': 136, 'Zen Cart': 131, 'Blog Design': 60, 'Windows API': 167, 
             'Audio Services': 80, 'Twitter': 54, 'Objective C': 47, 'Fashion Modeling': 146, 'ActionScript': 78, 'Google Analytics': 124, 
             'Covers &amp; Packaging': 115, 'Photo Editing': 89, 'Windows Desktop': 23, '3D Animation': 49, 'Boonex Dolphin': 199, 'SugarCRM': 163, 
             '.NET': 26, 'Brochure Design': 86, 'Zend': 178, 'Animation': 43, 'Infographics': 184, 'WHMCS': 166, 'Templates': 50, 'Flex': 133, 
             'Maya': 135, '3D Modelling': 55, 'Python': 70, 'Software Architecture': 4, 'Shell Script': 44, 'Fashion Design': 145, 'C Programming': 24, 
             'eCommerce': 22, 'T-Shirts': 118, '3D Printing': 193, 'InDesign': 147, 'Asterisk PBX': 110, 'Flyer Design': 107, 'HTML5': 31, 
             'Mac OS': 68, 'x86/x64 Assembler': 192, '3D Rendering': 66, 'Website Testing': 10, 'Visual Arts': 64, 'VPS': 177, 'C# Programming': 30, 
             'PSD to HTML': 71, 'Joomla': 33, 'Linkedin': 151, 'Format &amp; Layout': 182, 'Visual Basic': 53, 'Linux': 34, 'Banner Design': 56, 
             'Volusion': 156}


def compute_pattern(job_list):
    bitVector = BitVector( size = 200 )
    ids = []
    for job in job_list:
        if(job in hash_jobs):
            id = hash_jobs[job]
            ids.append(id)
    for id in ids:
        bitVector[id] = 1
    return bitVector
        

def compute_patterns():
    file = open("all_projects.csv", "r")
    patterns = {}
    i = 0
    for line in file.readlines():
        i += 1
        try:
            parsed = line.split(',', 1)
            id = parsed[0]  # mi-am luat id-ul
            parsed = parsed[1:]
            parsed_string = " ".join(parsed)
            parsed = re.split('20[0-9]{2}-[0-9]{2}-[0-9]{2}', parsed_string)
            nume = parsed[0][1:-2]  # numele este primul element din lista, fara primul caracter (spatiu) si ultimele doua (virgula, spatiu)
            date = " ".join(re.findall('20[0-9]{2}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}', parsed_string))  # mi-am luat data si ora
            parsed = re.split('20[0-9]{2}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}', parsed_string)[1][2:]  # string
            bid_count = parsed.split(', ')[-2]  # mi-am luat bid_countul ca penultima chestie despartita de virgula din string
            avg_bid = parsed.split(', ')[-1][:-1]  # mi-am luat avg_bidul ca ultima chestie despartita de virgula din string
            jobs = " ".join(parsed.split(', ')[:-2])  # mi-am luat jobs-urile ca tot de la data pana la sfarsit, mai putin ultimele 2 chestii
            job_list = jobs.split(',')
            pattern = compute_pattern(job_list)
            # avg bid, max, count
            patterns.setdefault(pattern.intValue(), (0.0, 0.0, 0))
            if avg_bid == "False":
                avg_bid = -1
            if(avg_bid != -1):
                avg_bid = float(avg_bid)
                
                tup = patterns[pattern.intValue()]
                avg = tup[0] + avg_bid
                max = tup[1] 
                if max < avg_bid:
                    max = avg_bid
                count = tup[2] + 1
                patterns[pattern.intValue()] = (avg, max, count)
            
        except IndexError:
            print line
        if i % 100000 == 0:
            print i,
           
    patterns = patterns.items()
    patterns.sort(key = lambda tup:tup[1][1], reverse = True)
    fout = open("earnings_by_pattern.dict", "w")
    #print patterns
    for pattern in patterns:
        #pattern avg_bid max_bid
        fout.write("%s:%f:%f,\n"%(pattern[0], pattern[1][0]/pattern[1][2], pattern[1][1]))
    fout.close()


#compute_patterns()  
foa = Foa()
details = foa.loadProjectDetailsFromCSV(filename="full_projects_details.csv")
patterns = {}
projects = foa.loadProjectsFromCSVFile("spring_2012_599.csv")

my = 0
size = len(details)
for detail in details.values():
    #print my,
    #print " of ",
    #print size
    my += 1
    prj_id = str(detail.id)
#    print prj_id
    if prj_id in projects:

        job_list = detail.jobs.split(";")
       # print "Job_list: ",
       # print job_list
        job_list = [job.strip() for job in job_list]
        pattern = compute_pattern(job_list)
        patterns.setdefault(pattern.intValue(), (0.0, 0.0, 0.0))
        
        exch_rate =  float(detail.exchg)
        if(exch_rate == -1):
            continue
        print exch_rate    
          
        avg_bid = projects[prj_id].avg_bid[:-1]
      #  print avg_bid 
    
        if avg_bid == "False":
            avg_bid = -1
        if(avg_bid != -1):
            
            avg_bid = float(avg_bid) * exch_rate
            if(avg_bid == 26575):
                    print "PROJECT ID:",
                    print prj_id
            tup = patterns[pattern.intValue()]
            avg = tup[0] + avg_bid
            max = tup[1] 
            if max < avg_bid:
                max = avg_bid
            count = tup[2] + 1.0
            patterns[pattern.intValue()] = (avg, max, count)
        #if(my == 000):
        #    break
patterns = patterns.items()
patterns.sort(key = lambda tup:tup[1][1], reverse = True)
fout = open("earnings_by_pattern.dict", "w")
#print patterns
for pattern in patterns:
    #pattern avg_bid max_bid
    if pattern[1][2] != 0.0:
        fout.write("%s:%f:%f,\n"%(pattern[0], pattern[1][0]/pattern[1][2], pattern[1][1]))
fout.close()
