import job
import json
import re
import project

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
        for line in lines:
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
        return projects
    
    def appendProjectsToCSVFile(self, projects, file_name = "projects.csv"):
        file = open(file_name, "a")
        for project in projects.values():
            file.write("%s, %s, %s, %s, %s, %s\n"%(project.id, project.name.encode('utf-8'), project.start_date.encode('utf-8'), project.jobs.encode('utf-8'), project.bid_count, project.avg_bid))
        file.close();    
    
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
    
    def writeUsersToFile(self, users, file_name = "users.json"):
        self.users = users
        file = open(file_name, "w")
        file.write(json.dumps([x.to_dict() for x in users], indent = 4))
        file.close()
