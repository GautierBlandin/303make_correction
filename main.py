input = "tty: tty.o fs.h"

def parse(input):
    input = input.split(" ")
    input = [i.split(":") for i in input]
    return input