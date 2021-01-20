import sys
import argparse

from interpreter.my_language import run

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str,
                    help="input program file")
parser.add_argument("-m", "--multithreaded", action="store_true",
                    help="run program in multithreaded mode", default=False)
args = parser.parse_args()

f = open(args.file, 'r')
file = f.read()
f.close()

value_table = run(file, args.multithreaded)
print('\n' + str(value_table))