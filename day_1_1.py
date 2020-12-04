import itertools
from functools import reduce
import operator
import numpy as np

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



if __name__ == "__main__":
    # val = day_1_1('day_1_1_input.txt')
    # val = day_1_2('day_1_1_input.txt')
    # val = day_3_2('day_2_1_input.txt')
    # val = day_3_1('day_3_1_input.txt', 1, 1)
    val = 0
    val = day_3_2('day_3_1_input.txt', 1, 1)
    val *= day_3_2('day_3_1_input.txt', 3, 1)
    val *= day_3_2('day_3_1_input.txt', 5, 1)
    val *= day_3_2('day_3_1_input.txt', 7, 1)
    val *= day_3_2('day_3_1_input.txt', 1, 2)
    print(val)
