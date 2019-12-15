import json
import pickle
import crypto
from datetime import date

def new_game():
    test = {
        "Name": "Test_Nyantaro:N-1436",
        "food_level": 100,
        "brain_power": 100,
        'food_stoc': 0,
        'money': 100,
        "last_played": "10-15-1998",
        "invt": []
    }

    y = json.dumps(test)

    pickle.dump(y, open("save_game.pickle", "wb"))

    return pickle.load(open("save_game.pickle", "rb"))

def cont_game():
    save = pickle.load(open("save_game.pickle", "rb"))
    return(json.loads(save))


'''try:
    save = pickle.load(open("dict.pickle", "rb"))
    print(save)
except (OSError, IOError) as e:
    test = {
        "food_level": "0",
        "brain_power": "0",
        "last_played": "10-15-1998",
        "invt": ""
    }

    y = json.dumps(test)

    pickle.dump(y, open("dict.pickle", "wb"))

save1 = json.loads(save)
date = date.today()
date = str(date)
if save1['last_played'] == "10-15-1998" :
    save1['last_played'] = date
    save1['food_level'] = 100
    save1['brain_power'] = 100

date_old = save1['last_played'].split('-')
date_new = date.split('-')

if int(date_new[2]) - int(date_old[2]) >= 7:
    print("test")
else:
    print("test1")

save = json.dumps(save1)
pickle.dump(save, open("dict.pickle", "wb"))

save = pickle.load(open("dict.pickle", "rb"))
print(save)'''




