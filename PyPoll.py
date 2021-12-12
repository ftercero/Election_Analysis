#Write path to the file
#Resources/election_results.csv

#Read, process, and parse(analyze) data

#Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
#Print the present time.
print("The time right now is", now)

#Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    #Print the header row.
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
#election_data=(file_to_load, 'r')
    #To do: perform analysis.
    #print(election_data)

#Close the file.
#election_data.close()
#Ensure file is closed, otherwise data may be lost


#Using the with satement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

#Use the open statement to open the file as a text file.
#outfile = open(file_to_save,"w")
#Write some data to the file.
#outfile.write("Hello World")
    #txt_file.write("Counties in the election\n---------------\nArapahoe\nDenver\nJefferson")
#Close the file
#outfile.close()