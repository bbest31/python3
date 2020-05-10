# Pickling is the process where Python objects are seralized into bytestreams and unpickled by converting bytestreams back into objects.
import pickle
import json

class SpaceMarine:
    def __init__(self, chapter, rank):
        self.chapter = chapter
        self.rank = rank
    
iron_hand = SpaceMarine("Iron Hands", "Chapter Master")

# writing technically in binary so need mode to be wb
# with open("space_marines.pickle", "wb") as f:
#     pickle.dump(iron_hand, f, pickle.HIGHEST_PROTOCOL)

    

# with open("space_marines.pickle", "rb") as f:
#     data = pickle.load(f)
#     print(data)

# JSON Pickling - can use external package called jsonpickle then do jsonpickle.encode() or jsonpickle.decode()
# formats a python object as a STRING of JSON
j = json.dumps(['foo', {'bar' : ('bam', None, 1.0, 2)}])
# j = json.dumps(iron_hand.__dict__)

print(j)