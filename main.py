import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import PIL
import os
my_path = '/home/eo/Desktop/'
my_file = 'y.csv'
y_vals = genfromtxt(my_path+my_file, delimiter=',')
y_array=np.array(y_vals)
# Remove NaN values
y_result = y_array[np.logical_not(np.isnan(y_array))]
# Determine min and max Y values to identify range
y_min = np.min(y_result)
y_max = np.max(y_result)
# Subtract max-min to get range (smaller value is higher up in tank)
y_range = y_max-y_min
# Multiply by .33333 to determine 1/3 length of y_range
zone_size = y_range*.33333
# Define top zone cut-off y position
top_zone = y_min + zone_size
# Define minute intervals. Video was recorded at 60 fps. Therefore, one minute is 3600 frames
min1 = y_result[0:3600]
min2 = y_result[3601:7200]
min3 = y_result[7201:10800]
min4 = y_result[10801:14400]
min5 = y_result[14401:18000]

#Part 1: Determining number of top zone entries by test minute
plt.gca().invert_yaxis()
plt.plot(min1, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min1)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute1") #set the title of the graph
plt.savefig(my_path+'Minute_1.tif')
plt.show()

plt.plot(min2, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min2)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute2") #set the title of the graph
plt.savefig(my_path+'Minute_2.tif')
plt.show()

plt.plot(min3, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min3)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute3") #set the title of the graph
plt.savefig(my_path+'Minute_3.tif')
plt.show()

plt.plot(min4, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min4)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute4") #set the title of the graph
plt.savefig(my_path+'Minute_4.tif')
plt.show()

plt.plot(min5, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min5)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute5") #set the title of the graph
plt.savefig(my_path+'Minute_5.tif')
plt.show()

#Part 2: Determining time in top zone
# Isolate only the frames, per test minute, for which the fish is present within the top zone.
min1_top = min1[min1<top_zone]
min2_top = min2[min2<top_zone]
min3_top = min3[min3<top_zone]
min4_top = min4[min4<top_zone]
min5_top = min5[min5<top_zone]
# Count the number of top zone frames per test minute.
min1_size = np.size(min1_top)
min2_size = np.size(min2_top)
min3_size = np.size(min3_top)
min4_size = np.size(min4_top)
min5_size = np.size(min5_top)
# Divide each minute by 60 (fps) to determine top zone time in seconds.
min1_time = min1_size/60
min2_time = min2_size/60
min3_time = min3_size/60
min4_time = min4_size/60
min5_time = min5_size/60
# Convert these to csv for file output
import pandas as pd
results_header=('Min_1','Min_2','Min_3','Min_4','Min_5')
results=(min1_time, min2_time, min3_time, min4_time, min5_time)
dict= {'Test_Minute':results_header, 'Top_Zone_Time(sec)':results}
df = pd.DataFrame(dict)
df.to_csv('/home/eo/Desktop/results.csv')
