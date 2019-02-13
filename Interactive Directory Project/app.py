import json;
from difflib import get_close_matches;
error_msg="Word not found"
data=json.load(open("data.json"))

def keyword(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        return "Did you mean %s instead?" %get_close_matches(word,data.keys())[0]
    else:
        return (error_msg)

word=input("Enter a word to look for..")
print(keyword(word))
