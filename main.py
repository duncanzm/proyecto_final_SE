from flask import Flask, request
from logpy_rules import *
from collections.abc import Iterable
import json


app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    json_data = {}
    for key in request.json:
        try:
            json_data[int(key)] = int(request.json[key])
        except ValueError:
            pass  

    already_processed_resonants = []

    for key, value in json_data.items():
        failing_frecuencies = {}
        if key not in already_processed_resonants:
            resonants_to_process = give_me_resonantes(int(key))
            for resonant in resonants_to_process:
                print(value_within_range(json_data.get(resonant)))
                if not value_within_range(json_data.get(resonant)):
                    failing_frecuencies[resonant]=json_data.get(resonant)
                    print (failing_frecuencies)
                    print (len(failing_frecuencies))
                already_processed_resonants.append(resonant)
            if (failing_frecuencies):
                measure_category = categorize_measure(failing_frecuencies,len(resonants_to_process))
                break
    return {
        "speakerStatus": measure_category, 
        "failingFrecuencies":list(failing_frecuencies.keys())
    }

if __name__ == '__main__':
    app.run(port=8000, debug=True)
