import itertools
from functools import reduce
import operator
import numpy as np
import re

def day_1_1(infile):
    f = open(infile, 'r')
    lines = [int(line) for line in f.readlines()]
    f.close
    for pair in itertools.combinations(lines,2):
        if(sum(pair) == 2020):
            return(reduce(operator.mul, pair, 1))

def day_1_2(infile):
    f = open(infile, 'r')
    lines = [int(line) for line in f.readlines()]
    f.close
    for trip in itertools.combinations(lines,3):
        if(sum(trip) == 2020):
            return(reduce(operator.mul, trip, 1))

def split_line(line):
    ch1, ch2, string = line.split()
    low, high = ch1.split("-")
    char = ch2.replace(':', "", 1)
    return int(low), int(high), char, string

def day_2_1(infile):
    f = open(infile, 'r')
    lines = [line for line in f.readlines()]
    f.close
    count = 0
    for line in lines:
        low, high, char, string = split_line(line)
        if low <= string.count(char) <= high:
            count += 1
    return count

def day_2_2(infile):
    f = open(infile, 'r')
    lines = [line for line in f.readlines()]
    f.close
    count = 0
    for line in lines:
        low, high, char, string = split_line(line)
        low -= 1
        high -= 1
        try:
            if (string[low] == char) ^ (string[high] == char):
                count += 1
        except IndexError:
            next
    return count

def day_3_1(infile, right, down):
    f = open(infile, 'r')
    lines = [line.rstrip() for line in f.readlines()]
    f.close
    rows = len(lines)
    cols = len(lines[0])
    row = 0
    col = 0
    count = 0
    while row < rows:
        row = row + down
        if (col + right) >= cols:
            incr = right - (cols - col)
            col = incr
        else:
            col = col + right
        try:
            if (lines[row][col] == "#"):
                count += 1
        except IndexError:
            next
    return count

def day_3_2(infile, right, down):
    f = open(infile, 'r')
    lines = [line.rstrip() for line in f.readlines()]
    f.close
    rows = len(lines)
    cols = len(lines[0])
    row = 0
    col = 0
    count = 0
    while row < rows:
        row = row + down
        if (col + right) >= cols:
           incr = right - (cols - col)
           col = incr
        else:
            col = col + right
        try:
            if (lines[row][col] == "#"):
                count += 1
        except IndexError:
            next
    return count

def check_pport(_pport):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for key in keys:
        if key not in _pport and key is not 'cid':
            return 0
        if key == 'byr':
            if re.match('^\d{4}$', _pport[key]) is None:
                return 0
            elif int(_pport[key]) < 1920 or int(_pport[key]) > 2002:
                return 0
        elif key == 'iyr':
            if re.match('^\d{4}$', _pport[key]) is None:
                return 0
            elif int(_pport[key]) < 2010 or int(_pport[key]) > 2020:
                return 0
        elif key == 'eyr':
            if re.match('^\d{4}$', _pport[key]) is None:
                return 0
            elif int(_pport[key]) < 2020 or int(_pport[key]) > 2030:
                return 0
        elif key == 'hgt':
            if re.match('^\d+in', _pport[key]) is None and re.match('^\d+cm', _pport[key]) is None:
                return 0
            elif re.match('^\d+in', _pport[key]) is not None:
                height = _pport[key].replace('in', '')
                if int(height) < 59 or int(height) > 76:
                    return 0
            elif re.match('^\d+cm', _pport[key]) is not None:
                height = _pport[key].replace('cm', '')
                if int(height) < 150 or int(height) > 193:
                    return 0
        elif key == 'hcl':
            if re.match('^#[a-f0-9]{6}$', _pport[key]) is None:
                return 0
        elif key == 'ecl':
            if re.match('^(amb|blu|brn|gry|grn|hzl|oth)', _pport[key]) is None:
                return 0
        elif key == 'pid':
            if re.match('^[0-9]{9}$', _pport[key]) is None:
                return 0
    return 1

def day_4_1(infile):
    f = open(infile, 'r')
    lines = [line for line in f.readlines()]
    f.close
    pport = {}
    count = 0
    for line in lines:
        if line == "\n" or line == "\r":
            count += check_pport(pport)
            pport = {}
            next
        pairs = line.split()
        for pair in pairs:
            key, val = pair.split(":", 1)
            pport[key] = val
    count += check_pport(pport)
    return count

def day_5_1(infile):
    f = open(infile, 'r')
    lines = [line for line in f.readlines()]
    f.close
    seven = "FBFBBFFRLR"
    seat = 128
    for pos in seven:





if __name__ == "__main__":
    # val = day_1_1('day_1_1_input.txt')
    # val = day_1_2('day_1_1_input.txt')
    # val = day_3_2('day_2_1_input.txt')
    # val = day_3_1('day_3_1_input.txt', 1, 1)
    # val = 0
    # val = day_3_2('day_3_1_input.txt', 1, 1)
    # val *= day_3_2('day_3_1_input.txt', 3, 1)
    # val *= day_3_2('day_3_1_input.txt', 5, 1)
    # val *= day_3_2('day_3_1_input.txt', 7, 1)
    # val *= day_3_2('day_3_1_input.txt', 1, 2)
    # val = day_4_1('day_4_1_input.txt')
    val = day_5_1('day_5_1_input.txt')
    print(val)
