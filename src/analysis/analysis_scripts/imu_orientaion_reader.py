import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
from tf.transformations import euler_from_quaternion
import math

b = bagreader('/home/arvinder/RSN/src/analysis/rosbag_data/15_minutes_data.bag')

imudata= b.message_by_topic(topic="/imu_data")
imudataread = pd.read_csv(imudata)
imudf = pd.DataFrame(imudataread, columns=["Time", "orientation.x", "orientation.y", "orientation.z", "orientation.w"]).astype(float)
imudf["Time"] = (imudf["Time"] - imudf.at[0,"Time"])/60

eulerdf = pd.DataFrame(columns=["Time", "roll", "pitch", "yaw"])

for ind in imudf.index:
    x = imudf["orientation.x"][ind]
    y = imudf["orientation.y"][ind]
    z = imudf["orientation.z"][ind]
    w = imudf["orientation.w"][ind]

    quaternion = (x,y,z,w)
    euler = euler_from_quaternion(quaternion)
    eulerdf.loc[ind] = [imudf["Time"][ind], math.degrees(euler[0]), math.degrees(euler[1]), math.degrees(euler[2])] 

roll_mean = eulerdf["roll"].mean()
pitch_mean = eulerdf["pitch"].mean()
yaw_mean = eulerdf["yaw"].mean()

roll_stdv = eulerdf["roll"].std()
pitch_stdv = eulerdf["pitch"].std()
yaw_stdv = eulerdf["yaw"].std()

print(f"Roll Mean = {roll_mean} degree \nPitch Mean =  {pitch_mean} degree \nYaw Mean =  {yaw_mean} degree")

print(f"Roll Std. Deviation = {roll_stdv} degree \nPitch Std. Deviation =  {pitch_stdv} degree \nYaw Std. Deviation =  {yaw_stdv} degree")

# For Roll
plot_roll = eulerdf.plot("Time", "roll", c ='red', label= "roll at time t")
plt.title("Roll at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Roll(Degree)")
plt.grid(True)
   
# For Pitch
plot_pitch = eulerdf.plot("Time", "pitch", c ='green', label= "pitch at time t")
plt.title("Pitch at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Pitch(Degree)")
plt.grid(True)

# For Yaw
plot_yaw = eulerdf.plot("Time", "yaw", c ='black', label= "yaw at time t")
plt.title("Yaw at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Yaw(Degree)")
plt.grid(True)

plt.show()
