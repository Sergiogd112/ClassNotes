import re
import json
import os
from pprint import pprint
import svgwrite
import networkx as nx
from matplotlib import pyplot as plt
import time

testdict = {'p':{
    'a': {
        'aa': {},
        'ab': {
            'aba': {},
            'abb': {
                'abba': {},
                'abbb': {}
            },
            'abc': {}
        },
        'ac': {

        }
    },
    'b': {
        'ba': {
            'baa': {

            },
            'bab': {}
        },
        'bb': {}
    }}
}


graph = nx.from_dict_of_dicts(testdict)

nx.draw(graph)
plt.draw()
plt.show()
