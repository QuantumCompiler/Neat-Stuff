# import libraries
import numpy as np
import matplotlib.pyplot as plt

def logistic(v, x): #equation given to us
    return v*x

n = 1000000  # total number of points
v = np.linspace(0.0, 1.0, n) # range of variable
iterations = 100 # times function is iterated through

x = np.random.uniform(0.0, 1.0, n)  # initial Value for x_0, with range
for _ in range(iterations):  # iterating through function
    x = logistic(v, x) # updating x_n+1

fig = plt.figure(figsize=(10, 7.5)) # figure size
ax = plt.axes() # plot axes

ax.set_title(f"Bifurcation Diagram", fontsize=18) # set set title
ax.set_xlabel('Variable', fontsize=18) # x label of graph
ax.set_ylabel('$x_{n+1}$', fontsize=18) # y label of graph
ax.tick_params(axis='both', which='major', labelsize=18) # add ticks to graph
ax.set_xlim(0.0, 1.0) # set x bounds of graph
ax.set_ylim(0.0, 1.0) # set y bounds of graph

ax.plot(v, x, ',b', alpha=.5) # plot graph
plt.show() # show plot
