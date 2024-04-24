from flask import Flask, request
from logpy_rules import *
from collections.abc import Iterable
import json
import base64


app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():

# Decode the Base64 string

    decoded_json = json.loads(base64.b64decode(request.data.decode("utf-8")).decode("utf-8"))
    measure_category = "OK"
    failing_frecuencies = {}

    json_data = {}
    for key in decoded_json[0]:
        try:
            json_data[int(key)] = int(decoded_json[0][key])
        except ValueError:
            pass  
    already_processed_resonants = []

    print (json_data)
    for key, value in json_data.items():
        failing_frecuencies = {}
        if key not in already_processed_resonants:
            resonants_to_process = give_me_resonantes(int(key))
            for resonant in resonants_to_process:
                if not value_within_range(json_data.get(resonant)):
                    failing_frecuencies[resonant]=json_data.get(resonant)
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
