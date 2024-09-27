from scipy.stats import entropy
from math import log

#Select a region by uncommenting the country list (or add your own (refer to users.txt))

#africa
country_list=["south_africa", "nigeria", "tanzania", "kenya", "congo", "egypt", "uganda", "algeria", "sudan", "morocco", "angola", "mozambique", "madagascar", "ghana", "cameroon", "niger", "mali", "malawi", "zambia", "senegal", "chad", "somalia", "zimbabwe", "guinea", "rwanda", "benin", "tunisia", "togo", "botswana", "seychelles"]

#africa + europe
#country_list=["south_africa", "nigeria", "tanzania", "kenya", "congo", "egypt", "uganda", "algeria", "sudan", "morocco", "angola", "mozambique", "madagascar", "ghana", "cameroon", "niger", "mali", "malawi", "zambia", "senegal", "chad", "somalia", "zimbabwe", "guinea", "rwanda", "benin", "tunisia", "togo", "botswana", "seychelles", "cyprus", "georgia", "kazakhstan", "turkey", "azerbaijan", "ukraine", "russia", "germany", "uk", "france", "italy", "spain", "ukraine", "poland", "romania", "netherlands", "belgium", "czech", "greece", "portugal", "sweden", "hungary", "belarus", "austria", "serbia", "switzerland", "bulgaria", "denmark", "finland", "slovakia", "norway", "ireland", "croatia", "moldova", "bosnia", "albania", "lithuania", "macedonia", "slovenia", "latvia", "estonia", "montegenero", "luxembourg", "malta", "iceland", "andorra", "monaco", "liechtenstein"]

#western europe
#country_list= ["germany", "austria", "belgium", "france", "liechtenstein", "luxembourg", "monaco", "netherlands", "switzerland"]

#central and eastern europe
#country_list= ["estonia", "germany", "latvia", "lithuania", "poland", "czech", "slovakia", "hungary", "romania", "bulgaria", "slovenia", "croatia", "albania", "montegenero", "serbia", "macedonia", "bosnia"]

#eurasia
#country_list= ["uae", "hkg", "cyprus", "georgia", "kazakhstan", "turkey", "azerbaijan", "ukraine", "russia", "germany", "uk", "france", "italy", "spain", "ukraine", "poland", "romania", "netherlands", "belgium", "czech", "greece", "portugal", "sweden", "hungary", "belarus", "austria", "serbia", "switzerland", "bulgaria", "denmark", "finland", "slovakia", "norway", "ireland", "croatia", "moldova", "bosnia", "albania", "lithuania", "macedonia", "slovenia", "latvia", "estonia", "montegenero", "luxembourg", "malta", "iceland", "andorra", "monaco", "liechtenstein", "china", "india", "russia", "indonesia", "pakistan", "bangladesh", "japan", "philippines", "vietnam", "thailand", "burma", "south_korea", "malaysia", "nepal", "korea", "taiwan", "sri_lanka", "cambodia", "papua", "laos", "singapore", "mongolia", "bhutan", "maldives"]

#europe
#country_list= ["cyprus", "georgia", "kazakhstan", "turkey", "azerbaijan", "ukraine", "russia", "germany", "us", "france", "italy", "spain", "ukraine", "poland", "romania", "netherlands", "belgium", "czech", "greece", "portugal", "sweden", "hungary", "belarus", "austria", "serbia", "switzerland", "bulgaria", "denmark", "finland", "slovakia", "norway", "ireland", "croatia", "moldova", "bosnia", "albania", "lithuania", "macedonia", "slovenia", "latvia", "estonia", "montegenero", "luxembourg", "malta", "iceland", "andorra", "monaco", "liechtenstein"]

#apac + uae
#country_list= ["uae", "hkg", "china", "india", "australia", "new_zealand", "russia", "indonesia", "pakistan", "bangladesh", "japan", "philippines", "vietnam", "thailand", "burma", "south_korea", "malaysia", "nepal", "korea", "taiwan", "sri_lanka", "cambodia", "papua", "laos", "singapore", "mongolia", "bhutan", "maldives"]

#americas
#country_list= ["belize", "us", "canada", "virgin", "costa", "dominican", "el_salvador", "venezuela", "guatemala", "honduras", "mexico", "panama", "puerto_rico", "colombia","brazil", "argentina", "bolivia", "chile", "ecuador", "paraguay", "peru", "uruguay"]

#americas + western europe
#country_list= ["belize", "us", "canada", "virgin", "costa", "dominican", "el_salvador", "venezuela", "guatemala", "honduras", "mexico", "panama", "puerto_rico", "colombia","brazil", "argentina", "bolivia", "chile", "ecuador", "paraguay", "peru", "uruguay", "germany", "austria", "belgium", "france", "liechtenstein", "luxembourg", "monaco", "netherlands", "switzerland"]

total_users = 0
ent=0

# Calculating total users in the country list
with open("Tor data/users.txt", "r") as f:
	for line in f:
		if(line.split()[0].casefold() in country_list):
			total_users += int(line.split()[1])

			# # Uncomment to print countries found in your list
			# print("Found: "+ str(line.split()[0]))

print("====================================================")
print("Users: " + str(total_users))
f.close()

entropy_list = []

"""
# Confirm Tor User count
total_users_confirm = 0
for c in country_list:
	with open("ASN data/generated/"+c+"_final.txt", "r") as f: 
		for line in f:            
			total_users_confirm += float(line.split()[1])
f.close()
print("total users recheck: " + str(total_users_confirm))
"""


# Calculating entropy
for c in country_list:
	with open("ASN data/generated/"+c+"_final.txt", "r") as f: 
		for line in f:
		    var = float(line.split()[1])
		    if((var/total_users) > 0):
			    entropy_list.append((float(var/total_users)))
f.close()

# Calculating normalized entropy
for n_entropy in entropy_list:
	try:
		ent -= (n_entropy * log(n_entropy, 2))/log(len(entropy_list), 2)
	except:
		pass

# print("Entropy:" + str(entropy(entropy_list, base=2)))

print("Normalized ASN Entropy:" +str(ent))




