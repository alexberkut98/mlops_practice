import numpy
import pickle

Xtest = [] 
Ytest = []

f = open('test/Xtest.txt')
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
     Xtest.append(list)
Xtest = numpy.array(Xtest)

f = open('test/Ytest.txt')
for line in f:
     line = line.replace("\n", "")
     for num in line:
        Ytest.append(float(num))
Ytest = numpy.asarray(Ytest)

 # Load from file 
with open('pickle_model.pkl', 'rb') as file: 
  pickle_model = pickle.load(file) 


score = pickle_model.score(Xtest, Ytest) 
print("Model test accuracy is: {0:.3f}".format(score)) 