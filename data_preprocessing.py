import numpy as np
import csv, random
from math import sin, asin, cos, radians, fabs, sqrt

ROOT = '/home/rick/PythonWorkplace/CIGIT2021/data/622'
filename = '2020-05-01-gps.csv'
data = ROOT + '/' + filename

# Definition of 'number or not' func
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# Definition of 'Computation of distance from longitude and latitude' func
def hav(theta):
    s = sin(theta / 2)
    return s * s

def get_distance_hav(lat0, lng0, lat1, lng1):
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance

EARTH_RADIUS = 6371


# Read CSV
lati = []
longi = []
v = []
with open(data, 'r', encoding='gbk') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == '渝BW2233':
            if is_number(row[2][9]) == True and is_number(row[2][10]) == False:  # 6 - 9
                if int(row[2][9]) >= 6:
                    tmp_lati = float(row[3])
                    tmp_longi = float(row[4])
                    tmp_v = int(row[6])

                    lati = np.append(lati, tmp_lati)
                    longi = np.append(longi, tmp_longi)
                    v = np.append(v, tmp_v)

            elif is_number(row[2][9]) == True and is_number(row[2][10]) == True:  # 10 - 21
                tmp_lati = float(row[3])
                tmp_longi = float(row[4])
                tmp_v = int(row[6])

                lati = np.append(lati, tmp_lati)
                longi = np.append(longi, tmp_longi)
                v = np.append(v, tmp_v)
        else:
            continue

'''
distance = [0]
coord = [0]
for i in range(1, len(lati)):
    tmp_d = get_distance_hav(lati[i-1], longi[i-1], lati[i], longi[i])
    distance = np.append(distance, tmp_d)
    coord = np.append(coord, coord[i-1] + tmp_d)
'''
ans = get_distance_hav(29.683626,106.58997,29.683285,106.593353)