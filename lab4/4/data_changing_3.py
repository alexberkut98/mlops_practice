import pandas as pd
new_data = pd.read_csv('datasets/new_data.csv',delimiter=',')
new_data_encoded = pd.get_dummies(new_data.Sex,prefix='Sex')
final_data = new_data.join(new_data_encoded)
final_data.to_csv('datasets/new_data.csv',index=False)
