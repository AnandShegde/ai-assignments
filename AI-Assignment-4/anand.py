import numpy as np
import matplotlib.pyplot as plt
def plot_tour(tour,points,title= "Tour"):
    points= np.array(points)
    plt.scatter(points[:,0],points[:,1])
    for x in range(len(tour)-1):
        i = tour[x]
        j = tour[x+1]
        plt.plot([points[i,0],points[j,0]],[points[i,1],points[j,1]])
    i= tour[0]
    j= tour[-1]
    plt.plot([points[i,0],points[j,0]],[points[i,1],points[j,1]])
    plt.title(title)
    plt.show()