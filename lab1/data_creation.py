from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
 
# Load and split data 
data = load_iris() 
Xtrain, Xtest, Ytrain, Ytest = train_test_split(data.data, data.target, test_size=0.3, random_state=4) 
f = open('test/Xtest.txt', 'w')
for nums in Xtest:
    f.write(str(nums) + '\n')
f.close()

f = open('train/Xtrain.txt', 'w')
for nums in Xtrain:
    f.write(str(nums) + '\n')
f.close()

f = open('test/Ytest.txt', 'w')
for nums in Ytest:
    f.write(str(nums) + '\n')
f.close()

f = open('train/Ytrain.txt', 'w')
for nums in Ytrain:
    f.write(str(nums) + '\n')
f.close()
