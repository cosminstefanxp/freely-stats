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