# 3-Axis Digital Accelerometer Tilt Sensor Calibration

3-axis digital acceleration tilt sensor calibration with Python. Execute the desired commands using serial communication. This project provides a set of scripts for calibrating a 3-axis digital accelerometer tilt sensor using Python.
Accelerometers like the ADXL350 are vital in applications such as smartphones, robotics, and gaming devices. They measure acceleration along three perpendicular axes (X, Y, and Z), enabling the calculation of tilt and orientation. Proper calibration is crucial for accurate readings.

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
    - Measure the sensor’s output at 0 g (stationary) and 1 g (aligned with gravity).
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

1. Connect your sensor to the serial port, identify the port number (ex: COM3), determine the baudrate (ex: 9600)  
2. Run the calibration script:
    ```sh
    python calib_gen.py
    ```

3. Follow the on-screen instructions (from the terminal screen) to complete the calibration.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
