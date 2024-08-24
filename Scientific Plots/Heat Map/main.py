'''Module Imports'''
import numpy as np
import matplotlib.pyplot as plt

'''Heat map example: '''
def trig(x,y): #Function to be plotted in the z
    return np.cos(x) * np.sin(y) #Cos(x) * Sin*y)

'''Scaling for x and y axis: '''
partition = 100 #Partition number
x = np.linspace(0, np.pi, partition) #X-Axis
y = np.linspace(0, np.pi, partition) #Y-Axis
amp = np.zeros((partition, partition)) #Amplitude

'''Matrix assembly of z axis values'''
for i in range(partition): #Column for loop
    for j in range(partition): #Row for loop
        amp[j,i] = trig(x[i], y[j]) #z axis value

'''Plotting'''
plt.figure() #Create figure
plt.contourf(x, y, amp, levels=300) #Create contour map
plt.title('Heat Map of z = Sin(y)*Cos(x)') #Plot title
plt.ylabel('Sin(y)') #y axis label
plt.xlabel('Cos(x)') #x axis label
plt.colorbar() #Color bar
plt.show() #Show plot
