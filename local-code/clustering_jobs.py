import json
import clusters
def generate_projects_for_jobs():
    #citeste joburile => dict cu ele
    file = open ("jobs_TOP100_in_main_categories.json", "r")
    jobs_all = json.load(file)
    file.close()
    
    #initializing job-projects dictionary
    top_jobs = [job["name"] for job in jobs_all]
    jobs_projects = {}
    for job in top_jobs:
        jobs_projects[job] = {}
    header ={}
       
       
    #citeste rand cu rand proj details, ia joburile lui si pune 1 pe linia jobului si coloana proiectului
    file = open("projects_details_uniq.csv", "r")
    count = 0
    for line in file.readlines():
        details = line.split(",")
        id = details[0]
        header[count] = id +""
        jobs = {}
        if details[7]:
            jobs = details[7].split(";")
        else:
            continue
        for job in jobs_projects:
            if(job in jobs):
                jobs_projects[job][count] = "1"
            else:
                jobs_projects[job][count] = "0"
        count+=1
        print count
    file.close()
    
    
    fout = open("job_projects", "w")
    fout.write("Projects\t%s\n"%("\t".join(header.values())))
    for job in jobs_projects:
        fout.write("%s\t%s\n"%(job, "\t".join(jobs_projects[job].values())))
    fout.close()          
            
#generate_projects_for_jobs()

def draw_dendogram():
    jobnames,projects,data=clusters.readfile('job_projects')
    clust=clusters.hcluster(data)
    #clusters.printclust(clust,labels=jobnames)
    clusters.drawdendrogram(clust,jobnames,jpeg='jobclust.jpg')
    
def kmeans():
    x = 2
    0
    jobnames,projects,data=clusters.readfile('job_projects')
    clust=clusters.kcluster(data, k=x)
    fout = open("kclust.json", "w")
    fout.write(json.dumps(clust, indent = 4))
    fout.close()
    for i in range(x):
        print [jobnames[r] for r in clust[i]]
        
kmeans()
