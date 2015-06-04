#!/usr/bin/env python
# -*- coding: utf-8 -*
# Osamu Fujimoto - January 2014

import lxml.html
import csv

# Grabs the schedules from http://courses.k-state.edu and save its to a csv file.
# This was part of a schedule maker that I was planning to make.
def main():
    out_file = open('results.csv', 'wb')
    writer = csv.writer(out_file, delimiter=',')
    writer.writerow(['CourseID', 'Section', 'Type', 'Number', 'Units', 'Basis',
                    'Days', 'Hours', 'Facility', 'Instructor', 'Comment1'])
    url = 'http://courses.k-state.edu/fall2014/CIS/'
    page = lxml.html.parse(url)

    cid = ''
    for elem in (page.findall('//tbody[@class]')):
        if elem.find('tr/th/span[@class="number"]') is not None:
            cid = elem.find('tr/th/span[@class="number"]').text
        else:
            section = elem.find('tr[1]/td[1]').text
            mytype = elem.find('tr[1]/td[2]').text
            number = elem.find('tr[1]/td[3]').text
            units = elem.find('tr[1]/td[4]').text
            if elem.find('tr[1]/td[5]/span') is not None:
                basis = elem.find('tr[1]/td[5]/span').text
            else: basis = 0
            days = elem.find('tr[1]/td[6]').text
            hours = elem.find('tr[1]/td[7]').text
            if elem.find('tr[1]/td[8]/a') is not None and days != "Appointment":
                facility = elem.find('tr[1]/td[8]/a').text
            else: facility = 0 
            if days == "Appointment":
                inst = elem.find('tr[1]/td[9]').text
            else:
                inst = elem.find('tr[1]/td[10]').text
            if days is not None:
                days = days.encode('ascii', 'ignore')
                days = days.strip()
            else: days = 0
            if hours is None: hours = 0

            comment = ''
            if elem.find('tr[2]/td/ul/li') is not None:
                for li in elem.findall('tr[2]/td/ul/li'):
                    comment += li.text + ' '
            else:
                comment = 0

            writer.writerow([cid, section, mytype, number, units, basis, days,
                            hours, facility, inst, comment])
    out_file.close()


if __name__ == "__main__":
    main()
