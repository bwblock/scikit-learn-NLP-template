#! /usr/bin/env python

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


#POIS = [x for x in enron_data if x['poi'] == True]
#print len(POIS)


print "number of data points", len(enron_data.keys())

POIS = [key for key in enron_data.keys() if enron_data[key]['poi'] == True]

print "number of pois: ", len(POIS)

print POIS

print enron_data["PRENTICE JAMES"]['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

paylist = [enron_data['SKILLING JEFFREY K']['total_payments'],enron_data['LAY KENNETH L']['total_payments'],enron_data['FASTOW ANDREW S']['total_payments']]
print max(paylist),paylist.index(max(paylist))

known_sal = sum([1 for key in enron_data.keys() if str(enron_data[key]['salary']).isdigit()])

print "number of known salaries: ", known_sal

known_email = sum([1 for key in enron_data.keys() if enron_data[key]['email_address'] != "NaN"])

print "number of known emails: ", known_email

unknown_payments = sum([1 for key in enron_data.keys() if enron_data[key]['total_payments'] == "NaN"])

print "number of unknown payments: ", unknown_payments

total_payment_poi = [enron_data[key]['total_payments'] for key in POIS]

print total_payment_poi

