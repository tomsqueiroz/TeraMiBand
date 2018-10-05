import pandas as pd
from datetime import datetime


class SleepCicle:
    def __init__(self, duration, deepness):
        self.duration = duration
        self.deepness = deepness

class Sleep:
    def __init__(self, sleepCiclesDataFrame, initialTime, endTime):
        self.sleepCiclesDataFrame = sleepCiclesDataFrame
        self.initialTime = initialTime
        self.endTime = endTime


def initializePandasWithCSV():
    headersNames = ['Index', 'StartTime', 'EndTime', 'AwakeMinutes', 'DeepMinutes', 'LightMinutes', 'SleepCicleString', 'asd', 'assd']
    data = pd.read_csv("dbFernando.csv", header=None, names=headersNames)
    data = data.drop(data.columns[8], axis=1)
    data = data.drop(data.columns[7], axis=1)
    return data


def parseSleepCicleString( sleepCicleString ):
    time = ''
    listSleepCicles = list()
    for i in range(0, len(sleepCicleString)):
        if sleepCicleString[i] != 'L' and sleepCicleString[i] != 'D' and sleepCicleString[i] != 'A':
            time = time + sleepCicleString[i]
        else:
            deepness = sleepCicleString[i]
            listSleepCicles.append(SleepCicle(int(time), deepness))
            time = ''
    return listSleepCicles


def createSleepList( data ):
    SleepList = list()
    for index, row in data.iterrows():
       SleepCicleStringDataFrame = pd.DataFrame.from_records(createSleepCicleStringList(parseSleepCicleString(row['SleepCicleString'])))
       SleepList.append(Sleep(SleepCicleStringDataFrame, convertTimeStamptoMinutes(row['StartTime']), convertTimeStamptoMinutes(row['EndTime'])))
    return SleepList

def convertTimeStamptoMinutes( timestamp ):
    dateandtime = datetime.utcfromtimestamp(timestamp)
    return dateandtime


def createSleepCicleStringList( listSleepCicles ):
    SleepCicleStringList = list()
    for i in range(0, len(listSleepCicles)-1):
        for j in range(0, listSleepCicles.__getitem__(i).duration):
            SleepCicleStringList.append(deepnessToString(listSleepCicles.__getitem__(i).deepness))
    return SleepCicleStringList


def deepnessToString( deepness ):
    if deepness == 'L':
        return [11,0,0]
    if deepness == 'D':
        return [0,11,0]
    if deepness == 'A':
        return [0,0,11]


data = initializePandasWithCSV()
sleepList = createSleepList(data)
print(sleepList)
x = 1


