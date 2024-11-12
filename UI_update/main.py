import serial
import time
import logging

logging.basicConfig(
    filename='arduino_communication.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def initialize_serial_connection(port, baud_rate=9600):
    """
    Initialize serial communication with the Arduino.

    :param port: The COM port to which the Arduino is connected (e.g., 'COM6').
    :param baud_rate: The baud rate for serial communication (default is 9600).
    :return: Serial object if initialization is successful; otherwise, None.
    """
    try:
        ser = serial.Serial(port, baud_rate)
        time.sleep(2)  # wait for MCU to reset
        logging.info(f"Serial connection initialized on {port}:{baud_rate}.")
        return ser
    except serial.SerialException as e:
        logging.error(f"Error initializing serial connection: {e}")
        return None


def send_message(ser, message):
    """
    Send a multi-line message to the Arduino.

    :param ser: The serial connection object.
    :param message: The message to send to the Arduino.
    """
    if ser:
        try:
            ser.write(message.encode('utf-8') + b'\n')
            logging.info("Message sent successfully.")
        except serial.SerialException as e:
            logging.error(f"Error sending message: {e}")
    else:
        logging.warning("Serial connection not established.")


def close_serial_connection(ser):
    """
    Close the serial connection.

    :param ser: The serial connection object.
    """
    if ser:
        ser.close()
        logging.info("Serial connection closed.")
    else:
        logging.warning("Serial connection was not established.")


