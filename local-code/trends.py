import foa as FileOA

def createMonthsList():
    months = ["2012-11", "2012-10", "2012-09", "2012-08", "2012-07", "2012-06", "2012-05", "2012-04", "2012-03", "2012-02", "2012-01", "2011-12", "2011-11", "2011-10", "2011-09", "2011-08", "2011-07", "2011-06", "2011-05", "2011-04", "2011-03", "2011-02", "2011-01", "2010-12", "2010-11", "2010-10", "2010-09", "2010-08", "2010-07", "2010-06", "2010-05", "2010-04", "2010-03", "2010-02", "2010-01", "2009-12", "2009-11", "2009-10", "2009-09", "2009-08", "2009-07", "2009-06", "2009-05", "2009-04", "2009-03", "2009-02", "2009-01"]
    return months


foa = FileOA.Foa()
top_100_jobs = foa.loadJobsFromFile("jobs_TOP100_in_main_categories.json")
trends = {}
for giob in top_100_jobs:
#    print giob["name"]
    trends[giob["name"]] = {}

prj = foa.loadProjectsFromCSVFile(file_name="spring_2012_199.csv")
for elem in prj.values():
#    print elem.name
#    print elem.job_list
    for skill in elem.job_list:
#        print skill
        if skill in trends.keys():
            if elem.shrt_date in trends[skill]:
                trends[skill][elem.shrt_date] += 1
            else:
                trends[skill][elem.shrt_date] = 1

                

total_dict = {}
for skill in trends.keys():
    for month in trends[skill]:
        total_dict[month] = 0
for skill in trends.keys():
    for month in trends[skill]:
        # print month
        # print trends[skill][month]
        total_dict[month] += trends[skill][month]

# trends["total"] = total_dict
    
# import operator
# sorted_trends = sorted(trends.iteritems(), key=operator.itemgetter(1))
               
# for skill in trends.keys():
    # print skill
    # print trends[skill]

# for trend in sorted_trends:
    # print trend[0],
    # print " ",
    # print trend[1]


