import yaml

f = open("../config/data.yaml", encoding="utf8")
data = yaml.safe_load(f)
print(data['person'])

