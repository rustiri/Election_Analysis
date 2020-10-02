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



#Modules: to connect to files path & add dependencies
import csv
import os

# Assign a variable to load a file from a path (set path for file).
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = "/Users/ROR/Desktop/ucb_data_analytics/module3_pypoll_python/Election_Analysis/Resources/election_results.csv"

# # Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = "/Users/ROR/Desktop/ucb_data_analytics/module3_pypoll_python/Election_Analysis/analysis/election_analysis.txt"


# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file
    for row in file_reader:
        print(row)
     
# Close the file.
election_data.close()