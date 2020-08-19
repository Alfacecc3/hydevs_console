#editme
import json
import random
import time
random.seed(time.time())
x=json.loads(open('json.json').read())

if x['OriginalIntent']['use_syns_output'] == 1:
    c=x['OriginalIntent']['samples']
else:
    c=['editme']

print(c[random.randint(0, len(c)-1)])
