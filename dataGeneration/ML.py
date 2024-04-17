import tensorflow as tf
import pandas as pd

def loadData():
    data = pd.read_csv("data.csv")
    return data

def printData(data):
    print(data.head())

