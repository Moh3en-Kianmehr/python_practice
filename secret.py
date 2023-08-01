#edabit https://edabit.com/challenge/arFpErP9oz36oTcXW secret function

import re

def secret(string):
    x = string[0]
    result = re.split(r"\.", string)
    s = f"<{result[0]}. {result[1]} = '{result[2]}'></p>"

    return s

print(secret('p.class.five'))