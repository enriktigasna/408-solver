import copy

cipher = """
01P/Z/UB1kOR2pX2B
WV+eGYFo0HP4KwqYe
MJY^UIk8qTtNQYD6|
S-/03BPORAU2fRlqE
k^LMZJdr9pFHVWe7Y
4aqGD0KI|oqX86+S-
RNtIYElO7qGBTQS3B
Ld/P3B4XqEHMU^RRk
cZKqpI|WqI86LMr03
BPDRax2o9N-eEUHkF
ZcpOVWI6atL|l^RoH
I0DR5TYr9de/4XJQA
P6M7RUt1L|NVEKH2G
rIwJk604LMlNA|Z-P
+UpkA03BVW9aVTtOP
^2SrlfUeo8D+G11IM
Nk|ScE/011ZfAP5BV
peXqWq5F37ca40A0B
1OT6RUca5dYq5^SqW
VZeGYKE5TYA013Lt5
HwFBX0+XADd98Lw2q
5ed33oe6PORXQF1Gc
Z5JTaq57JIarBPQWo
VEXr0WIoqEHM|2UIk
"""


cipherkeys = {
    "0": "I",
    "1": "L",
    "2": "P",
    "3": "L",
    "4": "S",
    "5": "Y",
    "6": "T",
    "7": "A",
    "8": "S",
    "9": "R",
    "+": "E",
    "-": "N",
    "/": "K",
    "|": "H",
    "^": "N",
    "A": "W",
    "B": "L",
    "D": "N",
    "E": "E",
    "F": "S",
    "G": "A",
    "H": "T",
    "I": "T",
    "J": "F",
    "K": "S",
    "L": "T",
    "M": "H",
    "N": "E",
    "O": "N",
    "P": "I",
    "Q": "F",
    "R": "G",
    "S": "A",
    "T": "O",
    "U": "I",
    "V": "B",
    "W": "E",
    "X": "O",
    "Y": "U",
    "Z": "E",
    "a": "E",
    "c": "V",
    "d": "O",
    "e": "C",
    "f": "D",
    'k': 'I',
    'l': 'A',
    'o': 'E',
    'p': 'E',
    'q': 'M',
    'r': 'R',
    't': 'R',
    'w': 'O',
    'x': '.'
}


cipher_new = copy.copy(cipher)

for key in cipherkeys:
    for i in range(len(cipher)):
        if cipher[i] == key:
            cipher_new = cipher_new[:i] + cipherkeys[key] + cipher_new[i+1:]

print(cipher_new)