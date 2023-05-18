from sklearn import preprocessing
import numpy

Xtrain = [] 
Xtest = []
f = open('test/Xtest.txt')
for line in f:
     line = line.replace("[", "")
     line = line.replace("]", "")
     line = line.replace(". ", ".0")
     nums = line.split(' ')
     nums[3] = nums[3].replace("\n", "")
     list = []
     for num in nums:
          list.append(float(num))
     Xtest.append(list)
X_test = numpy.array(Xtest)

f = open('train/Xtrain.txt')
for line in f:
     line = line.replace("[", "")
     line = line.replace("]", "")
     line = line.replace(". ", ".0")
     nums = line.split(' ')
     nums[3] = nums[3].replace("\n", "")
     list = []
     for num in nums:
          list.append(float(num))
     Xtrain.append(list)
X_train = numpy.array(Xtrain)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

f = open('test/X_test_scaled.txt', 'w')
for nums in Xtest:
    f.write(str(nums) + '\n')
f.close()

f = open('train/X_train_scaled.txt', 'w')
for nums in Xtrain:
    f.write(str(nums) + '\n')
f.close()


