import job
import json
import re
import project
import bids
import user
from project import Project
from project_details import ProjectDetails

class Foa:
    def __init__(self):
        self.jobs = {}
        self.projects = {}
        self.users = {}
        self.bids = {}
    
    def loadJobsFromFile(self, file_name = "jobs.json"):
        file = open(file_name, "r")
        #id nume nr_proiecte
        jobs = json.load(file)
        for giob in jobs:
            self.jobs[giob['id']] =  job.Job(giob['id'], giob['name'], giob['projects_count'], giob['seo_url'])
        return jobs
                     
    def writeJobsToFile(self, jobs, file_name = "jobs.json", type="json"):
        
        self.jobs = jobs
        file = open(file_name, "w")
        if(type == "json"):
            file.write(json.dumps([x.to_dict() for x in jobs], indent = 4))
        else:
            for job in self.jobs:
                file.write("%s, %s, %d, %s\n"%(job.id, job.name, job.projects_count, job.seo_url))
        file.close()
        
    def loadProjectsFromFile(self, file_name = "projects.json"):
        file = open(file_name, "r")
        #id nume nr_proiecte
        raw_projects = json.load(file)
        projects = {}
        for project in raw_projects:
            projects[project['id']] =  project.Project(project['id'], project['name'], project['start_date'], project['jobs'], project['bid_count'], project['avg_bid'])
        return projects
	
    def loadProjectsFromCSVFile(self, file_name):
        file = open(file_name, "r")
        #id, nume*, start_date, jobs*, bid_count, avg_bid
        projects = {}
        lines = file.readlines()
        i = 0
        nr = len(lines)
        for line in lines:
            i += 1
            try:
                parsed = line.split(',',1)
                id = parsed[0]	#mi-am luat id-ul
                parsed = parsed[1:]
                parsed_string = " ".join(parsed)
                parsed = re.split('20[0-9]{2}-[0-9]{2}-[0-9]{2}', parsed_string)
                nume = parsed[0][1:-2]	#numele este primul element din lista, fara primul caracter (spatiu) si ultimele doua (virgula, spatiu)
                date = " ".join(re.findall('20[0-9]{2}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}', parsed_string))	#mi-am luat data si ora
                parsed = re.split('20[0-9]{2}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}', parsed_string)[1][2:]	#string
                bid_count = parsed.split(', ')[-2]	#mi-am luat bid_countul ca penultima chestie despartita de virgula din string
                avg_bid = parsed.split(', ')[-1]	#mi-am luat avg_bidul ca penultima chestie despartita de virgula din string
                jobs = " ".join(parsed.split(', ')[:-2])	#mi-am luat jobs-urile ca tot de la data pana la sfarsit, mai putin ultimele 2 chestii
                projects[id] = project.Project(id, nume, date, jobs, bid_count, avg_bid)
            except IndexError:
                print line
            if i % 100000 == 0:
                print i,
                print "out of",
                print nr
        return projects
    
    def appendProjectsDetailsToCSVFile(self, projects_details, file_name = "projects_details.csv"):
        file = open(file_name, "a")
        
        for project in projects_details.values():
            if project.name:
                name = project.name.replace(","," ")
                name = name.replace("\n", " ")
                name = name.encode('ascii', 'ignore')
            else:
                name = project.name
            if project.short_descr:
                description = "".join(project.short_descr.splitlines())
                description = "".join(description.split(","))
                description = description.encode('ascii', 'ignore')
            else:
                description = project.short_descr
            if project.buyer_name:
                buyer_name = project.buyer_name.replace(",", " ").encode('ascii', 'ignore')
            else:
                project.buyer_name
                
            if project.buyer_country :
                buyer_country = project.buyer_country.replace(",", " ").encode('ascii', 'ignore')
            else:
                buyer_country = project.buyer_country
                
            jobs = ";".join(project.jobs).encode('ascii', 'ignore')
            
            if project.accepted_bidder_username:
                accepted_bidder_username = project.accepted_bidder_username.replace(",", " ").encode('ascii', 'ignore')
            else:
                accepted_bidder_username = project.accepted_bidder_username
           # print description
           
           
            #id, name, buyer_id, buyer_name, buyer_country, state, short_descr, jobs, accepted_bidder_id, accepted_bidder_username)
            file.write("%d, %s, %d, %s, %s, %s, %s, %s, %d, %s\n"%(project.id, name, project.buyer_id, buyer_name, buyer_country, project.state, description, jobs, project.accepted_bidder_id, accepted_bidder_username))
        file.close();  
    
    
    
    def appendProjectsToCSVFile(self, projects, file_name = "projects.csv"):
        file = open(file_name, "a")
        for project in projects.values():
            file.write("%s, %s, %s, %s, %s, %s\n"%(project.id, project.name.encode('utf-8'), project.start_date.encode('utf-8'), project.jobs.encode('utf-8'), project.bid_count, project.avg_bid))
        file.close();   
        
    def appendBidsToCSVFile(self, projects_bids, file_name ="projects_bids.csv"): 
        file = open(file_name, "a")
        for project_id in projects_bids:
            bids = projects_bids[project_id]
            for bid in bids.values():
                # provider_userid, provider, bid_amount, descr, rating):
                if bid.descr:
                    description = "".join(bid.descr.splitlines())
                    description = "".join(description.split(","))
                    descr = description.encode('ascii', 'ignore')
             
                else:
                    descr = bid.descr
                if bid.provider:
                    provider = bid.provider.encode('ascii', 'ignore')
                else:
                    provider = bid.provider
                
                file.write("%s, %s, %s, %s, %s, %f\n"%(project_id, bid.provider_userid, provider, bid.bid_amount, descr, bid.rating))
        file.close()
         
    def appendUsersToCSVFile(self, users, file_name ="users.csv"): 
        file = open(file_name, "a")
        for user_id in users:
            user = users[user_id]
            username = user.username.encode('ascii', 'ignore')
            if user.country:
                country = user.country.encode('ascii', 'ignore')
            else:
                country = user.country
            if user.city:
                city = user.city.encode('ascii', 'ignore')
            else:
                city = user.city
            jobs = user.jobs.encode('ascii', 'ignore')
            
         
            rating = float(user.rating)

            currency = int(user.currency)
           
            #id, username, country, city, jobs, rating, currency):    
            file.write("%d, %s, %s, %s, %s, %f %d\n"%(int(user_id), username, country, city, jobs, rating, currency))
        file.close()
    def writeProjectsToFile(self, projects, file_name = "projects.json", type="json"):
        file = open(file_name, "w")
        if type == "json":
            file.write(json.dumps([x.to_dict() for x in projects.values()], indent = 4))
        else:
            for project in projects.values():
                file.write("%s, %s, %s, %s, %s, %s\n"%(project.id, project.name.encode('utf-8'), project.start_date, project.jobs, project.bid_count, project.avg_bid))

        file.close()
        
    def loadUsersFromFile(self, file_name = "users.json"):
        print "TODO: "
        
    def load_users_from_csv(self, filename):
        print "Loading users from:", filename
        file = open(filename, "r")
        #id, nume, tara, oras, lista_separata_cu_;_de_skilluri, rating currency
        users = {}
        lines = file.readlines()
        i = 0
        nr = len(lines)
        for line in lines:
            i += 1
            try:
                parsed = line.split(',',4)
                user_id = parsed[0].strip()	            #mi-am luat user_id-ul
                user_name = parsed[1].strip()	        #mi-am luat user_name-ul
                user_country = parsed[2].strip()        #mi-am luat user_country-ul
                user_city = parsed[3].strip()           #mi-am luat user_city-ul
                parsed = parsed[4:] 
                parsed_string = "".join(parsed)
                parsed = parsed_string.rsplit(',',1)
                last = parsed[-1].split(' ')
                rating = last[1]                #mi-am luat rating-ul
                currency = last[2]              #mi-am luat currency-ul
                parsed = parsed[:-1]
                skills = "".join(parsed).strip().split(';')   #skills-urile
                users[user_id] = user.User(user_id, user_name, user_country, user_city, skills, rating, currency)
            except IndexError:
                print line
            if i % 5000 == 0:
                print "Processed",i,"out of",nr
        print "Loaded users details."
        return users
    
    def loadProjectDetailsFromCSV(self, filename="project_details.csv"):
        print "Loading projects details from:", filename
        fin = open(filename, "r")
        projects = {}
        lines = fin.readlines()
        i = 0
        nr = len(lines)
        for line in lines:
            i += 1
            p = ProjectDetails.fromCSV(line)
            projects[p.id] = p
            if i % 5000 == 0:
                print "Processed", i, "out of", nr
        print "Loaded projects details."
        return projects
        
    def writeUsersToFile(self, users, file_name = "users.json"):
        self.users = users
        file = open(file_name, "w")
        file.write(json.dumps([x.to_dict() for x in users], indent = 4))
        file.close()
