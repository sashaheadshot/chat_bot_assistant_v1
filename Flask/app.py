import time
from flask import Flask, request, render_template, jsonify
import json
from difflib import get_close_matches
import random

app = Flask(__name__)

def load_data(dataset):
    with open(dataset,'r') as json_file:
        data = json.load(json_file)
        return data

def find_the_best_match(user_input, dict_1):
    dict_1_list = list(dict_1.keys())
    best_match = get_close_matches(user_input, dict_1_list, n=1, cutoff=0.7)
    return best_match

def save_new_data(new_database, file_path, old_input, new_input):
    new_database[old_input] = [new_input]
    with open(file_path,'w') as json_file:
        json.dump(new_database, json_file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").lower()
    dict_1 = load_data("database.json")
    time.sleep(0.5)
    answer = find_the_best_match(user_input, dict_1)

    if answer:
        bot_response = random.choice(dict_1[answer[0]])
        return jsonify({"response": bot_response})
    else:
        return jsonify({"response": "I don't understand. Please teach me how to respond to you."})

@app.route('/learn', methods=['POST'])
def learn():
    data = request.json
    question = data.get("question", "").lower()
    answer = data.get("answer", "")
    dict_1 = load_data("database.json")
    save_new_data(dict_1, "database.json", question, answer)
    return jsonify({"response": "Thanks for teaching me! Ask me the same question again."})

if __name__ == "__main__":
    app.run(debug=True)
