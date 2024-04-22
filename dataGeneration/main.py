from AmplitudeModifier import AmplitudeModifier
import pandas as pd
import random
from tqdm import tqdm
import base64


frequencies = ["20", "30", "40", "50", "60", "80", "100", "120", "150", "200", "300", "400", "500", "600", "800", "1000", "1200", "2000", "3000", "4000", "5000", "6000", "8000", "10000", "12000", "20000", "Ground-truth"]

resonances = [
    ["20", "40", "80"],
    ["30", "60", "120"],
    ["50", "100", "200", "400", "800"],
    ["150", "300", "600", "1200"],
    ["500", "1000", "2000", "4000", "8000"],
    ["3000", "6000", "12000"],
    ["5000", "10000", "20000"]
]

normalCount = 0
quietCount = 0
loudCount = 0


def getProbabilisticState(probability: float = 0.9244):
    probability = 0.2
    tailSize = (1 - probability) / 2
    leftTail = tailSize
    rightTail = 1 - tailSize
    return leftTail, rightTail

def getCurrentProbabilisticState():
    seed = random.random()
    leftTail, rightTail = getProbabilisticState()
    if seed < leftTail:
        return "quiet"
    elif seed > rightTail:
        return "loud"
    else:
        return "normal"

def createRandomData():
    global normalCount, quietCount, loudCount
    data = {}
    for frecuency in frequencies:
        data[frecuency] = AmplitudeModifier.normal()

    currentProbabilityState = getCurrentProbabilisticState()
    if currentProbabilityState == "normal":
        normalCount = normalCount + 1
        data["Ground-truth"] = "Normal"
        return data
    random_resonance = random.choice(resonances)


    readingError = random.randint(0, 99)
    if readingError < 5:
        faultyResonance = random.choice(random_resonance)
        data[faultyResonance] = AmplitudeModifier.normal() * 10
        data["Ground-truth"] = "Faulty"

    else:
        if currentProbabilityState == "quiet":
            modifier = AmplitudeModifier.quiet
            data["Ground-truth"] = "Quiet"
            quietCount = quietCount + 1
        elif currentProbabilityState == "loud":
            modifier = AmplitudeModifier.loud
            data["Ground-truth"] = "Loud"
            loudCount = loudCount + 1

        for affectedResonance in random_resonance:
            data[affectedResonance] = modifier()
    return data

def saveToFile(df):
    df.to_csv("data.csv", index=False)
    print("Data saved to data.csv")

def saveToMultipleFiles(df):
    for index, row in df.iterrows():
        frequencies = row.iloc[:-1]
        type = row.iloc[-1]
        result = pd.DataFrame([frequencies])
        name = f"{index}_{type}.ssa"

        json = result.to_json(orient="records")
        json_bytes = json.encode("utf-8")
        base64_bytes = base64.b64encode(json_bytes)
        base64_string = base64_bytes.decode('utf-8')
        folder = 'ssa_files'
        with open(f"{folder}/{name}", "w") as f:
            f.write(base64_string)


    print('Files created')

if __name__ == '__main__':
    selection = ''
    while selection not in ["q"]:
        selection = input("Generate batch data or single files? (b/s): (press q for quit)")
        if selection == "q":
            break
        rows_to_generate = int(input("How many speaker emulations do you want to generate?"))
        df = pd.DataFrame()
        for i in tqdm(range(rows_to_generate)):
            df = pd.concat([df, pd.DataFrame([createRandomData()])], ignore_index=True)
        print(df)
        print("Quiet: ", quietCount)
        print("Normal: ", normalCount)
        print("Loud: ", loudCount)
        if selection == "b":
            saveToFile(df)
        elif selection == "s":
            saveToMultipleFiles(df)
        elif selection == "q":
            print("Goodbye!")
        else:
            print("Invalid selection")
            continue


