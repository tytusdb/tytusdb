import numpy as np
import pandas as pd


a = np.zeros((4,3))

print(a)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]   

print(a.shape)
# (4, 3) # dimensiones de matriz en forma de tupla


print(np.insert(a, a.shape[0], np.array((20, 20, 20)), 0)) # 0 o tambien axis=0
# se agrega a la ultima fila a.shape[0]
# para denotar fila se usa cero (0) axis = 0
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [20. 20. 20.]]


print(np.insert(a, a.shape[1], np.array((10, 10, 10, 10)), 1)) 
# 1 o tambien axis=1
# se agrega a la ultima columna a.shape[1]
# para denotar columna se usa uno (1) axis = 1
# [[ 0.  0.  0. 10.]
#  [ 0.  0.  0. 10.]
#  [ 0.  0.  0. 10.]
#  [ 0.  0.  0. 10.]]


def unique_rows(a): 
    a = np.ascontiguousarray(a) 
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1])) 
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1])) 


va = np.array([[1, 1, 1], [2, 3, 3], [1, 1, 4], [5, 4, 4], [2, 3, 3]])
b = unique_rows(va) 
#print(b)
#z = np.group_by(va[:, 0]).split(va[:, 1])
#print(z)

data = {"Team": [1,2,3,4,4,4,4],
		"Pos": [100,200,300,400,400,500,500],
		"Age": [1,2,3,4,4,4,4]}
df = pd.DataFrame(data)
print(df)
print("aqui va ")
#df_new = df.groupby(['Team', 'Pos', 'Age']).agg({'Pos': ['sum', 'min', 'max']})
df_new = df.groupby(['Pos', 'Team', 'Age'],as_index=True)['Pos'].mean()
print(df_new)

df_new = df.groupby(['Pos', 'Team', 'Age'],as_index=True)['Pos'].count()
print(df_new)


df_new = df.groupby(['Pos', 'Team', 'Age'],as_index=True)['Pos'].max()
print(df_new)

df_new = df.groupby(['Pos', 'Team', 'Age'],as_index=True)['Pos'].min()
print(df_new)

df_new = df.groupby(['Pos', 'Team', 'Age'],as_index=True)['Pos'].sum()
print(df_new)

data = pd.DataFrame({'Student Name' : ['Anil', 'Musk','Bill'], 
                        'Class' : [1,2,2], 
                        'Age' : [6, 7, 8 ]})
output = data.groupby(data["Class"])
output.filter(lambda g: len(g) > 2)
print(data)
print(output)


a = np.array([[1,100]])
print(np.insert(a, a.shape[1], np.array((2)), 1)) 

ind = [1,2,3]
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
print(df.sort_values(by=['col1', 'col2']))
print(df.sort_values(by='col1', ascending=False))


dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
          ('Galahad', 1.7, 38)]
a = np.array(values, dtype=dtype)       # create a structured array
np.sort(a, order='height') 
a[::1].sort(order='height')
print(a)
'''
print()

# Orden por índice (fila):
print(df.sort_index())

print()

# Ordenar por índice (columna):
print(df.sort_index(axis=1, ascending=False))

print()

# Ordenar por los valores de la columna 'tres':
'''

arr2D = np.array([[11, 12, 13, 22], [21, 7, 23, 14], [31, 10, 33, 7]])
print(arr2D)
columnIndex = 1
# Sort 2D numpy array by 2nd Column
sortedArr = arr2D[arr2D[:,columnIndex].argsort()]
print('Sorted 2D Numpy Array')
print(sortedArr)
sort = arr2D[arr2D[:,columnIndex].sort()]
print(sort)