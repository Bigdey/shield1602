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