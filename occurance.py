"""
author: Srikar Sundaram
lang: python3.7
filename: occurance.py
desc: Processes how many times a function occurs given the brodmann area number
"""


def process_file_brod(filename):
    """
        Processes a tsv file of brodmann areas.

        :param filename: name of the file relative to the current directory
    """
    struct = dict()
    file = open(filename)
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        line = line.split("\t")
        line[1] = [*map(int, line[1].split(","))]
        struct[line[0]+"\t\t"+line[2]] = line[1]
    file.close()

    return struct


def process_table(filename):
    """
        Processes a tsv file of table.

        :param filename: name of the file relative to the current directory
    """
    file = open(filename)
    struct = dict()
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        line = line.split("\t")
        line[1] = line[1].split(",")
        line[1] = [*map(int, line[1])]
        struct[line[0]] = line[1]
    file.close()

    return struct


def getfunc(num, dic):
    """
        Given a brodmann area number and and directory of functions will look up which function is active.

        :param num: the brodmann area number for the area which will be looked up
        :param dic: dictionary of functions
    """
    val = []
    for key in dic:
        if num in dic[key]:
            for lol in key.split(","):
                val.append(lol)
    return val


def move_to_func(brd, dic):
    """
        Moves the brodmann area of cortex which is active and will check which function is active.

        :param brd: dictionary of the dicrectory brodmann area which will be looked up.
        :param dic: dictionary of the dicrectory of functions
    """
    func = dict()

    for k in brd:
        v = brd[k]
        val = [*map(lambda x: getfunc(x, dic), v)][0]
        func[k] = val
    return func


def count_times(func):
    """
        Checks how many times a function repeats.

        :param func: dictionary in the format (k, v): (name of brodmann area, name of the functions) 
    """
    times = dict()
    print(func.keys())
    for val in func.values():
        for v in val:
            inc = 1
            v = v.split("\t\t")[0]
            if v in times:
                times[v] += inc
            else:
                times[v] = inc
    return times


def print_result(times):
    """
        Prints how many times the function repeats in the table file. 

        :param times: dictionary of how many times a function repeats. format: (k, v): (name of the function, how many times the funciton occurs)
    """
    sor = sorted(times.items(), key=lambda item: item[1], reverse=True)
    for k, v in sor:
        print(k, "occurs", v, "time/s")


def main(brodmann, table):
    """
        Prints how many times the function repeats in the table file. 

        :param brodmann: name of the file of the tsv file in which directory of functions
        :param table: name of the file of the tsv file in which table of active areas is.
    """

    dic = process_file_brod(brodmann)
    brd = process_table(table)
    func = move_to_func(brd, dic)
    times = count_times(func)
    print_result(times)
