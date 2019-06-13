import yaml

with open("config.yaml", 'r') as stream:
    res = yaml.safe_load(stream)