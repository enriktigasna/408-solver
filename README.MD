# Solving Zodiac cipher 408 from scratch.. almost

In recent days i've been kinda captivated by the zodiac ciphers, and found them to be fascinating. Especially since I have been at the swedish cyber-championships and one of the big topics there is cryptography.

I have decided to do my best to recreate the solution for the 408 cipher without explicitly looking at it. I kinda know parts of the solution in my brain but I intend to recreate the cipherkeys from scratch.

I am NOT to look at existing solutions or cheat from the time that I start this project. The purpose is to recreate how a clueless or semi-clueless may have solved it.

## Methodology
1. To begin I will make a 0-Z ASCII remake of the cipher to make it easier for program to process it.
2. I will look for common repeating strings of length 2 and match them to real repeating strings, example I know outright is to look for LL.
3. Create a program that will decipher instantly when I give it a substitution key. This is an advantage that I have over the people that solved this back in the late 60s. I have a computer that can do pretty much instant substitution.

## Purpose
Just to learn some stuff about cryptography and document my journey incase someone in the future finds this useful. I might find out some interesting details along the way.

## Writeup

First of all if you for some reason want to read my exact thoughts and procedure consult the notes.

### Encoding
First I gave each symbol an ASCII representation and for hand encoded it into a text string, so that a program can easily handle it.

[Insert image of zodiac cipher]

This was my rules:

```
Triangle: 0
Square with white in top left: 1
Square with white in top right: 2
Filled square: 3
Square with dot: 4
Square: 5
Filled circle: 6
Filled triangle: 7
Triangle with dot: 8
Backward slash: 9

Slash: /

Lambda: ^ (A without dash)

Circle with dot: o


Zodiac symbols:
horizontal line: -
plus: +
vertical line: |

ACTUAL PLUS: a

I-looking thing with bottom kinda round: w

Almost t looking thing?: x

Letters:
CAPITAL LETTER
Backwards/Upside-down letters:
lowercase letter
```

Now that I have made these rules I decoded the cipher into this

```
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
```
## Analysis and Scripts

First we have the frequency analysis, which we can find in frequency-analysis.py

Then we have the digraph analysis, and a simulation.

The simulation spits out a nice normal distribution graph.

[Show simulation]

[Show graph]

Clearly it is in the 0.01th percentile or something in the amount of repeating digraphs, which shows that it is a substitution cipher, that decodes to human text.

However there are clearly way more charachters, than 27, which implies that there can be multiple keys for one char. This makes substitution a bit harder, but we just have to try some more.


From the cipher, the only repeating charachters are 11/square-square, and they are close together.

It is reasonable to assume that this would be something like KILL considering the theme of this cipher, and what the zodiac is usually putting out.

Update: I didn't realize the double threes too, but at the end they also turned out to be L's. Oops.

[Show repeating asciis]

After putting KILL into the correct locations I got this, which seems to be an amazing start.

```
IL.K.K..L........
..K.I...I........
.................
..KI.............
.................
...I.I........K..
..........I......
..K..............
...............I.
.................
.................
.I.........K.....
.......L........I
......I..........
K....I...........
...........KILL..
......KILL.......
.............I.I.
L................
...I.......IL....
.....IK..........
..............LI.
.................
....I............
```

I then put in some more stuff like ILIKEKILLING in the beginning.

(Reference my "saves" to see it it would fill up too much space)

Then I made the beginning

ILIKEKILLINGPEOPLE because it would fit in the with the last L on the line

from there i could fill in GIRL and PARADICE

That made COLLECTING very clear.

Then I got stuck for a while chasing kinda empty leads like filling in
ED after different KILL that were popping up.

The word KILL was just popping up everywhere while solving this cipher, which was a bit creepy tbh.

Then I realized
.I.G...R.OCK.O...
IT..GIRL.......PI

And remembered that there was something about ROCKS OFF (which is maybe cheating but I can't help accidentally remembering something).

So I filled in
ROCKS OFF WITH A GIRL

After that the board became way more filled up and progress was pretty fast, and I had some leads to chase.

After filling in around 50 keys I finally got a readable output.

ILIKEKILLINGPEOPL
EBECAUSEITISSOMUC
HFUNITISMOREFUNTH
ANKILLINGWIPDGAME
INTHEFORRESTBECAU
SEMANISTHEMOSTEAN
GERTUEANAMALOFALL
TOKILLSOMETHINGGI
VESMETHEMTSTTHRIL
LINGE.PERENCEITIS
EVENBETTERTHANGET
TINGYOURROCKSOFFW
ITHAGIRLTHEBESTPA
RTOFITISTHAEWHENI
EIEIWILLBEREBORNI
NPARADICESNEALLTH
EIHAVEKILLEDWIYLB
ECOMEMYSLAVESIWIL
LNOTGIVEYOUMYNAME
BECAUSEYOUWILLTRY
TOSLOIEOWNORSTOPM
YCOLLECTINGOFSLAV
EYFOEMYAFTERLIFEE
EUSNEWUWSOEGTTSEE
BEORIETEMETHHPITI

This roughly decodes to

```
I LIKE KILLING PEOPLE BECAUSE IT IS SO MUCH FUN IT IS MORE FUN THAN KILLING WILD GAME IN THE FORREST (bad spelling lol) BECAUSE MAN IS THE MOST ANGERTUE ?? ANIMAL OF ALL TO KILL SOMETHING ??? THRILLING PERENCE IT IS EVEN BETTER THAN GETTING YOUR ROCKS OFF WITH A GIRL THE BEST PART OF IT IS THAT WHEN I DIE I WILL BECOME REBORN IN PARADICE ?? ALL THE PEOPLE I HAVE KILLED WILL BECOME MY SLAVES I WILL NOT GIVE YOU MY NAME BECAUSE YOU WILL TRY TO SLOW ME DOWN OR STOP MY COLLECTING (maybe collection?) OF SLAVES FOR MY AFTERLIFE 
```
Then it is gibberish but it is supposed to end in gibberish
