from pyDOE import *
import json
import sys

with open('param_ranges.json') as json_file:
    param_ranges = json.load(json_file)
    items = lhs(len(param_ranges), samples=int(sys.argv[1]), criterion='center')
    param_sets = []
    for item in items:
        n = 0
        param_set = {}
        for param in item:
            value = param_ranges[n]['from'] + (param * (param_ranges[n]['to'] - param_ranges[n]['from']))
            param_set[param_ranges[n]['name']] = value
            n = n + 1
        param_sets.append(param_set)
    dumped = json.dumps(param_sets)
    path = 'param_sets.json'
    with open(path, 'w') as f:
        json.dump(param_sets, f)
