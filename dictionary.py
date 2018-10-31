import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return (w,data[w])
    elif  w.lower() in data:
        return (w.lower(),data[w.lower()])
    elif  w.upper() in data:
        return (w.upper(),data[w.upper()])
    elif  w.title() in data:
        return (w.title(),data[w.title()])
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn=="y":
            return (get_close_matches(w, data.keys())[0],data[get_close_matches(w, data.keys())[0]])
        elif yn == "N" or yn=="n":
            return ("The word doesn't exist. Please double check it.",w)
        else:
            return ("We didn't understand your entry.",w)
    else:
        return ("The word doesn't exist. Please double check it.",w)


word=""
while word!="exit":
    word = input("Enter word: ")
    (word2,output) = translate(word)
    print ("%s:" % word2)
    print ("{}:".format(word2))
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
