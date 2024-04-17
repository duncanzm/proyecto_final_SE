import tensorflow as tf
import pandas as pd

def loadData():
    data = pd.read_csv("data.csv")
    return data

def printData(data):
    print(data.head())

class_names = {
            "Quiet": 0,
            "Normal": 1,
            "Loud": 2,
            "Faulty": 3,
            "South": 4,
            "South West": 5,
            "West": 6,
            "North West": 7}