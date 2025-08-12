import json

# Create a JSON from a Python dict
template_name = {
    "Story": "A story goes here",
    "Questions": "Questions go here",
    "Correct Answers": "Correct answers go here"
}

json_data = json.dumps(template_name)
print(template_name)


# Write data to a JSON file
with open('test.json', 'w') as file:
    json.dump(template_name, file)

print("JSON data has been stored")


# Reading a JSON from a file
with open('test.json', 'r') as file:
    loaded_test = json.load(file)

# Displaying the loaded data
print("Loaded JSON data:")
print(loaded_test)