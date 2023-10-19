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
        list_from_line = line.split()
        if len(list_from_line) < 3:
            continue

        counter += 1

        if list_from_line[-2] in status_codes.keys():
            status_codes[list_from_line[-2]] += 1
        files_size += int(list_from_line[-1])

        if counter == 10:
            output += "File size: {}\n".format(files_size)
            for key in status_codes.keys():
                if status_codes[key] > 0:
                    output += "{}: {}\n".format(key, status_codes[key])
            print(output, end='')
            counter = 0
            output = ""
    except KeyboardInterrupt:
        output = ""
        output += "File size: {}\n".format(files_size)
        for key in status_codes.keys():
                if status_codes[key] > 0:
                    output += "{}: {}\n".format(key, status_codes[key])
        print(output, end='')
        raise
