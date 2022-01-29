# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:58:41 2022

@author: ADMIN
"""

from copy import deepcopy
from dis import dis
from math import dist
from turtle import distance
import numpy as np
import matplotlib.pyplot as plt
import time,sys,random

def plot_tour(tour,points,title= "Tour"):
    
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
    plt.savefig(f"{title}.jpg")
    
    
if __name__== "__main__":
    #points= {0: 27, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 28: 26, 29: 28, 30: 29, 31: 30, 32: 31, 33: 32, 34: 33, 35: 34, 36: 35, 37: 36, 38: 37, 39: 38, 40: 39, 41: 40, 42: 41, 43: 42, 44: 43, 45: 44, 46: 45, 47: 46, 48: 47, 49: 48, 50: 49, 51: 50, 52: 51, 53: 52, 54: 53, 55: 54, 56: 55, 57: 56, 58: 57, 59: 58, 60: 59, 61: 60, 62: 61, 63: 62, 64: 63, 65: 64, 66: 65, 67: 66, 68: 67, 69: 68, 70: 69, 71: 70, 72: 71, 73: 72, 74: 73, 75: 74, 76: 75, 77: 76, 78: 77, 79: 78, 80: 79, 81: 80, 82: 81, 83: 82, 84: 83, 85: 84, 86: 85, 87: 86, 88: 87, 89: 88, 90: 89, 91: 90, 92: 91, 93: 92, 94: 93, 95: 94, 96: 95, 97: 96, 98: 97, 99: 98, 27: 99}
    plot_tour(points)