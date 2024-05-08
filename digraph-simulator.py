import random

cipher = ""
cipherkeys = {
    "0": ".",
    "1": ".",
    "2": ".",
    "3": ".",
    "4": ".",
    "5": ".",
    "6": ".",
    "7": ".",
    "8": ".",
    "9": ".",
    "+": ".",
    "-": ".",
    "/": ".",
    "|": ".",
    "^": ".",
    "A": ".",
    "B": ".",
    "D": ".",
    "E": ".",
    "F": ".",
    "G": ".",
    "H": ".",
    "I": ".",
    "J": ".",
    "K": ".",
    "L": ".",
    "M": ".",
    "N": ".",
    "O": ".",
    "P": ".",
    "Q": ".",
    "R": ".",
    "S": ".",
    "T": ".",
    "U": ".",
    "V": ".",
    "W": ".",
    "X": ".",
    "Y": ".",
    "Z": ".",
    "a": ".",
    "c": ".",
    "d": ".",
    "e": ".",
    "f": ".",
    'k': '.',
    'l': '.',
    'o': '.',
    'p': '.',
    'q': '.',
    'r': '.',
    't': '.',
    'w': '.',
    'x': '.'
}


def find_digraphs(sequence):
    digraphs = {}
    for i in range(len(sequence) - 1):
        digraph = sequence[i] + sequence[i + 1]
        if digraph in digraphs:
            digraphs[digraph] += 1
        else:
            digraphs[digraph] = 1
    return digraphs


dict = {}
for i in range(10000):
    cipher = ""
    for i in range(408):
        cipher += random.choice(list(cipherkeys.keys()))

    digraph_dict = find_digraphs(cipher)

    counter = 0
    for i, j in digraph_dict.items():
        if j > 1:
            counter += 1
        # print(i, j) if j > 1 else None
    if counter not in dict:
        dict[counter] = 1
    else:
        dict[counter] += 1

for i in sorted(dict):
    print(i, "." * (dict[i]//10))