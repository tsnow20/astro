#!/usr/bin/python
__author___ = 'Timothy Snowberger'

import csv

with open(r'C:\Users\tsnow.DATACORE\Projects\astro\astro\hygxyz.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)