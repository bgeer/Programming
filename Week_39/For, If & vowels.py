s = "Guido van Rossum heeft programmeertaal Python bedacht."

def check(ch):
    lvowel = ['a','e','i','o','u']
    uvowel = ['A','E','I','O','U']
    vowel = []
    for x in ch:
        # print(x in lvowel);
       if (x in lvowel) or (x in uvowel):
            vowel.append(x);
    return vowel

print(check(s));

