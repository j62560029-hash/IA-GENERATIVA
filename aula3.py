import numpy as np
from sklearn .tree import DecisionTreeClassifier

# y = f(x)

x = np.array([
    [1,5],
    [2,4],
    [3,3],
    [4,1],
    [5,0],
])

y = np.array([1,1,1,0,0])
modelo = DecisionTreeClassifier()
modelo.fit(x,y)
print(modelo.predict([[2,10]]))