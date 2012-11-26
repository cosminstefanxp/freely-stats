import foa as FileOA
import json
import re
import project

months = ["2012-11", "2012-10", "2012-09", "2012-08", "2012-07", "2012-06", "2012-05", "2012-04", "2012-03", "2012-02", "2012-01", "2011-12", "2011-11", "2011-10", "2011-09", "2011-08", "2011-07", "2011-06", "2011-05", "2011-04", "2011-03", "2011-02", "2011-01", "2010-12", "2010-11", "2010-10", "2010-09", "2010-08", "2010-07", "2010-06", "2010-05", "2010-04", "2010-03", "2010-02", "2010-01", "2009-12", "2009-11", "2009-10", "2009-09", "2009-08", "2009-07", "2009-06", "2009-05", "2009-04", "2009-03", "2009-02", "2009-01", "2008-12", "2008-11", "2008-10", "2008-09", "2008-08", "2008-07", "2008-06", "2008-05", "2008-04", "2008-03", "2008-02", "2008-01"]
foa = FileOA.Foa()
top_100_jobs = foa.loadJobsFromFile("jobs_TOP100_in_main_categories.json")

trends = {}
for giob in top_100_jobs:
#    print giob["name"]
    trends[giob["name"]] = {}

#init trends dictionary for each month and each skill
for skill in trends.keys():
    for month in months:
        trends[skill][month] = 0    

#init total count dictionary  
total_dict = {}
for skill in trends.keys():
    for month in trends[skill]:
        total_dict[month] = 0

file = open("spring_2012_7599.csv", "r")
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
        proj = project.Project(id, nume, date, jobs, bid_count, avg_bid)
        
        # done reading. now let's process
        
        for skill in proj.job_list:
#        print skill
            if skill in trends.keys():
                trends[skill][proj.shrt_date] += 1
                
        total_dict[proj.shrt_date] += 1    
    except IndexError:
        print line
    if i % 50000 == 0:
        print i,
        print "out of",
        print nr

        

print "Done reading projects. Begin processing"

print "Done creating the trends dictionary. Starting to write to file"                

#trends["total"] = total_dict
    
# import operator
# sorted_trends = sorted(trends.iteritems(), key=operator.itemgetter(1))
               
# for skill in trends.keys():
    # print skill
    # print trends[skill]

# for trend in sorted_trends:
    # print trend[0],
    # print " ",
    # print trend[1]

file = open("trends2.csv", "w")

luni = ",".join(reversed(months))
row = "skill," + luni

file.write(row + "\n")
row = "total,"
for month in sorted(total_dict.iterkeys()):
    # print "%s: %s" % (key, trends["total"][key])
    row = row + str(total_dict[month]) + ","
    
file.write(row + "\n")

for skill in trends.keys():
    row = skill
    for month in sorted(trends[skill].iterkeys()):
        row = row + "," + str(trends[skill][month])
    file.write(row + "\n")

file.close()