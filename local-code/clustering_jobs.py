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
    
def kmeans(x):
    jobnames,projects,data=clusters.readfile('job_projects')
    cl, matches = clusters.kcluster(data, k=x)
    #print cl
    matches_with_names = []
    for i in range(x):
         matches_with_names.append([jobnames[r] for r in matches[i]])
    return matches_with_names

def multidim():
    jobnames,projects,data=clusters.readfile('job_projects')
    coords = clusters.scaledown(data)
    clusters.draw2d(coords,jobnames,jpeg='job_multidim.jpg')



fout = open("k-means(10-16)", "w")
for x in [10, 11, 12, 13, 14, 15, 16]:      
    print "X = ",
    print x  
    k_clusters = kmeans(x)
    fout.write("%d,"%(x))
    for cluster in k_clusters:
        fout.write(";")
        jobs  = ""
        for job in cluster:
            job = job.replace("&amp", "&")
            jobs += job+"~"
        fout.write(jobs[:-1])
    fout.write("\n")
fout.close()
