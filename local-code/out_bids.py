'''
iau pentru fiecare tara, in ce tari sunt acceptati cei mai multi useri de-ai ei
imi scriu un fisier, cu o linie de ex: USA, [(Romania, 13), (Taiwan, 2), (Canada, 10)], numar_total_de_useri_din_sua. sa semene cu https://github.com/cosminstefanxp/freely-stats/blob/master/data/accepted_bidders_nationalities.csv

ma uit in project details, vad in ce tara e proiectul si din ce tara e ala care a fost acceptat
pot sa am un dictionar de tari_care_au_proiecte. ca valori, o sa am un dictionar , cu cheia: tara si valoarea: cati oameni din tara respectiva au fost acceptati.  ai trebuie sa calculez cumva si nr total de utilizatori din SUA care au aplicat (e suma valorilor din dict2)
'''
import foa as FileOA

foa = FileOA.Foa()

#project details
#id, name, buyer_id, buyer_name, buyer_country, state, short_descr, jobs, accepted_bidder_id, accepted_bidder_username)

users = foa.load_users_from_csv("data\users.csv")
projects = foa.loadProjectDetailsFromCSV("data\projects_details_uniq.csv")

countries = {}
count = 0
no_accepted = 0
failed = 0
for p in projects.values():
    # Printing
    count += 1
    if count % 2500 == 0:
        print "Processed", count, "projects out of", len(projects.values())
        
    if p.accepted_bidder_id == -1:
        no_accepted += 1
        continue;
        
    # Get the accepted bidder
    try:
        accepted_bidder = users[p.accepted_bidder_id]
    except KeyError:
        failed += 1
        continue

    # Get the buyer countries for this country
    c = countries.get(accepted_bidder.country)
    if c == None:
        c = [0, {}]
        countries[accepted_bidder.country] = c
        
    
    
    # Set the new count value for accepted_bidder
    c[1].setdefault(p.buyer_country, 0)
    c[1][p.buyer_country] = c[1][p.buyer_country] + 1
    c[0] = c[0] + 1
    
# Sort buyers countries    
print "Unable to find user for", failed, "projects. No accepted bidder for ", no_accepted, "projects"
countries = countries.items()
countries.sort(key=lambda x: x[1][0], reverse=True)

# Sort accepted bidders' countries and write to output file
fout = open("data\out_bidders_nationalities.csv", "w")
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