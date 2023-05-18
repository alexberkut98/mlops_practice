from sklearn.linear_model import LogisticRegression
import numpy
import pickle

model = LogisticRegression(C=0.1, 
max_iter=20, 
fit_intercept=True, 
n_jobs=3, 
solver='liblinear') 

X_train = [] 
Ytrain = []

f = open('train/Xtrain.txt')
for line in f:
     line = line.replace("[", "")
     line = line.replace("]", "")
     line = line.replace(". ", ".0")
     nums = line.split(' ')
     nums[3] = nums[3].replace("\n", "")
     list = []
     for num in nums:
          num = num.replace(",", "")
          list.append(float(num))
     X_train.append(list)
X_train = numpy.array(X_train)

f = open('train/Ytrain.txt')
for line in f:
     line = line.replace("\n", "")
     for num in line:
        Ytrain.append(float(num))
Ytrain = numpy.asarray(Ytrain)

model.fit(X_train, Ytrain) 

# Save to file in the current working directory 
pkl_filename = "pickle_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(model, file) 