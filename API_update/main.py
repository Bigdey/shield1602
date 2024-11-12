import datetime

import serial
import time
import logging
import requests

# Logging setup
logging.basicConfig(
    filename='arduino_communication.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def initialize_serial_connection(port, baud_rate=9600):
    """
    Initialize serial communication with the Arduino.
    """
    try:
        ser = serial.Serial(port, baud_rate)
        time.sleep(2)  # Wait for Arduino to reset
        logging.info(f"Serial connection initialized on {port}:{baud_rate}.")
        return ser
    except serial.SerialException as e:
        logging.error(f"Error initializing serial connection: {e}")
        return None


def send_message(ser, message):
    """
    Send a message to the Arduino.
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
    """
    if ser:
        ser.close()
        logging.info("Serial connection closed.")
    else:
        logging.warning("Serial connection was not established.")


def get_bitcoin_price():
    """
    Fetch the latest Bitcoin price from a public API.
    """
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        data = response.json()
        price = data['bpi']['USD']['rate']  # Get the price in USD
        return f"BTC: ${price[:6]}"  # Limit to 6 characters for better LCD fit
    except requests.RequestException as e:
        logging.error(f"Error fetching Bitcoin price: {e}")
        return "BTC N/A"


def update_lcd_with_bitcoin_price(port):
    """
    Continuously update the Arduino LCD with the latest Bitcoin price every 30 seconds.
    """
    while True:
        ser = initialize_serial_connection(port)
        if ser:
            # Fetch the latest Bitcoin price
            price_message = get_bitcoin_price()
            # Pad the message to fit 16 characters for each LCD line
            time_now = datetime.datetime.now().strftime("%H:%M")
            line1_message = price_message.ljust(16)[:16]
            time.sleep(0.1)
            line2_message = f"At: {time_now}".ljust(16)[:16]
            # Send to Arduino
            send_message(ser, f"{line1_message}{line2_message}")
            close_serial_connection(ser)
        else:
            logging.error("Failed to initialize serial connection for Bitcoin update.")

        # Wait for 30 seconds before updating again
        time.sleep(30)


if __name__ == "__main__":
    # Replace 'COM6' with your actual Arduino port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
    ARDUINO_PORT = 'COM4'
    update_lcd_with_bitcoin_price(ARDUINO_PORT)
