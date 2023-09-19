import re
import json

# Read the original format from a text file
with open('QA_Eminem.txt', 'r') as file:
    original_format = file.read()

# Splitting the original format into individual Q&A pairs
pairs = original_format.strip().split(' Q: ')

# Creating the target JSON structure
train_json = []

for pair in pairs:
    qa_parts = pair.split(' A: ')

    if len(qa_parts) == 2:
        user_text = qa_parts[0].strip()
        assistant_text = qa_parts[1].strip()

        target_json = {
        "messages": [
            {"role": "system", "content": "You are chatbot who answers question with rapper's tone and rythme."}
        ]
        }
        target_json["messages"].append({"role": "user", "content": user_text.strip()})
        target_json["messages"].append({"role": "assistant", "content": assistant_text.strip()})
        train_json.append(target_json)

with open('QA_Eminem_train.jsonl', 'w') as jsonl_file:
    for item in train_json:
        jsonl_file.write(json.dumps(item) + '\n')