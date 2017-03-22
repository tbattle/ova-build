import json
import os

print('Start...')
print()

# Open JSON file
jsonFile = open("config.json", "r") 
data = json.load(jsonFile)
jsonFile.close()

## Change JSON data
data['httpEndpoints'][0]['authEnabled'] = False
print('authEnabled = False')

## Save JSON file
jsonFile = open("config.json", "w+")
jsonFile.write(json.dumps(data))
jsonFile.close()

print()
print('...End')