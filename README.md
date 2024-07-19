# 3-Axis Digital Accelerometer Tilt Sensor Calibration

3-axis digital acceleration tilt sensor calibration with Python. Execute the desired commands using serial communication. This project provides a set of scripts for calibrating a 3-axis digital accelerometer tilt sensor using Python.

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
