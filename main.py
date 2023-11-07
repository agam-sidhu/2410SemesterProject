import pandas as pd
import matplotlib.plyplot as plt
import seaborn as sns 

faithful = pd.read_csv('oldfaithful.csv')
time_between_eruptions=faithful['Eruption']
length_of_eruptions=faithful['Waiting']
sns.scatterplot(data = faithful, x = time_between_eruptions, y = length_of_eruptions)
#this is my test commit
#test commit
plt.xlabel("Time Between Eruptions (minutes)")
plt.ylabel("Length of Eruption (minutes)")
plt.title("Scatter Plot: Time Between Eruptions vs. Length of Eruption")