## `manner-of-thpeaking`
Description

_Tho, I came Acroth thith therieth of inthturcthins, and thomething that thaid "the key ith the attached litht of ATHCII printableth." Tho anywayth, here'th the inthtructhinth._

And two files, `inthtructhins.txt` and `printableth.txt`.

Hints:

_Pardon my LITHP_

_Backthaltheth in printableth.txt are ethcape charachterth_

So `printableth.txt` is filled with weird strings with only `c`, `a`, `d`, and `r` letters. Looking at the hint, it turns out this is a weird list processing on Common LISP programming language, with `a` means take the first element and `d` means took every element except the first element. So I made a program `thpeaking.py` to parse the strings inside `inthtructhins.txt`.

Basically what I do is pushing the `printableth.txt` list to a list of list (I had to do it manually because I'm lazy to think about parsing tuplets), removing the letter `c` and `r` from each word on `inthtructhins.txt` and parse it from behind to get the flag.
