#!/usr/bin/python
__author__ = 'Timothy Snowberger'

import csv

with open(r'hygxyz.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)