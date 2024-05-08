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

cipher = cipher.replace("\n", "")


def find_digraphs(sequence):
    digraphs = {}
    for i in range(len(sequence) - 1):
        digraph = sequence[i] + sequence[i + 1]
        if digraph in digraphs:
            digraphs[digraph] += 1
        else:
            digraphs[digraph] = 1
    return digraphs

digraph_dict = find_digraphs(cipher)

print("REPEATED DIGRAPHS:")
counter = 0
for i, j in digraph_dict.items():
    if j > 1:
        counter += 1
    print(i, j) if j > 1 else None
print("Total repeated digraphs:", counter)