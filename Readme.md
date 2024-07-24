# IMU Sensor Device driver, Characterization and Data Analysis

## Project Overview

This project focuses on characterizing and selecting IMU (Inertial Measurement Unit) sensors for robotic applications. The goal is to develop a device driver for the Vectornav VN-100 IMU, collect and analyze data, and understand the noise characteristics and errors of the sensor.

## Hardware and Sensors

- **IMU Sensor**: Vectornav VN-100
- **Hardware Setup**: Ensure proper configuration of udev rules and latency settings to handle high-rate sensor data.

### Hardware Setup

1. **Configure udev Rules**:
   - Create a file `/etc/udev/rules.d/50-VN-100.rules` with the following content:
     ```
     KERNEL=="ttyUSB[0-9]*", ACTION=="add", ATTRS{idVendor}=="1d6b", ATTRS{idProduct}=="0002", MODE="0666", GROUP="dialout"
     ```

   - Add USB latency rules by creating `/etc/udev/rules.d/49-USB-LATENCY.rules` with:
     ```
     ACTION=="add", SUBSYSTEM=="usb-serial", DRIVER=="ftdi_sio", ATTR{latency_timer}="1"
     ```

   - Apply the new rules:
     ```bash
     sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger
     ```

   - Verify the latency setting:
     ```bash
     cat /sys/bus/usb-serial/devices/<ttyUSB0>/latency_timer
     ```

## Device Driver Development

1. **IMU Device Driver**:
   - The provided code can be used as a device driver for the Vectornav VN-100 IMU. It opens the serial port with a baud rate of 115200 and configures the IMU to output data at 200Hz.
    python3 IMU-Driver/src/imu_device_driver/imu_device_driver.py

2. **Data Collection**:
   - Collected a time series data (rosbag) for accelerometers, gyros, and magnetometers.
   - Recorded data for at least 10-15 minutes with the IMU stationary, away from potential sources of interference.

3. **Stationary Noise Analysis**:
   - Ploted time series data and analyzed noise characteristics (mean and standard deviation).

## Allan Variance Analysis

1. **Data Collection**:
   - Collected approximately 5 hours of stationary IMU data in a vibration-free environment.

2. **Analyze Allan Variance**:
   - Used the MathWorks code for Allan variance analysis provided [here](https://www.mathworks.com/help/nav/ug/inertial-sensor-noise-analysis-using-allan-variance.html).
   - Addressed questions regarding error sources and noise modeling.
