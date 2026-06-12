#investimento de marketing


import numpy  as np
from sklearn.linear_model import LinearRegression
# investimento em mkt 1mil
X = np.array([[1],[2],[4],[5],[3]])
# vendas 
y =  np.array([2,8,4,6,5])



modelo = LinearRegression()


modelo.fit(X, y)



print(modelo.predict([[6]]))