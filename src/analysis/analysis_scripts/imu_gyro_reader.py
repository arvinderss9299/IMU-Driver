import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
from tf.transformations import euler_from_quaternion

b = bagreader('/home/arvinder/RSN/src/analysis/rosbag_data/15_minutes_data.bag')

imudata= b.message_by_topic(topic="/imu_data")
imudataread = pd.read_csv(imudata)
imudf = pd.DataFrame(imudataread, columns=["Time", "gyro.x", "gyro.y", "gyro.z"]).astype(float)
imudf["Time"] = (imudf["Time"] - imudf.at[0,"Time"])/60

gyro_x_mean = imudf["gyro.x"].mean()
gyro_y_mean = imudf["gyro.y"].mean()
gyro_z_mean = imudf["gyro.z"].mean()


gyro_x_stdv = imudf["gyro.x"].std()
gyro_y_stdv = imudf["gyro.y"].std()
gyro_z_stdv = imudf["gyro.z"].std()

print(f"Gyro X Mean = {gyro_x_mean} rad/sec \nGyro Y Mean =  {gyro_y_mean} rad/sec \nGyro Z Mean =  {gyro_z_mean} rad/sec")

print(f"Gyro X Std. Deviation = {gyro_x_stdv} rad/sec \nGyro Y Std. Deviation =  {gyro_y_stdv} rad/sec \nGyro Z Std. Deviation =  {gyro_z_stdv} rad/sec")


# For Gyro X
plot_gyro_x = imudf.plot("Time", "gyro.x", c ='red', label= "gyro_x at time t")
plt.title("gyro_x at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Gyro(rad/sec)")
plt.grid(True)
  
# For Gyro Y
plot_gyro_y = imudf.plot("Time", "gyro.y", c ='green', label= "gyro_y at time t")
plt.title("gyro_y at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Gyro(rad/sec)")
plt.grid(True)

# For Gyro Z
plot_gyro_z = imudf.plot("Time", "gyro.z", c ='black', label= "gyro_z at time t")
plt.title("gyro_z at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Gyro(rad/sec)")
plt.grid(True)

plt.show()


