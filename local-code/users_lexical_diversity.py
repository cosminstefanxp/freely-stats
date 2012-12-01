#projects_bids_uniq.csv: project_id, user_id, user_name, bid_amount, message, rating
#users_uniq.csv: id, nume, tara, oras, lista_separata_cu_;_de_skilluri, rating, currency
'''
citesc projects_bids_uniq linie cu linie. pentru fiecare userid caut in users_uniq.csv sa vad din ce tara e. pe urma adaug intr-un dictionar, unde cheia e tara si valoarea e un string format din mesajele de aplicare la un proiect ale userilor din tara respective. DE VAZUT CUM OPTIMIZEZ
'''

import foa as FileOA

foa = FileOA.Foa()


def get_user_city(user_id, big_user_structure):
    return big_user_structure[user_id].city

def get_user_country(user_id, big_user_structure):
    return big_user_structure[user_id].country

def read_bids_from_csv(filename, big_user_structure):
    file = open(filename, "r")
    #project_id, user_id, user_name, bid_amount, message, rating
    tari = {}
    lines = file.readlines()
    i = 0
    nr = len(lines)
    number_of_missing_users = 0
    for line in lines:
        i += 1
        try:
            parsed = line.split(',',4)
            project_id = parsed[0].strip()	    #mi-am luat project_id-ul
            user_id = parsed[1].strip()	        #mi-am luat user_id-ul
            user_name = parsed[2].strip()       #mi-am luat user_name-ul
            bid_amount = parsed[3].strip()      #mi-am luat bid_amount-ul
            parsed = parsed[4:] 
            parsed_string = "".join(parsed)
            parsed = parsed_string.rsplit(',',1)
            rating = parsed[-1].strip()         #mi-am luat rating-ul
            parsed = parsed[:-1]
            message = "".join(parsed).strip()   #mi-am luat message-ul
            #to be continued
            user_country = get_user_country(user_id, big_user_structure)            
            if user_country in tari.keys():
                tari[user_country][0] += 1
            else:
                valoare = [1, []]
                #valoare[0] = 1
                #valoare[1] = []
                tari[user_country] = valoare
            tari[user_country][1] += message
        except KeyError:
            #print "ERROR AT",
            #print line
            number_of_missing_users += 1
        if i % 10000 == 0:
            print i,
            print "out of",
            print nr
    return tari, number_of_missing_users

users = foa.load_users_from_csv("data\users_uniq.csv")
#print users["1193992"]
tari, number_of_missing_users = read_bids_from_csv("data\projects_bids_uniq.csv", users)
print tari["Norway"]
#print tari[tari.keys()[0]]
print number_of_missing_users
#print tari.keys()