import json
import tiktoken

# Token counting functions
encoding = tiktoken.get_encoding("cl100k_base")

def num_tokens_from_messages(messages, tokens_per_message=3):
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

dataset = []

# Open the JSONL file and read each line
with open("QA_Eminem_train.jsonl", "r") as jsonl_file:
    for line in jsonl_file:
        # Parse each line as a JSON object and append it to the dataset list
        data = json.loads(line)
        dataset.append(data)
        
total_tokens = 0
for ex in dataset:
    messages = ex["messages"]
    total_tokens += num_tokens_from_messages(messages)
    
print("Token counts:", total_tokens)
print("3 ipochs:", total_tokens*3)
print("Cost: $", total_tokens*3*0.008/1000)