import json
import sys

filename = sys.argv[1]
try:
    data = json.load(open(filename))
    label = data.get('label', '')
    if isinstance(label, dict):
        import itertools
        label = next(itertools.chain.from_iterable(label.values()), '')
    print(label)
except:
    print('')
    