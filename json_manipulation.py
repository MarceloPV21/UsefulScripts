import json

with open("data.json","r") as f:

    data = json.load(f)

def readJson(name, syllable, meaning, phrase, partOfSp, resource):

    print(name, syllable, meaning, phrase, partOfSp, resource)

def getJson():
    for k in data:
        readJson(k['name'],k['syllable'],k['meaning'],k['phraseWithWord'],k['partOfSpeech'],k['resource'])
    

if __name__ == "__main__":
    
    getJson()