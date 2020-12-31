import pickle
from analizer.abstract import instruction as inst

with open("obj.pickle", "rb") as f:
    result = pickle.load(f)
# Imprime [1, 2, 3, 4].
for v in result:
    if isinstance(v, inst.Select) or isinstance(v, inst.SelectOnlyParams):
        r = v.execute(None)
        if r:
            list_ = r[0].values.tolist()
            labels = r[0].columns.tolist()
            querys.append([labels, list_])
        else:
            querys.append(None)
    else:
        r = v.execute(None)