#!/usr/bin/python
__author__ = 'Timothy Snowberger, Kendall Brown'
#Added my name to the author string

import csv

with open(r'hygxyz.csv') as file_:
    reader = csv.reader(file_)
    for row in reader:
        print(row)