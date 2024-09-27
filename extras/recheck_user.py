
country_list=[]
counter=0
with open("data/users.txt", "r") as f:
	for line in f:
		counter = counter + 1
		country_list.append(line.split()[0])
		if(counter==203):
				break
counter=0
total_users = 0
with open("data/users.txt", "r") as f:
	for line in f:
		counter = counter + 1
		#print(line.split()[0])
		total_users += int(line.split()[1])
		if(counter==203):
				break
print("TOTAL TOR USERS IN THE COUNTRY LIST: " + str(total_users))
total_users = 0
		
	

print(len(country_list))
total_users_confirm = 0
for c in country_list:
	#print(c)
	with open("data/generated/"+c+"_final.txt", "r") as f: 
		for line in f:            
			total_users_confirm += float(line.split()[1])
print("total users recheck: " + str(total_users_confirm))
total_users_confirm = 0


f.close()

