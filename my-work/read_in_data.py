# This program reads in the data from "data.csv"
# and outputs each line as a list.
# Author: Elaine Cazetta

import csv

FILENAME= "data.csv"
DATADIR = "../my-work/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)