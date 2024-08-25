# Arduino LCD Message Display with Python Interface
Project Overview

This project demonstrates how to use an Arduino to control a 16x2 LCD display and interface with it using Python. The Arduino code reads messages from the serial port and displays them on the LCD, handling messages longer than 16 characters by splitting them across two lines. The Python script sends messages to the Arduino for display.
Features

    Arduino LCD Control: Displays messages on a 16x2 LCD screen.
    Python Integration: Send messages from Python to Arduino.
    Multi-Line Handling: Automatically splits and displays long messages across two lines of the LCD.

## Components

    Arduino Board: Compatible with Arduino Mega or Uno.
    16x2 LCD Display: HD44780-compatible LCD.
    Breadboard and Jumper Wires: For connecting the LCD to the Arduino.
    Potentiometer: For adjusting LCD contrast.
    Python Environment: For running the script to send messages.

## Arduino Setup
### Hardware Connections

    LCD to Arduino Connections:
        RS to Digital Pin 8
        E to Digital Pin 9
        D4 to Digital Pin 4
        D5 to Digital Pin 5
        D6 to Digital Pin 6
        D7 to Digital Pin 7
        VSS to Ground
        VCC to 5V
        VO to Potentiometer (middle pin for contrast adjustment)
        RW to Ground

    Potentiometer:
        One end to Ground
        Other end to 5V
        Middle pin to the VO pin of the LCD
### Arduino Code

    #include <LiquidCrystal.h>
    
    // Initialize the LCD with the pins connected to Arduino
    const int rs = 8, en = 9, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
    LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
    
    void setup() {
      lcd.begin(16, 2); // Initialize the LCD with 16 columns and 2 rows
      Serial.begin(9600); // Initialize serial communication
    }
    
    void loop() {
      if (Serial.available()) {
        String message = Serial.readStringUntil('\n'); // Read message until newline
    
        lcd.clear(); // Clear the LCD before printing new content
    
        // Split the message into two lines if it is longer than 16 characters
        if (message.length() > 16) {
          String line1 = message.substring(0, 16); // First 16 characters for the first line
          String line2 = message.substring(16);    // Remaining characters for the second line
          
          lcd.setCursor(0, 0); // Set cursor to the beginning of the first line
          lcd.print(line1);   // Print the first line
          
          lcd.setCursor(0, 1); // Set cursor to the beginning of the second line
          lcd.print(line2);   // Print the second line
        } else {
          lcd.setCursor(0, 0); // Set cursor to the beginning of the first line
          lcd.print(message); // Print the message if it fits within one line
        }
      }
    }
## Python Script 

## Usage

## Troubleshooting

## License

## Acknowledgments
