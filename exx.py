import json

print(json.loads(open("/config.json").read())["meow"], sep="\n")