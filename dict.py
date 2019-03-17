import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data=json.load(open("076 data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
         yn=input("did you mean %s instead press Y if yes, otherwise N " %get_close_matches(w,data.keys())[0])
         yn=yn.upper()
         if yn=="Y":
             return data[get_close_matches(w,data.keys())[0]]
         elif yn=="N":
             return "there is no such word"
         else:
             return "invaild input"
    else:
        return "Word in incorrect try again."

word=input("Enter the word:")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
