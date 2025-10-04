# This program reads in the data from "data.csv"
# and outputs each line as a list.
# Author: Elaine Cazetta

import csv

FILENAME= "data.csv"
DATADIR = "../my-work/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row is header row
            pass
    else: # all subsequent rows
        total += int(line[1])
    linecount += 1
print (f"average is {total/(linecount-1)}")