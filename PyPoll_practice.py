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


#Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
#print the present time.
#print("The time right now is ", now)

#Modules: to connect to csv files
import os
import csv

# Assign a variable to load a file (set path for file).
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = "/Users/ROR/Desktop/ucb_data_analytics/module3_pypoll_python/Election_Analysis/Resources/election_results.csv"

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = "/Users/ROR/Desktop/ucb_data_analytics/module3_pypoll_python/Election_Analysis/analysis/election_analysis.txt"

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

# Close the file
#outfile.close()
txt_file.close()

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    #reader function to read file 
    #file_reader = csv.reader(election_data)
    # To do: perform analysis.
    print(election_data)
     
# Close the file.
election_data.close()