import pandas as pd
import numpy as np

Accounts_Group = pd.DataFrame({'Account': ['A1','A2','A3']})
groups = np.array([['g1','g2'],['g3','g4'],['g1','g2','g3']])
Accounts_Group["Group"] = groups.tolist()
key_values = pd.DataFrame({'ID': ['1','2','3','4','5'],'Key': ['g1','g2','g3','g4','g5']})
keys = key_values.set_index('Key')['ID']
ag = Accounts_Group.explode('Group')
updated = ag['Group'].map(keys).groupby(level=0).agg(list)
output = Accounts_Group.assign(Group=updated)
print(output)
