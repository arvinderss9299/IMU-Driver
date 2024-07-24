import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
from tf.transformations import euler_from_quaternion

b = bagreader('/home/arvinder/RSN/src/analysis/rosbag_data/15_minutes_data.bag')

imudata= b.message_by_topic(topic="/imu_data")
imudataread = pd.read_csv(imudata)
imudf = pd.DataFrame(imudataread, columns=["Time", "acceleration.x", "acceleration.y", "acceleration.z"]).astype(float)
imudf["Time"] = (imudf["Time"] - imudf.at[0,"Time"])/60

acceleration_x_mean = imudf["acceleration.x"].mean()
acceleration_y_mean = imudf["acceleration.y"].mean()
acceleration_z_mean = imudf["acceleration.z"].mean()


acceleration_x_stdv = imudf["acceleration.x"].std()
acceleration_y_stdv = imudf["acceleration.y"].std()
acceleration_z_stdv = imudf["acceleration.z"].std()

print(f"Acceleration X Mean = {acceleration_x_mean} m/sec^2 \nAcceleration Y Mean =  {acceleration_y_mean} m/sec^2 \nAcceleration Z Mean =  {acceleration_z_mean} m/sec^2")

print(f"Acceleration X Std. Deviation = {acceleration_x_stdv} m/sec^2 \nAcceleration Y Std. Deviation =  {acceleration_y_stdv} m/sec^2 \nAcceleration Z Std. Deviation =  {acceleration_z_stdv} m/sec^2")

# For acceleration X
plot_acceleration_x = imudf.plot("Time", "acceleration.x", c ='red', label= "acceleration_x at time t")
plt.title("acceleration_x at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Acceleration(m/sec^2)")
plt.grid(True)
  
# For acceleration Y
plot_acceleration_y = imudf.plot("Time", "acceleration.y", c ='green', label= "acceleration_y at time t")
plt.title("acceleration_y at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Acceleration(m/sec^2)")
plt.grid(True)

# For acceleration Z
plot_acceleration_z = imudf.plot("Time", "acceleration.z", c ='black', label= "acceleration_z at time t")
plt.title("acceleration_z at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Acceleration(m/sec^2)")
plt.grid(True)

plt.show()
