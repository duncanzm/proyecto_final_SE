import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import os

def loadData():
    data = pd.read_csv("data.csv", header=0)
    return data

def printData(data):
    print(data.head())

class_names = {
            "Quiet": 0,
            "Normal": 1,
            "Loud": 2,
            "Faulty": 3}

reversed_class_names = {v: k for k, v in class_names.items()}

def save_model(model, model_name):
    model_path = f"models/{model_name}"
    model.save(model_path)
    print(f"Model saved to {model_path}")

def load_saved_model(model_name):
    model_path = f"models/{model_name}"
    model = tf.keras.models.load_model(model_path)
    print(f"Model loaded from {model_path}")
    return model

def train_new_model():
    datasetPercentageForTraining = 0.7
    datasetPercentageForTesting = 0.3

    data = loadData()
    dataCount = len(data)
    trainingCount = int(dataCount * datasetPercentageForTraining)
    testingCount = int(dataCount * datasetPercentageForTesting)

    trainingData = data.iloc[:, :26][:trainingCount]
    trainingLabels = data.iloc[:, 26][:trainingCount]

    testingData, testingLabels = get_test_data()

    #convert labels to numbers in class_names
    trainingLabels = trainingLabels.map(class_names)
    testingLabels = testingLabels

    model = keras.Sequential([
        keras.layers.Dense(26, activation='relu'),
        keras.layers.Dense(3),
        keras.layers.Dense(len(class_names), activation='softmax')
    ])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                metrics=['accuracy'])

    epocs = int(input("Enter number of epocs: "))
    model.fit(trainingData, trainingLabels, epochs=epocs)

    test_loss, test_acc = model.evaluate(testingData, testingLabels, verbose=2)

    print('\nTest accuracy:', test_acc)



    saveModel = input("Do you want to save the model? (y/n): ").strip().lower()
    if saveModel == 'y':
        model_name = input("Enter a name to save your model: ").strip()
        save_model(model, model_name)

    makePrediction(model, testingData, testingLabels)

def makePrediction(model, testingData, testingLabels):
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    predictions = probability_model.predict(testingData)

    slice = 70
    end = slice + 30
    selected_predictions = predictions[slice:end]
    selected_actual = testingLabels[slice:end]

    fig, axs = plt.subplots(5, 4, figsize=(15, 20))

    for i, ax in enumerate(axs.flat):
        # Plot the predicted values
        ax.bar(reversed_class_names.values(), selected_predictions[i], alpha=0.5, label='Predicted')
        # Plot the actual value
        actual_values = [0] * len(reversed_class_names)
        actual_values[selected_actual.iloc[i]] = 1
        ax.bar(reversed_class_names.values(), actual_values, alpha=0.5, label='Actual')
        ax.set_title(f'Prediction {i + 1}')
        ax.set_ylabel('Confidence')
        ax.set_ylim([0, 1])
        ax.legend()

    plt.tight_layout()
    plt.show()


def get_test_data():
    # This part is repeated from your train_new_model function
    datasetPercentageForTraining = 0.7
    datasetPercentageForTesting = 0.3
    data = loadData()
    dataCount = len(data)
    trainingCount = int(dataCount * datasetPercentageForTraining)
    testingCount = int(dataCount * datasetPercentageForTesting)


    testingData = data.iloc[:, :26][trainingCount:trainingCount + testingCount]
    testingLabels = data.iloc[:, 26][trainingCount:trainingCount + testingCount]
    testingLabels = testingLabels.map(class_names)

    return testingData, testingLabels

def list_models():
    return [f for f in os.listdir('models/') if os.path.isdir(os.path.join('models/', f))]

def check_gpu():
    print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
def main():
    choice = input("Do you want to load a saved model? (y/n): ").strip().lower()
    if choice == 'y':
        models = list_models()
        if not models:
            print("No saved models found.")
            return
        for idx, model_name in enumerate(models, 1):
            print(f"{idx}. {model_name}")
        selected_idx = int(input(f"Select a model (1-{len(models)}): "))
        selected_model_name = models[selected_idx - 1]
        model = load_saved_model(selected_model_name)
        testingImages, testingLabels = get_test_data()
        makePrediction(model, testingImages, testingLabels)

    else:
        train_new_model()



if __name__ == "__main__":
    check_gpu()
    main()

