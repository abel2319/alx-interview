#!/usr/bin/python3
"""Log parsing Module
"""
import sys


files_size = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0
                }
output = ""
counter = 0
for line in sys.stdin:
    try:
        list_from_line = line.split()[::-1]
        if len(list_from_line) < 3:
            continue

        counter += 1

        if list_from_line[1] in status_codes.keys():
            status_codes[list_from_line[1]] += 1
            files_size += int(list_from_line[0])

        if counter == 10:
            output += "File size: {}\n".format(files_size)
            for key in status_codes.keys():
                output += "{}: {}\n".format(key, status_codes[key])
                status_codes[key] = 0
            print(output, end='')
            files_size = 0
            counter = 0
            output = ""
    finally:
        output += "File size: {}\n".format(files_size)
        for key in status_codes.keys():
            output += "{}: {}\n".format(key, status_codes[key])
        print(output, end='')
