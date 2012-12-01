#projects_bids_uniq.csv: project_id, user_id, user_name, bid_amount, message, rating
#users_uniq.csv: id, nume, tara, oras, lista_separata_cu_;_de_skilluri, rating, currency
'''
citesc projects_bids_uniq linie cu linie. pentru fiecare userid caut in users_uniq.csv sa vad din ce tara e. pe urma adaug intr-un dictionar, unde cheia e tara si valoarea e un string format din mesajele de aplicare la un proiect ale userilor din tara respective. DE VAZUT CUM OPTIMIZEZ
'''

def load_users_from_csv(filename):
    file = open(file_name, "r")
    #id, nume, tara, oras, lista_separata_cu_;_de_skilluri, rating currency
    useri = {}
    lines = file.readlines()
    i = 0
    nr = len(lines)
    for line in lines:
        i += 1
        try:
            parsed = line.split(',',4)
            user_id = parsed[0]	            #mi-am luat user_id-ul
            user_name = parsed[1]	        #mi-am luat user_name-ul
            user_country = parsed[2]        #mi-am luat user_country-ul
            user_city = parsed[3]           #mi-am luat user_city-ul
            parsed = parsed[4:] 
            parsed_string = "".join(parsed)
            parsed = parsed_string.rsplit(',',1)
            last = parsed[-1].split(' ')
            rating = last[1]                #mi-am luat rating-ul
            currency = last[2]              #mi-am luat currency-ul
            parsed = parsed[:-1]
            skills = "".join(parsed).strip()   #skills-urile
            
            #to be continued
            projects[id] = project.Project(id, nume, date, jobs, bid_count, avg_bid)
        except IndexError:
            print line
        if i % 10000 == 0:
            print i,
            print "out of",
            print nr
    return projects
    
def get_user_city_and_country(user_id, big_use_structure):
    return big_user_structure[user_id][3], big_user_structure[user_id][2]


def read_bids_from_csv(filename):
    file = open(file_name, "r")
    #project_id, user_id, user_name, bid_amount, message, rating
    tari = {}
    lines = file.readlines()
    i = 0
    nr = len(lines)
    for line in lines:
        i += 1
        try:
            parsed = line.split(',',4)
            project_id = parsed[0]	    #mi-am luat project_id-ul
            user_id = parsed[1]	        #mi-am luat user_id-ul
            user_name = parsed[2]       #mi-am luat user_name-ul
            bid_amount = parsed[3]      #mi-am luat bid_amount-ul
            parsed = parsed[4:] 
            parsed_string = "".join(parsed)
            parsed = parsed_string.rsplit(',',1)
            rating = parsed[-1]      #mi-am luat rating-ul
            parsed = parsed[:-1]
            message = "".join(parsed)   #mi-am luat message-ul
            #to be continued
            projects[id] = project.Project(id, nume, date, jobs, bid_count, avg_bid)
        except IndexError:
            print line
        if i % 10000 == 0:
            print i,
            print "out of",
            print nr
    return projects
