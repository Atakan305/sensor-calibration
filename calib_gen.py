import serial
import time
from config import send_command, read_zerooffset_tilt, read_tilt_values
from backbone import (z_max_measurement, z_steps_transition, z_min_measurement, 
                      transition_z_to_x, x_max_measurement, x_steps_transition, 
                      x_min_measurement, transition_x_to_y, y_max_measurement, 
                      y_steps_transition, y_min_measurement, transition_to_initial)

def read_and_collect_data(ser, read_command, clear_command, duration=5, silent=False):
    data = []
    start_time = time.time()
    while time.time() - start_time < duration:
        send_command(ser, read_command)
        time.sleep(0.2)
        raw_value = ser.readline().decode().strip()

        # Strip off the ending '|' character if present
        if raw_value.endswith('|'):
            raw_value = raw_value[:-1]

        # Check if the raw_value is a valid float
        try:
            value = float(raw_value)
            data.append(value)
            if not silent:
                print(f"Current {read_command} value: {value}")
        except ValueError:
            if not silent:
                print(f"Invalid value received: {raw_value}")

    # Clear the buffer
    send_command(ser, clear_command)
    time.sleep(0.2)
    buffer_value = ser.readline().decode().strip()
    if not silent:
        print(f"Buffer {clear_command} value: {buffer_value}")

    return data

def perform_measurements(ser, read_command, clear_command, steps, record_data, silent=False):
    total_values = []

    for step in steps:
        command, repetitions, collect_data = step
        for _ in range(repetitions):
            response = send_command(ser, command)
            if collect_data:
                values = read_and_collect_data(ser, read_command, clear_command, duration=5, silent=silent)
                if not silent:
                    for value in values:
                        print(f'Axis {read_command} value: {value}')
                if record_data and not silent:
                    with open('sensor_data.txt', 'a') as file:
                        for value in values:
                            file.write(f'Axis {read_command} value: {value}\n')
                total_values.extend(values)

    return total_values

def store_sensor_data(ser, max_min_values):
    commands = {
        'SET_MAX_X': max_min_values['max_x'],
        'SET_MIN_X': max_min_values['min_x'],
        'SET_MAX_Y': max_min_values['max_y'],
        'SET_MIN_Y': max_min_values['min_y'],
        'SET_MAX_Z': max_min_values['max_z'],
        'SET_MIN_Z': max_min_values['min_z']
    }

    for command, value in commands.items():
        # Add '+' sign for max values
        if 'MAX' in command:
            full_command = f'{command}+{int(value)}'
        else:
            full_command = f'{command}{int(value)}'
        print(f"Sending command: {full_command}")
        send_command(ser, full_command)
        time.sleep(0.2)
        response = ser.readline().decode().strip()
        print(f"Stored {command}: {value} Response: {response}")

def read_sensor_data(ser):
    sensor_commands = [
        ('GET_MAX_X', 'max_x'),
        ('GET_MAX_Y', 'max_y'),
        ('GET_MAX_Z', 'max_z'),
        ('GET_MIN_X', 'min_x'),
        ('GET_MIN_Y', 'min_y'),
        ('GET_MIN_Z', 'min_z')
    ]

    print("Retrieving stored sensor data...")
    for command, variable in sensor_commands:
        print(f"Sending command: {command}")
        send_command(ser, command)
        time.sleep(0.2)
        value = ser.readline().decode().strip()
        print(f"{variable}: {value}")

def axis_calibration(ser, axis, max_command, min_command, transition_commands, record_data=True):
    max_min_values = {}

    print(f"Starting measurements for {axis} axis max.")
    max_values = perform_measurements(ser, f'READ_{axis}1', f'CLEAR_{axis}0', max_command, record_data=True)
    max_min_values[f'max_{axis.lower()}'] = max(max_values)

    print(f"Transitioning for {axis} axis.")
    perform_measurements(ser, '', '', transition_commands, record_data=False, silent=True)

    print(f"Starting measurements for {axis} axis min.")
    min_values = perform_measurements(ser, f'READ_{axis}1', f'CLEAR_{axis}0', min_command, record_data=True)
    max_min_values[f'min_{axis.lower()}'] = min(min_values)

    return max_min_values

def main():
    # Set up the serial connection (adjust the port and baudrate)
    ser = serial.Serial('COM3', 9600, timeout=1)

    # Give the sensor some time to reset
    time.sleep(2)

    # Initialize sensor connection and calibration
    input('Connect the sensor and press Enter')
    time.sleep(0.1)
    send_command(ser, 'CONNECT')
    time.sleep(0.2)
    send_command(ser, 'CALIBRATION START')
    time.sleep(0.2)
    calibration_response = ser.readline().decode().strip()
    print(f"Calibration response: {calibration_response}")

    if not calibration_response:
        print("Calibration failed or no response received.")
        return

    # Axis calibration steps
    steps_config = {
        'Z': {
            'max': z_max_measurement,
            'min': z_min_measurement,
            'transition': z_steps_transition
        },
        'X': {
            'max': x_max_measurement,
            'min': x_min_measurement,
            'transition': x_steps_transition
        },
        'Y': {
            'max': y_max_measurement,
            'min': y_min_measurement,
            'transition': y_steps_transition
        }
    }

    try:
        all_max_min_values = {}

        for axis, steps in steps_config.items():
            max_min_values = axis_calibration(ser, axis, steps['max'], steps['min'], steps['transition'])
            all_max_min_values.update(max_min_values)

        # Return to initial position
        print("Returning to initial position.")
        perform_measurements(ser, '', '', transition_to_initial, record_data=False)

        # Store sensor data
        print("Storing sensor data.")
        store_sensor_data(ser, all_max_min_values)

        # Retrieve and display sensor data
        if input("Retrieve and display sensor data? (y/n): ").strip().lower() == 'y':
            read_sensor_data(ser)

        # Option to stop the continuous process
        if input("Type 'stop' to end or press Enter to repeat: ").strip().lower() == 'stop':
            return

    except KeyboardInterrupt:
        print("Program interrupted.")

    finally:
        ser.close()

if __name__ == "__main__":
    main()
