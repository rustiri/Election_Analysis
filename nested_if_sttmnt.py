#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:49:02 2020

@author: ROR
"""

#What is the score?
score = int(input("What is your test score?"))

#Determine the grade
if score >= 90:
    print("Your grade is an A.")
else:
    if score >= 80:
        print("Your grade is a B.")
    else:
        if score >=70:
            print("Your grade is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print("Your grade is an F.")
                
#Using rule if-elif-else
#What is the score?
score = int(input("What is your test score?"))

#Determine the grade
if score >= 90:
    print("Your grade is an A.")
elif score >= 80:
    print("Your grade is a B.")
elif score >=70:
    print("Your grade is a C.")
elif score >= 60:
    print("Your grade is a D.")
else:
    print("Your grade is an F.")