import re
import json


def myFunc(jsonfile):
 with open(str(jsonfile)) as f:
    data = json.loads(f.read())
    newlist = [] 
    newdic = {}
    for i in data.values():
      pattern = r"(?<=\/)\d+(?=\/)"
      matches = re.findall(pattern, i)
      newlist.append(matches[0])
    print(newlist)
    for x in newlist:
        if str(int(x)) in newdic:
          newdic[str(int(x))] += 1
        else:
          newdic[str(int(x))] = 1
    return (newdic)
myFunc("34.json")

           


    


