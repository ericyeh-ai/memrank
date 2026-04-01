import json

with open("data/synthetic_conversations.json", "r") as f:
    dataset = json.load(f)

print(f"Loaded {len(dataset)} samples")

for sample in dataset:
    print(sample["id"])
    print("Question:", sample["question"])
    print("Ground truth:", sample["ground_truth"])
    print("-" * 40)