#!/usr/bin/python

#------------------------
# Chris Anatalio
# anataliocs@gmail.com
#------------------------

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#read text file and strip new lines
poiNames = [line.rstrip('\n') for line in open("../final_project/poi_names.txt")]
#names_file = pickle.load(open(, "r"))



#------------------------
#TOGGLES
#------------------------
printAllData = False
printAllFeatures = False
printAllNames = False


# TOGGLE
# ALL Data as JSON
#------------------------
if printAllData:
    print enron_data

# TOGGLE
# All FEATURES
#------------------------
if printAllFeatures:
    for d in enron_data["SKILLING JEFFREY K"]:
        print d

# TOGGLE
# Size of data set and/or Names
# uncomment print d to print out NAMES
# ------------------------
if printAllNames:
    for d in enron_data:
        print d




# ------------------------
# DATA
# ------------------------


# Number of features
#------------------------
featureCount = 0
for d in enron_data["SKILLING JEFFREY K"]:
    featureCount += 1
print "Feature Count:" , featureCount


# Size of data set and/or Names
#------------------------
count = 0
for d in enron_data:
    count += 1
print "Record Count: " , count


# How many POIs in Enron Data
#------------------------
countPois = 0
for d in enron_data:
    if enron_data[d]["poi"]:
        countPois += 1
print "POI count: " , countPois


# Total POIs
#------------------------
countPoisFromNames = 0
for l in poiNames:
    countPoisFromNames += 1
countPoisFromNames -= 2
print "POIs from Names: " , countPoisFromNames


# Total value of the stock belonging to James Prentice?
#------------------------
print "James Prentice Total Stock Value: " , enron_data["PRENTICE JAMES"]["total_stock_value"]

# How many email messages do we have from Wesley Colwell to persons of interest?
#------------------------
print "Wesley Colwell Total Email Msgs: " , enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# What's the value of stock options exercised by Jeffrey K Skilling?
#------------------------
print "Exercised Stock Options Jeffrey K Skilling: " , enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]


# Who took home the most money
#------------------------
print "Biggest take home"
print "     Lay Takehome: " , enron_data["LAY KENNETH L"]["total_payments"]
print "     Skilling Takehome: " , enron_data["SKILLING JEFFREY K"]["total_payments"]
print "     Fastow Takehome: " , enron_data["FASTOW ANDREW S"]["total_payments"]


# How many have a defined salary
#------------------------
definedSalary = 0
for d in enron_data:
    if enron_data[d]["salary"] != "NaN":
        definedSalary += 1
print "Defined Salary count: " , definedSalary

# How many have a known email
#------------------------
knownEmail = 0
for d in enron_data:
    if enron_data[d]["email_address"] != "NaN":
        knownEmail += 1
print "Known Email count: " , knownEmail

# How many people in the E+F dataset have "NaN" for their total payments?
# What percentage of people in the dataset as a whole is this?
nanTotalPayment = 0
for d in enron_data:
    if enron_data[d]["total_payments"] == "NaN":
        nanTotalPayment += 1
print "Unknown Total Payment count: " , nanTotalPayment
print "% of Total Dataset" , ( float(nanTotalPayment) / float(count) ) * 100


# How many POIs in the E+F dataset have NaN for their total payments?
# What percentage of POI's as a whole is this?
nanTotalPaymentPois = 0
for d in enron_data:
    if enron_data[d]["poi"]:
        if enron_data[d]["total_payments"] == "NaN":
            nanTotalPaymentPois += 1
print "Unknown Total Payment of POIs count: " , nanTotalPaymentPois
print "% of Total POIs" , ( float(nanTotalPaymentPois) / float(countPois) ) * 100