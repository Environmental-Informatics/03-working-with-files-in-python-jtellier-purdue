#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:28:57 2020

@author: jtellier
"""

"""This file is designed to input the raccoon life data, convert it
to a dictionary, and run summary statistics"""

from math import sqrt
"""file input"""
fin = open( "2008Male00006.txt", "r" ) #open the file
print(fin) #print file location

first = fin.readline() #read in the first (header) line
first = first.split(",") #split first line into a list of 15 strings (column headers)
lines = fin.readlines() #read to end of file, with each line as a string
last = lines[14] #extract last line separately
print(lines) #preliminary look at the data
fin.close() #close the file
Data = [0]*len(lines) #make a list of equal length to lines, propogated with zeroes
for lidx in range(len(lines)-1):
    Data[lidx] = lines[lidx].split(",") # split the line based on the separation flag
    Data[lidx][3] = int(Data[lidx][3]) #changing string to appropriate data type
    Data[lidx][4:6] = map(float,Data[lidx][4:6]) #changing string to appropriate data type
    Data[lidx][8:15] = map(float,Data[lidx][8:15]) #changing string to appropriate data type

print(Data) #checking that our input worked as intended

"""Conversion to Dictionary"""
raccoon = dict() #creating the dictionary
Data2 = [0]*15 #creating a blank list of size 15
for i in range(15):
    Data2[i] = [] #turning Data2 into a list of blank lists
Data2 #looking at Data2 to make sure it looks right
for i in range(15): #15 columns
    for j in range(14): #14 rows of data (skip last one with dead info)
        Data2[i].append(Data[j][i]) #adding the appropriate elements from Data to Data2 in order to get a list of columns
for j in range(15):
        raccoon[first[j]] = Data2[j]
raccoon #looking at raccoon to make sure it looks right
raccoon['Result'] = last #adding the last line of the data to the dictionary

"""Summary statistic functions for the dictionary"""
def listavg(lst): #function to compute mean of a list
    return sum(lst)/len(lst)

listavg(raccoon['ProbFoodCap']) #testing on floats
listavg(raccoon['George #']) #testing on integers

def listsum(lst): #function to compute sum of a list
    return sum(lst)

listsum(raccoon['ProbFoodCap']) #testing on floats
listsum(raccoon['George #']) #testing on integers
                
def distance(x1,x2,y1,y2): #function to compute distance travelled
    return sqrt((x2-x1)**2+(y2-y1)**2)
distance(0,10,0,10) #testing the function

"""creating and adding movement info"""
Movement = [0]*14 #placeholder list to hold incremental movement values
def list_dist(X,Y):
    for i in range(1,14): #compute the distance travelled between each timestep
        Movement[i]=distance(X[i-1],X[i],Y[i-1],Y[i])
list_dist(raccoon[' X'],raccoon[' Y'])
Movement #check the list
raccoon['Movement'] = Movement #adding movement data to the dictionary
listavg(raccoon[' X']) #average x location
listavg(raccoon[' Y']) #average y location
listsum(raccoon['Movement']) #total distance George moved in his life
listavg(raccoon['Energy Level']) #georges average energy level
raccoon['Result'] #what happened to george

"""writing output to a new file"""
fin = open( "Georges_life.txt", "w" ) #open output file
print(fin) #print file location
fin.write("Raccoon name: George \n") #write header info
fin.write("Average location: 591189.034454322, 4504604.085012094 \n")
fin.write("Distance traveled: 593.938275 \n")
fin.write("Average energy level: 563.621428 \n")
fin.write("Raccoon end state: George number 6 died from starvation \n")
fin.write(" \n") #empyt line
fin.write("Date"+"\t"+"Time"+"\t"+"X"+"\t"+"Y"+"\t"+"Asleep"+"\t"+"Behavior mode"+"\t"+"Distance traveled"+" \n")
for k in range(14):
    fin.write(str(raccoon['Day'][k])+"\t"+str(raccoon['Time'][k])+"\t"+str(raccoon[' X'][k])+"\t"+str(raccoon[' Y'][k])+"\t"+str(raccoon[' Asleep'][k])+"\t"+str(raccoon['Behavior Mode'][k])+"\t"+str(raccoon['Movement'][k])+" \n")
fin.close() #close the file and DONE

