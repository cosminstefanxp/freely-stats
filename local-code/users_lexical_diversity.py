#projects_bids_uniq.csv: project_id, user_id, user_name, bid_amount, message, rating
#users_uniq.csv: id, nume, tara, oras, lista_separata_cu_;_de_skilluri, rating, currency
'''
citesc projects_bids_uniq linie cu linie. pentru fiecare userid caut in users_uniq.csv sa vad din ce tara e. pe urma adaug intr-un dictionar, unde cheia e tara si valoarea e un string format din mesajele de aplicare la un proiect ale userilor din tara respective. DE VAZUT CUM OPTIMIZEZ
'''

#initial  ::::    tari: {"tara": [numar_bidderi, [lista,de,mesaje,de,aplicare]]}
#final    ::::    tari: {"tara": [numar_bidderi, [(cel_mai_des_cuvant, numar_aparitii), (al_doilea, nr_aparitii_2),... ]], lexical_diversity_of_country, average_rating_of_users_in_country}
from __future__ import division
import foa as FileOA
import re
import nltk
from nltk.corpus import stopwords


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
            parsed_string = "".join(parsed).strip()
            parsed = parsed_string.rsplit(',',1)
            rating = parsed[-1].strip()         #mi-am luat rating-ul
            parsed = parsed[:-1]
            message = "".join(parsed).strip()   #mi-am luat message-ul
            #print message
            #to be continued
            user_country = get_user_country(user_id, big_user_structure)            
            if user_country in tari.keys():
                tari[user_country][0] += 1
            else:
                valoare = [1, []]
                #valoare[0] = 1
                #valoare[1] = []
                tari[user_country] = valoare
            tari[user_country][1].append(message)
            #print tari[user_country][1]
        except KeyError:
            #print "ERROR AT",
            #print line
            number_of_missing_users += 1
        if i % 10000 == 0:
            print i,
            print "out of",
            print nr
    return tari, number_of_missing_users
    
def print_bidders_per_country_to_file(tari):
    file = open("bidderi_pe_tari.csv", "w")
    
    for key, value in sorted(tari.iteritems(), key=lambda (k,v): (v[0],k), reverse=True):
        file.write("%s,%s\n" % (key, value[0]))

    file.close()

def print_tari_to_file(tari, country_average2):
    
    file = open("country_statistics.csv", "w")

    linie = "tara, numar_bidderi, tupluri_de_cele_mai_frecvente_cuvinte_si_frecventa_lor, numar_total_cuvinte, numar_cuvinte_unice, lexical_diversity, average_rating(poate fi 0 doar daca niciun user din tara respectiva nu are rating)\n"
    file.write(linie)
    #try:
    for key, value in sorted(tari.iteritems(), key=lambda (k,v): (v[0],k), reverse=True):
        file.write("%s,%s,[" % (key, value[0]))
        linie = ""
        for pereche in tari[key][1]:
            linie += "(" + pereche[0] + "," + str(pereche[1]) + "),"
        file.write(linie[:-1]+"]")
        file.write(","+str(tari[key][2]))
        file.write(","+str(tari[key][3]))
        file.write(","+str(tari[key][4]))
        # print country_average_2[key][1]
        # print country_average_2[key][0]
        if key in country_average2.keys():
            file.write(","+str(country_average2[key][1]/country_average2[key][0]))
        else:
            file.write(",0")
        file.write("\n")
    #except KeyError:
        #print "ERROR at key"
        #print key

#POT SA MAI FAC AVERAGE RATING PE TARA        
        
        
        
        
def analyze_texts(tari):
    for tara in tari.keys():
        text = " ".join(tari[tara][1])
        text2 = clean_one_text(text)
        fdist = nltk.FreqDist(text2.split(" "))
        fd = []
        for word in fdist.keys()[:50]:
            fd.append((word, fdist[word]))
        tari[tara][1] = fd
        tari[tara].append(len(text2.split()))
        tari[tara].append(len(set(text2.split())))
        tari[tara].append(lexical_diversity(text2.split(" ")))
    return tari

        
def clean_one_text(line):
    line = re.sub(r'http[^\s\n]*', '', line)
    line = re.sub(r'www[^\s\n]*', '', line)
    line = re.sub(r'[0-9]', '', line)
    line = line.replace(',', ' ')
    line = line.replace('.', ' ')
    line = line.replace('&amp;amp', ' ')
    line = line.replace('&amp', ' ')
    line = line.replace('&', ' ')
    line = line.replace('&quot', ' ')
    line = line.replace('quot', ' ')
    line = line.replace(';', ' ')
    line = line.replace('?', ' ')
    line = line.replace('!', ' ')
    line = line.replace(':', ' ')
    line = line.replace('(', ' ')
    line = line.replace(')', ' ')
    line = line.replace('#', ' ')
    line = line.replace('@', ' ')
    line = line.replace('-', ' ')
    line = line.replace('$', ' ')
    line = line.replace('=', ' ')
    line = line.replace('%', ' ')
    line = line.replace('\'', ' ')
    line = line.replace('\"', ' ')
    line = line.replace('\'s', ' ')
    line = line.replace(' gt ', ' ')
    line = line.replace(' lt ', ' ')
    line = line.replace('w/', ' ')
    line = line.replace(' via ', ' ')
    line = line.replace(' re ', ' ')
    line = line.replace(' rt ', ' ')
    line = line.replace(' RT ', ' ')
    
    #replace multiple whitespace with only one
    line = ' '.join(line.split())
    #remove stopwords
    words = line.split()
    stopwords = nltk.corpus.stopwords.words('english')
    line = ' '.join([w for w in words if w.lower() not in stopwords])
    
    return line.lower()
    
def lexical_diversity(text):
    if len(set(text)) != 0:
        return len(text)/len(set(text))
    return 0

def compute_average_rating(users):
    ca = {}
    for key in users.keys():
        usr = users[key]
        country = usr.country
        if country in ca.keys():
            if float(usr.rating) > 0.0:
                ca[country][0] += 1
                ca[country][1] += float(usr.rating)
        else:
            if float(usr.rating) > 0.0:
                ca[country] = [1, float(usr.rating)]
    return ca
        

    
users = foa.load_users_from_csv("data\users.csv")
tari, number_of_missing_users = read_bids_from_csv("data\projects_bids_uniq.csv", users)
tari = analyze_texts(tari)
country_average = compute_average_rating(users)
print_tari_to_file(tari, country_average)
