import json
from difflib import get_close_matches
import random

def load_data(dataset):
    with open(dataset,'r') as json_file:
        data = json.load(json_file)
        return data

def find_the_best_match(user_input, dict_1):
    dict_1_list = list(dict_1.keys())
    best_match = get_close_matches(user_input, dict_1_list, n=1, cutoff=0.6)
    return best_match

def save_new_data(new_database, file_path, old_input, new_input):
    new_database[old_input] = [new_input]

    with open(file_path,'w') as json_file:
        json.dump(new_database, json_file, indent=4)


print("welcome to chatbot_v1")

print("""
       _______
     _/       \_
    / |       | \\
   /  |__   __|  \\
  |__/((o| |o))\\__|
  |      | |      |
  |\\     |_|     /|
  | \\           / |
   \\| /  ___  \\ |/
    \\ | / _ \\ | /
     \\_________/
      _|_____|
 ____|_________|____
/                   \\  -- Hey human
""")


while True:

    dict_1 = load_data("database.json")
    user_input = input("You: ").lower()
    answer = find_the_best_match(user_input, dict_1)
    if answer:
        print("Chat bot v1: ",random.choice(dict_1[answer[0]]))

    else:
        print("Chat bot v1: I don't understand. Can you teach me how to answer this question?")
        new_user_input = input("Please enter a new answer for the bot to learn: ")
        new_answer = save_new_data(dict_1, "database.json", user_input, new_user_input)
        print("Chat bot v1: Great! Let's try again. Ask me the same questions")