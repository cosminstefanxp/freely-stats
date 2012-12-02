'''
Created on Dec 1, 2012

@author: cosmin
'''

from foa import Foa

# Load data 
foa = Foa();
users = foa.load_users_from_csv("../data/users.csv");
projects = foa.loadProjectDetailsFromCSV("../data/projects_details.csv")

# Processing the projects
print "Building nationalities interactions map..."
countries = {}
count = 0
no_accepted = 0
failed = 0
for p in projects.values():
    # Printing
    count += 1
    if count % 2500 == 0:
        print "Processed", count, "projects out of", len(projects.values())
        
    # Get the countries of accepted bidders for this buyer_country
    accepted = countries.get(p.buyer_country)
    if accepted == None:
        accepted = [0, {}]
        countries[p.buyer_country] = accepted

    if p.accepted_bidder_id == -1:
        no_accepted += 1
        continue;
    
    # Get the accepted bidder
    try:
        accepted_bidder = users[p.accepted_bidder_id]
    except KeyError:
        failed += 1
        continue

    # Set the new count value for accepted_bidder
    accepted[1].setdefault(accepted_bidder.country, 0)
    accepted[1][accepted_bidder.country] = accepted[1][accepted_bidder.country] + 1
    accepted[0] = accepted[0] + 1
    
# Sort buyers countries    
print "Unable to find user for", failed, "projects. No accepted bidder for ", no_accepted, "projects"
countries = countries.items()
countries.sort(key=lambda x: x[1][0], reverse=True)

# Sort accepted bidders' countries and write to output file
fout = open("../../data/accepted_bidders_nationalities.csv", "w")
fout.write("country,bids_count,accepted\n");
for country in countries[:20]:
    accepted = country[1][1].items()
    accepted.sort(key=lambda x: x[1], reverse=True)
    print country[0].strip(), "[%d]: " % country[1][0], accepted
    fout.write("%s,%d," % (country[0].strip(), country[1][0]))
    for a in accepted[:6]:
        fout.write("%s:%d;" % (a[0], a[1]))
    fout.write("\n")
fout.close()
        



