# Fossibot Battery ESP-Home Component

** THIS IS DEVELOPMENT CODE, NOT TESTED YET ***

ESP-Home custom component for monitoring and controlling Fossibot large battery systems via Bluetooth Low Energy (BLE).

## Features

- **Battery Monitoring**: Real-time battery state of charge (%), remaining capacity (kWh), and time remaining
- **Power Monitoring**: Track input power, output power, system consumption, and total power flow
- **Output Control**: Switch USB ports, DC outputs, AC inverter, and light on/off
- **Home Assistant Integration**: All sensors and controls automatically discovered in Home Assistant
- **Auto-reconnect**: Handles BLE disconnections and automatically reconnects

## Hardware Requirements

- ESP32 board (ESP32-WROOM, ESP32-DevKit, etc.)
- Fossibot battery with BLE (device name starts with "POWER" or "Fossibot")
- The ESP32 should be within BLE range of the battery (typically 10-30 feet)

## Installation

1. Use the example configuration file `fossibot-example.yaml` as a starting point
2. Update WiFi credentials and API encryption key
3. Flash to your ESP32 device

## Configuration

### Sensors

All sensors are optional. Include only the ones you need:

```yaml
sensor:
  - platform: fossibot
    fossibot_id: my_fossibot
    battery_level:
      name: "Battery Level"
    input_power:
      name: "Input Power"
    output_power:
      name: "Output Power"
    system_power:
      name: "System Power"
    total_power:
      name: "Total Power"
    remaining_kwh:
      name: "Remaining Capacity"
    remaining_time:
      name: "Remaining Time"
```

### Binary Sensors

```yaml
binary_sensor:
  - platform: fossibot
    fossibot_id: my_fossibot
    connected:
      name: "Fossibot Connected"
    usb_active:
      name: "USB Active"
    dc_active:
      name: "DC Active"
    ac_active:
      name: "AC Inverter Active"
    light_active:
      name: "Light Active"
```

### Switches

```yaml
switch:
  - platform: fossibot
    fossibot_id: my_fossibot
    usb:
      name: "USB Output"
    dc:
      name: "DC Output"
    ac:
      name: "AC Inverter"
    light:
      name: "Light"
```