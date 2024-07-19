# 3-Axis Digital Accelerometer Tilt Sensor Calibration

This project provides a set of scripts for calibrating a 3-axis digital accelerometer tilt sensor using Python with executing the desired commands using serial communication.
Accelerometers like the ADXL350 are vital in applications such as smartphones, robotics, and gaming devices. They measure acceleration along three perpendicular axes (X, Y, and Z), enabling the calculation of tilt and orientation. Proper calibration is crucial for accurate readings.

## Field of Applications
There are a numerous use of these accelerometer sensors. Particularly, using these kinds of sensors, human beings can be monitored and benifitted or even saved from different conditions. Therefore the accelerometer sensors play important roles in various sectors, which include industry, medical, social applications, and domestic applications for monitoring motions of variety objects. 

## Useful Informations about ADXL350 3-Axis ±1g/±2g/±4g/±8g Digital Accelerometer 
The high performance ADXL350 is a small, thin, low power, 3-axis accelerometer with high resolution (13-bit) and selectable measurement ranges up to ±8 g. The ADXL350 offers industry-leading temperature performance with guaranteed min/max specification for offset over temperature. Digital output data is formatted as 16-bit twos complement and is accessible through either a SPI (3- or 4-wire) or I2C digital interface.

![image](https://github.com/user-attachments/assets/ba963be4-65ac-4bba-8f9a-483b6a0a6176)

It measures the static acceleration of gravity in tilt sensing applications, as well as dynamic acceleration resulting from motion or shock. Its high resolution (2 mg/LSB) enables measurement of inclination changes of less than 1.0°. 
You can check it out more details from: 
https://www.analog.com/en/products/adxl350.html#part-details 

## General Sensor Calibration Methods
### Single-Point Calibration:
- Objective: Establish a zero-g reference for each axis.
- Process:
    - Place the sensor on a stable, flat surface.
    - Record the sensor’s output for each axis.
    - Adjust subsequent readings by subtracting the recorded zero-g offsets.

### Two-Point Calibration:
- Objective: Use two known acceleration values to calibrate.
- Process:
    - Measure the sensor’s output at 0 g (stationary) and 1 g (aligned with gravity). Usually 
    - Calculate offset and scale factor for each axis.
    - Apply these adjustments to linearize the sensor’s output.

### Multi-Point Calibration:
- Objective: Use multiple reference points for a more accurate calibration.
- Process:
    - Measure the sensor’s output at several known points.
    - Fit a calibration curve through these points to correct non-linear behavior.

### Dynamic Calibration:
- Objective: Use motion to calibrate.
- Process:
    - Move the sensor through known accelerations (e.g., rotations or swings).
    - Compare the output to expected values.
    - Adjust readings based on this dynamic data.

## Files

- **calib_gen.py**: Main script to run the calibration process.
- **config.py**: Contains utility functions for serial communication and sensor data reading.
- **backbone.py**: Defines the motor operation steps for each axis during the calibration process.

## Requirements

- Python 3.x
- `numpy` library  
- `pyserial` library

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd sensor-calibration
    ```

2. Install the required Python packages:
    ```sh
    pip install numpy
    pip install pyserial
    ```

## Usage

1. Connect your sensor to the serial port, identify the port number (ex: COM3), determine the baudrate (ex: 9600 bps)  
2. Run the calibration script:
    ```sh
    python calib_gen.py
    ```

3. Follow the on-screen instructions (from the terminal screen) to complete the calibration.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
