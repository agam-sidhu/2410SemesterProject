import pandas as pd
import seaborn as sns 
import matplotlib.plyplot as plt

faithful = pd.read_csv('oldfaithful.csv')


sns.scatterplot(data = faithful, x = 'time between eruptions', y = 'length of eruptions')
#this is my test commit
#test commit