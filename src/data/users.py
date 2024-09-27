
print("country?")
country = input()
total_ip = 0
final = open("data/generated/"+country+"_final.txt", "w") 

try:
	with open("data/users.txt", "r") as f:
		for line in f:
				var = line.split()
				if (var[0] in country):
					total_users_of_country = int(line.split()[1])
					print(total_users_of_country)
					break
except:
	pass
f.close()
try:
	with open("data/"+country+"_asn.txt", "r") as f:
		for line in f:
			line_after_split = line.split("\t")
			length = len(line_after_split)
			total_ip += int(line_after_split[length-1])
except:
	pass
f.close()

total_ip_of_country = total_ip

try:
	with open("data/"+country+"_asn.txt", "r") as f:
		for line in f:
		    as_split = line.split("\t")
		    length = len(as_split)
		    percent = (int(as_split[length-1])/total_ip_of_country)*(total_users_of_country)
		    final.write(as_split[0] + " "+str(percent) +"\n")
except:
	pass
		    
final.close()
    

