import pandas as pd
new_data = pd.read_csv('datasets/new_data.csv',delimiter=',')
new_data['Age'] = new_data['Age'].fillna(new_data['Age'].mean())
new_data.to_csv('datasets/new_data.csv',index=False)
