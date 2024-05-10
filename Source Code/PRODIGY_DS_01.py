import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Age wise Electoral
plt.subplot(1,3,1)
age_wise_electoral = pd.read_csv('Age Wise Electoral.csv')

age_wise_electoral_x_axis = age_wise_electoral['Age Group']
age_wise_electoral_y_axis = age_wise_electoral['Vote Percent']

def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i]+0.3, y[i], ha='center')

plt.bar(age_wise_electoral_x_axis, age_wise_electoral_y_axis, edgecolor='black')

addlabels(age_wise_electoral_x_axis, age_wise_electoral_y_axis)

plt.title('Age wise Electoral in Maharashtra 2019')
plt.xlabel('Age Group')
plt.ylabel('Percent')

plt.tight_layout()

# PC Elections Maharashtra
plt.subplot(1,3,2)
PC = pd.read_csv('PC Elections Maharashtra.csv')
N = 5
width = 0.2

x_axis = np.arange(N)
pc_seats_BJP = PC['BJP']
pc_seats_INC = PC['INC']
pc_seats_SHS = PC['SHS']
pc_seats_NCP = PC['NCP']

plt.bar(x_axis, pc_seats_BJP, width, label = 'BJP', edgecolor='black', color = 'green')
plt.bar(x_axis+width, pc_seats_INC, width, label = 'INC', edgecolor='black', color = 'blue') 
plt.bar(x_axis+width*2, pc_seats_SHS, width, label = 'SHS', edgecolor='black', color = 'orange') 
plt.bar(x_axis+width*3, pc_seats_NCP, width, label = 'NCP', edgecolor='black', color = 'cyan') 

plt.title('PC Elections - Maharashtra')
plt.xlabel('Year')
plt.ylabel('Seats Won')
plt.xticks(x_axis+width+(width/2), PC['Year'])
plt.legend()

plt.tight_layout()

# EC Elections Maharashtra
plt.subplot(1,3,3)
EC = pd.read_csv('EC Elections Maharashtra.csv')
N = 5
width = 0.2

x_axis = np.arange(N)
ec_seats_BJP = EC['BJP']
ec_seats_INC = EC['INC']
ec_seats_SHS = EC['SHS']
ec_seats_NCP = EC['NCP']

plt.bar(x_axis, ec_seats_BJP, width, label = 'BJP', edgecolor='black', color = 'green') 
plt.bar(x_axis+width, ec_seats_INC, width, label = 'INC', edgecolor='black', color = 'blue') 
plt.bar(x_axis+width*2, ec_seats_SHS, width, label = 'SHS', edgecolor='black', color = 'orange') 
plt.bar(x_axis+width*3, ec_seats_NCP, width, label = 'NCP', edgecolor='black', color = 'cyan') 

plt.title('EC Elections - Maharashtra')
plt.xlabel('Year')
plt.ylabel('Seats Won')
plt.xticks(x_axis+width+(width/2), EC['Year'])
plt.legend()

plt.tight_layout()
plt.show()