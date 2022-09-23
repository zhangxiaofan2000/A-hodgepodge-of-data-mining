import xgboost as xgb
from sklearn.metrics import mean_absolute_error

import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import Dataset
dataset = pd.read_csv('./data/training_data.csv')
X_train=dataset.iloc[:,0:1].values
y_train=dataset.iloc[:,5].values

test_data = pd.read_csv('./data/testing_data.csv')
X_005=test_data.iloc[:,0:1].values
y_005=test_data.iloc[:,5].values

def xg_eval_mae(yhat,dtrain):
    y=dtrain.get_label()
    return 'mae',mean_absolute_error(np.exp(y),np.exp(yhat))



model = xgb.XGBRegressor()

model.fit(X_train, y_train)

# 当前循环次数
t = 40
y_pred  = model.predict(t)

t += 1
y_pred  = model.predict(t)

while (t < 165 and y_pred > 1.3):
    t += 1
    y_pred = model.predict(t)

rul = t - 40
print('rul :'+ f'{rul}')
from sklearn.metrics import r2_score
import sklearn
import math
y_pred = model.predict(X_005)
R2 = r2_score(y_005, y_pred)
mse = sklearn.metrics.mean_squared_error(y_005, y_pred)
rmse = math.sqrt(mse)
print(f'R2={R2},mse={mse},rmse={rmse}')
# Visualize
initial_capacity = model.predict(0)
print(initial_capacity)
threshold = initial_capacity * 0.7

# Visual results training
plt.figure()
plt.plot(0, 1.68, color='yellow')
plt.plot(X_005, y_005, color='red')
plt.plot(X_005, y_pred, color='blue')
plt.axhline(threshold, color='yellow', linestyle='--')
plt.title('RUL Prediction')
plt.xlabel('Cycle')
plt.ylabel('Capacity (Ah)')
plt.show()