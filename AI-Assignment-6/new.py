import imp
from statistics import mode
from tkinter.messagebox import NO
import pandas as pd
import sklearn as sk
from sklearn import svm
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv("spambase.data.csv",header=None)

X = data.iloc[:,:-1]
scale =StandardScaler()
X=scale.fit_transform(X)


Y = data.iloc[:,-1]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)



for i in range(5,15):
    model = svm.SVC(kernel="poly",C=i,degree=2)
    model.fit(X_train,Y_train)
    # print(f"Guassian Kernal i={i} ")
    # print(f"Training set accuracy {model.score(X_train,Y_train)}")
    print(model.score(X_test,Y_test))
    #print(model.score(X_train,Y_train))
    # print(f"Test Set accuracy {model.score(X_test,Y_test)}")
    # print("#"*40)

exit()
print('\n\n')
  

for i in range(20,40,2):
    model = svm.SVC(kernel="linear",C=i)
    model.fit(X_train,Y_train)
    print(f"linear Kernal c={i}")
    print(f"Training set accuracy {model.score(X_train,Y_train)}")
    model.score(X_test,Y_test)
    print(f"Test Set accuracy {model.score(X_test,Y_test)}")
    print("#"*40)
print('\n\n')

for i in range(5,15):
    model = svm.SVC(kernel="poly",C=i,degree=2)
    model.fit(X_train,Y_train)
    print(f"quadratic kernal c={i} ")
    print(f"Training set accuracy {model.score(X_train,Y_train)}")
    print(f"Test Set accuracy {model.score(X_test,Y_test)}")
    print("#"*40)




