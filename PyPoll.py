#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:50:48 2020

@author: Rita O'Rourke
"""

#The data we need to retrieve
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. The winner of the election based on popular vote

#Modules: Add our dependencies and to connect to files path
import csv
import os

# Assign a variable to load a file from a path (set path for file).
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = "/Users/ROR/Desktop/ucb_data_analytics/module3_pypoll_python/Election_Analysis/Resources/election_results.csv"

# # Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = "/Users/ROR/Desktop/ucb_data_analytics/module3_pypoll_python/Election_Analysis/analysis/election_analysis.txt"

#1. Initialize a total vote counter 
total_votes = 0

#Candidate option list/array
candidate_options = []

# Declare an empty dictionary to find the number of votes for each candidate
# where the key is each candidate's name and the vote count is the value for the key
candidate_votes = {}

# To determine the winning candidate by the number and percentage of votes,
# Need to declare variable that holds empty string value for the winning candidate,
# Declare a variable for winning count, equal to zero
# Declare a variable for winning_percentage equal to zero
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        #2. Add the total vote count
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate, get the unique names
        if (candidate_name not in candidate_options):
            # Add it to the list/array of candidates
            candidate_options.append(candidate_name)
            
            # Create each candidate as key and begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
            
        # Increment candidate's vote/Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
    #3. Percentage of votes each candidate won
    # Loop through candidate_options list to get the candidate's name
    # Loop through candidate_votes dictionary to retrieve the votes 
    # Calculate percentage of the vote count
    for candidateName in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidateName]
        
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # To do: print out each candidate's name, vote count, and percentage of votes
        print(f"{candidateName}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #5. Create if statement to determine vote count that was calculated is greater than
        # winning_count and vote_percentage greater than winning_percentage
        if((votes > winning_count) and (vote_percentage > winning_percentage)):
            # If true, then set the winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage 
            # Set the winning_candidate equal to candidate's name
            winning_candidate = candidateName 
 
    # Print winning candidate summary
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%"
    )
    print(winning_candidate_summary)

     
# Close the file.
election_data.close()