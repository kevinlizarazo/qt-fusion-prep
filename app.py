#!/usr/bin/env python 
# Kevin Lizarazo
# 2016-06-29
# QT/P Route processor

import os
import csv

path = 'CSV/'
files = os.listdir(path) 

#user_input = raw_input('Please enter a filename, no suffix: ')


#fh = open('CSV/' + user_input + '.csv', 'rB')
for file in files[1:]:
    route_list = ['address,name,placement,draw,marker \n']
    route_object = ''
    count = 0
    position = 0 
    fh = open('CSV/' + file, 'rB')
    reader = csv.reader(fh)

    for line in reader:
        if line[0]:
            address = '"{} {}, Queens NY, {}"'.format(line[0],line[1],line[2])
            name = line[3]
            placement = line[4]
            draw = line[5]
            if line[3] == 'PRESS BOX' or line[3] == 'TRIBUNE BOX' or line[3] == 'TRIB BOX':
                marker = 'large_blue'
            else:
                marker = 'large_red'
            route_object = address + ',' + name + ',' + placement + ',' + draw + ',' + marker
            route_list.append(route_object + '\n')
            count = count + 1

    fh.close()
    #fh = open('Output/' + user_input + ' processed' + '.csv', 'a')
    fh = open('Output/' + file + ' processed.csv', 'a')

    while position <= count:
        fh.write(route_list[position])
        position = position + 1

    fh.close()

    print 'New file created in a folder called Output.'
