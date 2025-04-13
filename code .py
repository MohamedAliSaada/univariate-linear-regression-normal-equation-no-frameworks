import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from pprint import pprint

#load the data and normalization it 
df = pd.read_csv('ex_1.csv')
columns_in_df= list(df.columns)     #this becouse i may have alot of features that i can not deal with one by one .
for column in columns_in_df
    df[column] = (df[column] - df[column].mean()) df[column].std() 

#training data in  row vector shape (mX1)
x= df['time']
x=np.array(x).reshape(len(x),1)    #(-1,1) do the same as you do .
y=df['el_power']
y=np.array(y).reshape(-1,1)

#add bias term to my x vector and make it (m,2) size
bias_vector =  np.ones(len(x)).reshape(-1,1)
x_origin = x
x= np.c_[bias_vector,x]   #add bias first mean we have b at first then w befor it .

#use normal equation to get w and b values now. solution = (Xᵀ X)⁻¹ Xᵀ y
solution =  np.linalg.inv(x.T @ x) @ x.T @ y

#results of w and b 
solution.shape
b= solution[0][0]
w=solution[1][0]
print(fModel y = {w}  x + {b})

# Predict values
y_pred = x @ solution  # shape (m, 1)
print(x.shape)
# Plot
plt.figure(figsize=(8, 5))
plt.scatter(x_origin, y, label='Normalized Data')
plt.plot(x_origin, y_pred, color='red', label='Prediction (Normal Equation)')
plt.title('Univariate Linear Regression (Normal Equation)')
plt.xlabel('Normalized Time')
plt.ylabel('Normalized El_Power')
plt.legend()
plt.grid(True)
plt.show()