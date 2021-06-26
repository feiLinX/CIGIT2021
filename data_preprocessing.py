import numpy as np
import os, glob
import csv, random

ROOT = 'E:\\PythonWorkplace\\CIGIT2021\\data\\622'
filename = '2020-05-01-gps.csv'
data = ROOT + '\\' + filename

with open(data, 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
    for
    print(result[0][0])