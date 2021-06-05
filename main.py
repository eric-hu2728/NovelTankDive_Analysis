import numpy as np
from numpy import genfromtxt
y_vals = genfromtxt('/home/eo/Desktop/test_Y_position_data.csv', delimiter=',')
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
# Print 'er out
print('min1:',min1_time,'min2:',min2_time,'min3:',min3_time,'min4:',min4_time,'min5:',min5_time)