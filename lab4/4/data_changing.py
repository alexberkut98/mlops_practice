import pandas as pd
data = pd.read_csv('datasets/titanic.csv',delimiter=',')
new_data = data[['Pclass','Sex','Age']]
new_data.to_csv('datasets/new_data.csv',index=False)
