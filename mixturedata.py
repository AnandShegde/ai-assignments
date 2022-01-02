import numpy as np
import time
import matplotlib.pyplot as plt
from numpy import random
from numpy.core.fromnumeric import shape
import seaborn as sns
import scipy.stats as stat

# generate some data of guassian distribution

mu1,sigma1= 0,1
size1=(50,1) # lamda1= 0.33 since i used 50/150


mu2, sigma2= 4,0.5 
size2=(100,1)# lamda2= 0.67 

data1= np.random.normal(mu1,sigma1,size=size1)
data2= np.random.normal(mu2,sigma2,size=size2)


data3 = np.append(data1,data2,axis=0)
# print(data3)

# sns.kdeplot(data=data3)
# # sns.histplot(data= data3, bins=30,kde=True)
# plt.show()


# em algorithm

#initialize things
mu= np.random.uniform(low=2,high=3,size=(2,1))
sigma=np.random.uniform(low=2,high=3,size=(2,1))
lamda= np.random.rand(2,1)
lamda[1,0]=1-lamda[0,0]
n= data3.shape[0]
mu=np.array([[0 ],[3]])
sigma=np.array( [[0.9], [0.4]])
lamda=np.array([[0.30] ,[0.7]])
gamma = np.zeros(shape=(data3.shape[0],2))
gamma1= np.zeros(shape=(data3.shape[0],1))
gamma2 = np.zeros(shape=(data3.shape[0],1))

gamma1=lamda[0,0]*(stat.norm(mu[0,0],sigma[0,0]).pdf(data3))
gamma2= (lamda[1,0]*stat.norm(mu[1,0],sigma[1,0]).pdf(data3))

gamma= np.append(gamma1/(gamma1+gamma2), gamma2/(gamma1+gamma2),axis=1)
# gamma= gamma.reshape((150,2))
print(mu,sigma,lamda,shape(gamma))



# updating the parameters
for _ in range(500):
    gammasum= np.sum(gamma,axis=0,keepdims=True)
    print(f"gammasum={shape(gammasum)}")
    print(f"gamma ={shape(gamma)} ")
    print(gammasum)
    print(f"mu size ={shape(mu)} ")
    

    
    
    mu[0,0] =np.sum( np.multiply(gamma[:,0].reshape(150,1),data3),axis=0)/gammasum[0,0]
    mu[1,0] =np.sum( np.multiply(gamma[:,1].reshape(150,1),data3),axis=0)/gammasum[0,1]
    # print(f"mu={shape(mu)}")

    lamda= np.transpose((1/n)*(np.sum(gamma,axis=0,keepdims=True)))
    # print(f"lamda= {shape(lamda)}")
    # print(f"sigma= {shape(sigma)}")
    sigma[0,0] = np.sum(np.multiply(gamma[:,0].reshape(150,1),(data3-sigma[0,0])**2),axis=0,keepdims=True)/gammasum[0,0]
    sigma[1,0] = np.sum(np.multiply(gamma[:,1].reshape(150,1),(data3-sigma[1,0])**2),axis=0,keepdims=True)/gammasum[0,1]
    gamma1= (lamda[0,0]*stat.norm(mu[0,0],sigma[0,0]).pdf(data3))
    gamma2= (lamda[1,0]*stat.norm(mu[1,0],sigma[1,0]).pdf(data3))
    gamma= np.append(gamma1/(gamma1+gamma2), gamma2/(gamma1+gamma2),axis=1)
    if(_%10==0):
        print(f"sigma= {sigma} \nlamda= {lamda} \nmu= {mu} ")
        time.sleep(2)
print(f"\n\n\nsigma= {sigma} lamda= {lamda} mu= {mu} \n\n\n")

