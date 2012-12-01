import json
file = open ("jobs_TOP100_in_main_categories.json", "r")
jobs_all = json.load(file)
file.close()

top_jobs = [job["name"] for job in jobs_all]
links = {}
for job in top_jobs:
    links[job] = {}

job_links = {}
for job in top_jobs:
    job_links[job] = []
    
file = open("projects_details_uniq.csv", "r")
for line in file.readlines():
    details = line.split(",")
    id = details[0]
    jobs = {}
    if details[7]:
        jobs = details[7].split(";")
    else:
         continue
    for job in jobs:
        if(job in top_jobs):
            for linked_job in jobs:
                if(job != linked_job):
                    links[job].setdefault(linked_job, 0.0)
                    links[job][linked_job] +=1
file.close()

for job in top_jobs:
    count = float(sum(links[job].values()))
    for link in links[job]:
        if links[job][link] / count > 0.01:
            job_links[job].append(link)

fout = open("job_links.json", "w")
fout.write(json.dumps(job_links, indent=4))
fout.close()
            