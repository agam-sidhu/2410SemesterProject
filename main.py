import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# read the csv file
faithful = pd.read_csv('oldfaithful.csv')

# select the two columns we need
time_between_eruptions=faithful['Eruption'].values.reshape(-1, 1)
length_of_eruptions=faithful['Waiting']

sns.scatterplot(data = faithful, x = time_between_eruptions.flatten(), y = length_of_eruptions)

# use matplotlib to show the scatterplot
plt.xlabel("Time Between Eruptions (minutes)")
plt.ylabel("Length of Eruption (minutes)")
plt.title("Scatter Plot: Time Between Eruptions vs. Length of Eruption")

# set the model to a Linear Regression and fit the model to the data
model = LinearRegression()
model.fit(time_between_eruptions, length_of_eruptions)

predictions = model.predict(time_between_eruptions)
plt.plot(time_between_eruptions.flatten(), predictions, "red")
plt.show()

# meanSquaredError = mean_squared_error(y_test, predictions)
# print(f'Mean Squared Error: {meanSquaredError}')