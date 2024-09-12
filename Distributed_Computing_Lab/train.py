from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

## Load the data
cars = pd.read_csv('https://raw.githubusercontent.com/EviIius/DSBA6190/main/Distributed_Computing_Lab/mtcars.csv', sep=',')

## Split the data
# X, y = diabetes.data, diabetes.target
X = cars.drop('mpg', axis=1)
y = cars['mpg']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

## Train a regression model
model = LinearRegression()
model.fit(X_train, y_train)

## Predict Y-pred values
y_pred = model.predict(X_test)

## Print MSE
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Save the model
import joblib
joblib.dump(model, '/mnt/datalake/instructor/diabetes_model.pkl')
