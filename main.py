import json
import time

with open('./gamedata/menu.json', 'r') as file:
    data = json.load(file)

def thisisactuallyanumber(number):
    try:
        int(number)
        return(True)
    except ValueError:
        return(False)

def loadUnit(unit_ID):
    current_unit = data['units'][unit_ID]
    for i in range(len(current_unit['text'])):
        print(current_unit['text'][i])
        # if not i == len(current_unit['text']) - 1:
        #     time.sleep(1.5)
    time.sleep(0.5)
    if 'options' in current_unit:
        opt = current_unit['options']
        for i in range(len(opt)):
            print(f"{i+1}. {opt[i]['text']}")
        
        okay_answer = False
        answer = input()
        while not okay_answer:
            if thisisactuallyanumber(answer) and int(answer) - 1 in range(len(opt)):
                okay_answer = True
            else:
                print("I'm sorry, come again?")
                answer = input()
            
        chosen = int(answer) - 1
        next_ID = opt[chosen - 1]['nextUnit']
        return(next_ID)

loadUnit('1')