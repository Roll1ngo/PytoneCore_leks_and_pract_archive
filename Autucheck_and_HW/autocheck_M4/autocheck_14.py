import sys


def parse_args():
    result = ""

    for i in sys.argv[1:]:
        result+= " " +i

    return result

print(parse_args())

