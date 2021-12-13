#print ("Hello World")
#counties=["Arapahoes","Denver","Jefferson"]
#if counties[1]=='Denver':
 #   print(counties[1])

#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
 #   print("El Paso is in the list of counties.")
#else:
 #   print("El Paso is not the list of counties.")

#if "Arapahoe" in counties and "El Paso" in counties:
 #   print("Arapahoe and El Paso are in the list of counties.")
#else:
 #   print("Arapahoe or El Paso is not in the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
 #   print("Arapahoe or El Paso is in the list of counties.")
#else:
 #   print("Arapahoe and El Paso are not in the list of counties.")

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties:
 #   print(county)

#for county in counties_dict.keys():
 #   print(county)

#for voters in counties_dict.values():
 #   print(voters)

#for county in counties_dict:
 #   print(counties_dict[county])

#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#prints as a continuous list
#print(voting_data)

#prints as a stack. prints 1 under the other
#for county_dict in voting_data:
    #print(county_dict)

#3.2.10 says this will iterarte and print the counties.
#I understand the for loop but dont understand the print line.
#how does the module expect us to know this if we didn't cover it.
#['county'] is throwing me off
#for i in range(len(voting_data)):
    #print(voting_data[i]['county'])

#for i in range(len(voting_data)):
    #print(voting_data[i]['registered_voters'])

#why doesnt this work with registered_voters_dict. neither_dict are defined
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

#candidate_votes = int (input("How many votes did the candidate get in the election?"))
#total_votes = int(input("What is the total number of votes in the election?"))
#message_to_candidate = (
    #f"You received {candidate_votes:,} number of votes. "
    #f"The total number of votes in the election was {total_votes:,}. "
    #f"You received {candidate_votes / total_votes * 100:.2f}% of the votes")
#print(message_to_candidate)

#f'{value:{width},.{precision}}'
#width=number of characters
#precision=.#'sf where # is the decimal places

#skill drill
#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters:,} registered voters.")
#skill drill--need help solving
#for county_dict in voting_data:
     #print(f"{county} county has {voters} registered voters.")
for county, voters in voting_data:
    print (f"{'county'} county has {'voters'} registered voters")
