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

freqs = {}
for i in range(len(cipher)):
    if cipher[i] in freqs:
        freqs[cipher[i]] += 1
    else:
        freqs[cipher[i]] = 1

print("FREQUENCY ANALYSIS:")
for i in sorted(freqs, key=freqs.get, reverse=True):
    print(i, freqs[i])