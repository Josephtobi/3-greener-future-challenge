import pandas as pd
import os
import sys

# Add the root folder to the system path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from submission import predict_temperatures

base_path = os.path.dirname(__file__)
test_path = os.path.join(base_path, 'test.csv')

test = pd.read_csv(test_path)

# Select features and target
features = test.drop(columns=['LandAverageTemperature', 'LandAndOceanAverageTemperature'])
target = test['LandAverageTemperature']

# Predict the temperatures
predictions = predict_temperatures(len(test))

# Calculate the root mean squared error
rmse = ((predictions['LandAverageTemperature'] - target) ** 2).mean() ** 0.5
print(f'Root Mean Squared Error: {rmse}')