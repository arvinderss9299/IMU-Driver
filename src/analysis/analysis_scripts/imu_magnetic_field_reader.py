import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
from tf.transformations import euler_from_quaternion

b = bagreader('/home/arvinder/RSN/src/analysis/rosbag_data/15_minutes_data.bag')

imudata= b.message_by_topic(topic="/imu_data")
imudataread = pd.read_csv(imudata)
imudf = pd.DataFrame(imudataread, columns=["Time", "magnetic_field.x", "magnetic_field.y", "magnetic_field.z"]).astype(float)
imudf["Time"] = (imudf["Time"] - imudf.at[0,"Time"])/60

magnetic_field_x_mean = imudf["magnetic_field.x"].mean()
magnetic_field_y_mean = imudf["magnetic_field.y"].mean()
magnetic_field_z_mean = imudf["magnetic_field.z"].mean()


magnetic_field_x_stdv = imudf["magnetic_field.x"].std()
magnetic_field_y_stdv = imudf["magnetic_field.y"].std()
magnetic_field_z_stdv = imudf["magnetic_field.z"].std()

print(f"Magnetic field X Mean = {magnetic_field_x_mean} Tesla \nMagnetic field Y Mean =  {magnetic_field_y_mean} Tesla \nMagnetic field Z Mean =  {magnetic_field_z_mean} Tesla")

print(f"Magnetic field X Std. Deviation = {magnetic_field_x_stdv} Tesla \nMagnetic field Y Std. Deviation =  {magnetic_field_y_stdv} Tesla \nMagnetic field Z Std. Deviation =  {magnetic_field_z_stdv} Tesla")

# For magnetic_field X
plot_magnetic_field_x = imudf.plot("Time", "magnetic_field.x", c ='red', label= "magnetic_field_x at time t")
plt.title("magnetic_field_x at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Magnetic_field(Tesla)")
plt.grid(True)
  
# For magnetic_field Y
plot_magnetic_field_y = imudf.plot("Time", "magnetic_field.y", c ='green', label= "magnetic_field_y at time t")
plt.title("magnetic_field_y at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Magnetic_field(Tesla)")
plt.grid(True)

# For magnetic_field Z
plot_magnetic_field_z = imudf.plot("Time", "magnetic_field.z", c ='black', label= "magnetic_field_z at time t")
plt.title("magnetic_field_z at time t")
plt.legend(loc="upper right")
plt.xlabel("Time(min)")
plt.ylabel("Magnetic_field(Tesla)")
plt.grid(True)

plt.show()
