# the goal of this code is to give all the chords of a given key


import random


KeySignatures = {
   "Key of C Major":{
       "I": "C Major",
       "ii": "D Minor",
       "iii": "E Minor",
       "iv": "F Major",
       "V": "G Major",
       "vi": "A Minor",
       "vii": "B Diminished"
},
    "Key G Major":{
       "I": "G Major",
       "ii": "A Minor",
       "iii": "B Minor",
       "IV": "C Major",
       "V": "D Major",
       "vi": "E Minor",
       "vii": "F# Dimished"
},
    "Key of D Major":{
        "I": "D Major",
        "ii": "E Minor",
        "iii": "F# Minor",
        "IV": "G Major",
        "V": "A Major",
        "vi": "B Minor",
        "vii": "C# Dimished"
},
    "Key of A Major":{
        "I": "A Major",
        "ii": "B Minor",
        "iii": "C# Minor",
        "IV": "D Major",
        "V": "E Major",
        "vi": "F# Minor",
        "vii": "G# Dimished"
},
    "Key of E Major":{
        "I": "E Major",
        "ii": "F# Minor",
        "iii": "G# Minor",
        "IV": "A Major",
        "V": "B Major",
        "vi": "C# Major",
        "vii": "D# Dimished"
},
    "Key of B Major":{
        "I": "B Major",
        "ii": "C# Minor",
        "iii": "D# Minor",
        "IV": "E Major",
        "V": "F# Major",
        "vi": "G# Major",
        "vii": "A# Major"
},
    "Key of F# Major":{
        "I": "F# Major",
        "ii": "G# Minor",
        "iii": "A# Minor",
        "IV": "B Major",
        "V": "C# Major",
        "vi": "D# Minor",
        "vii": "E# Dimished"
 },
    "Key of C# Major":{
        "I": "C# Major",
        "ii": "D# Minor",
        "iii": "E# Minor",
        "IV": "F# Major",
        "V": "G# Major",
        "vi": "A# Minor",
        "vii": "B# Diminished"
},
    "Key of F Major":{
        "I": "F Major",
        "ii": "G Minor",
        "iii": "A Minor",
        "IV": "Bb Major",
        "V": "C Major",
        "vi": "D Minor",
        "vii": "E Diminished"
},
    "Key of Bb Major":{
        "I": "Bb Major",
        "ii": "C Minor",
        "iii": "D Minor",
        "IV": "Eb Major",
        "V": "F Major",
        "vi": "G Minor",
        "vii": "A Diminished"
},
    "Key of Eb Major":{
        "I": "Eb Major",
        "ii": "F Minor",
        "iii": "G Minor",
        "IV": "Ab Major",
        "V": "Bb Major",
        "vi": "C Minor",
        "Vii": "D Diminished"
},
    "Key of Ab Major":{
        "I": "Ab Major",
        "ii": "Bb Minor",
        "iii": "C Minor",
        "IV": "Db Major",
        "V": "Eb Major",
        "vi": "F Minor",
        "vii": "G Diminished"
},
    "Key of Db Major":{
        "I": "Db Major",
        "ii": "Eb Minor",
        "iii": "F Minor",
        "IV": "Gb Major",
        "V": "Ab Major",
        "vi": "Bb Minor",
        "vii": "C Diminished"
},
    "Key of Gb Major":{
        "I": "Gb Major",
        "ii": "Ab Minor",
        "iii": "Bb Minor",
        "IV": "Cb Major",
        "V": "Db Major",
        "vi": "Eb Minor",
        "vii": "F Diminished"
},
    "Key of Cb Major":{
        "I": "Cb Major",
        "ii": "Db Minor",
        "iii": "Eb Minor",
        "IV": "Fb Major",
        "V": "Gb Major",
        "vi": "Ab Minor",
        "vii": "Bb Diminished"
    }

}
#print(KeySignatures)
#print(KeySignatures["Key of C Major"])
RandomKey = random.choice(list(KeySignatures.keys()))
#print(KeySignatures[RandomKey])

userinput= input(f"What are all the chords that belong in the {RandomKey}?")
if userinput == "C Major, D Minor, E Minor, F Major, G Major, A Minor, B Diminished":
    print("That's correct!")

elif userinput == "G Major, A Minor, B Minor, C Major, D Major, E Minor, F# Diminished":
    print("That's correct!")

elif userinput == "D Major, E Minor, F# Minor, G Major, A Major, B Minor, C# Diminished":
    print("That's correct!")

elif userinput == "A Major, B Minor, C# Minor, D Major, E Major, F# Minor, G# Diminished":
    print("That's correct!")

elif userinput == "E Major, F# Minor, G# Minor, A Major, B Major, C# Minor, D# Diminished":
    print("That's correct!")

elif userinput == "B Major, C# Minor, D# Minor, E Major, F# Major, G# Minor, A# Diminished":
    print("That's correct!")

elif userinput == "F# Major, G# Minor, A# Minor, B Major, C# Major, D# Minor, E# Diminished":
    print("That's correct!")

elif userinput == "C# Major, D# Minor, E# Minor, F# Major, G# Major, A# Minor, B# Diminished":
    print("That's correct!")

elif userinput == "F Major, G Minor, A Minor, Bb Major, C Major, D Minor, E Diminished":
    print("That's correct!")

elif userinput == "Bb Major, C Minor, D Minor, Eb Major, F Major, G Minor, A Diminished":
    print("That's correct!")

elif userinput == "Eb Major, F Minor, G Minor, Ab Major, Bb Major, C Minor, D Diminished":
    print("That's correct!")

elif userinput == "Ab Major, Bb Minor, C Minor, Db Major, Eb Major, F Minor, G Diminished":
    print("That's correct!")

elif userinput == "Db Major, Eb Minor, F Minor, Gb Major, Ab Major, Bb Minor, C Diminished":
    print("That's correct!")

elif userinput == "Gb Major, Ab Minor, Bb Minor, Cb Major, Db Major, Eb Minor, F Diminished":
    print("That's correct!")

elif userinput == "Cb Major, Db Minor, Eb Minor, Fb Major, Gb Major, Ab Minor, Bb Diminished":
    print("That's correct!")

else:
    print("That is incorrect!")
