ESP32 Smart Home Beginner Project

MicroPython • ESP32 • Buttons • LEDs • Smart Home Basics

By Ahmad Azroun

Renewable Energy Manager | IoT & AI Specialist | Smart Energy Systems Developer

---

Deutsche Dokumentation

Dieses Projekt dokumentiert die ersten praktischen Schritte im Bereich IoT und Smart Home mit ESP32 und MicroPython.

Das Projekt begann mit der Steuerung der internen LED des ESP32 und entwickelte sich später zu mehreren LEDs, Tastern und Widerständen.

Verwendete Komponenten

- ESP32 DevKit V1
- Breadboard
- Push Buttons
- LEDs
- Widerstände
- Jumper Kabel
- MicroPython

---

1️⃣ Interne LED mit einem Taster

Im ersten Schritt wurde ein einzelner Taster verwendet, um die interne LED des ESP32 zu steuern.

- Taster → GPIO4 / D4
- Interne LED → GPIO2

---

2️⃣ Externe LED mit einem Taster

Danach wurde eine externe LED mit einem Widerstand verwendet.

Der Widerstand schützt die LED und begrenzt den Stromfluss.

- Taster → GPIO4
- Externe LED → GPIO5

---

3️⃣ Vollständiges Projekt

Die finale Version verwendet:

- Drei Taster
- Interne und externe LEDs
- Einen Taster zur Steuerung von zwei LEDs gleichzeitig
- Standalone-Ausführung mit "main.py"
- Widerstände zum Schutz der LEDs

🔘 Funktionen

Button| Funktion
GPIO4| Steuert zwei externe LEDs
GPIO19| Steuert eine externe LED
GPIO18| Steuert die interne LED

---

Future Improvements

- WiFi-Steuerung
- Bluetooth-Steuerung
- Lüfter- und Relaissteuerung
- Temperatur- und Feuchtigkeitssensoren
- Smart Energy Systems
- Solarenergie-Integration
- KI-basierte Smart-Home-Automatisierung

---

🇬🇧 English Documentation

This project documents the first practical steps in IoT and Smart Home development using ESP32 and MicroPython.

The project started with controlling the internal LED of the ESP32 and later evolved into controlling multiple LEDs, buttons, and resistors.

Components Used

- ESP32 DevKit V1
- Breadboard
- Push Buttons
- LEDs
- Resistors
- Jumper Wires
- MicroPython

---

1️⃣ Internal LED with One Button

The first stage of the project used one push button to control the internal LED of the ESP32.

- Button → GPIO4 / D4
- Internal LED → GPIO2

---

2️⃣ External LED with One Button

The next step added an external LED with a resistor.

The resistor protects the LED and limits the current flow.

- Button → GPIO4
- External LED → GPIO5

---

3️⃣ Complete Final Project

The final version of the project includes:

- Three push buttons
- Internal and external LEDs
- One button controlling two LEDs together
- Standalone execution using "main.py"
- Resistors for LED protection

🔘 Functions

Button| Function
GPIO4| Controls two external LEDs
GPIO19| Controls one external LED
GPIO18| Controls the internal LED

---

Future Improvements

- WiFi control
- Bluetooth control
- Fan and relay control
- Temperature and humidity sensors
- Smart energy systems
- Solar energy integration
- AI-based Smart Home automation

---

📄 Project Documentation

The complete bilingual project documentation PDF is included in this repository.

---

Author

Ahmad Azroun

Renewable Energy Manager | IoT & AI Specialist | Smart Energy Systems Developer
