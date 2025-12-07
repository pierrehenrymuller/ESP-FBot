# ESP-Home FBot Battery Component

** THIS IS DEVELOPMENT CODE, NOT TESTED YET ***

This is a HomeAssistant, ESP-Home custom component for locally monitoring and controlling battery systems via Bluetooth. Should work with the following batteries:

 - [FOSSiBOT F3600 Pro Portable Power Station](https://www.fossibot.com/products/fossibot-f3600-pro)
 - [FOSSiBOT F2400 Portable Power Station](https://www.fossibot.com/products/fossibot-f2400)
 - [SYDPOWER N052](https://www.sydpower.com/product/n052?id=665461cb8b0da4a4e43e4609)
 - [SYDPOWER N066](https://www.sydpower.com/product/detail?id=665462e4a7c432936b1b583d)
 - [AFERIY P210](https://www.aferiy.com/products/aferiy-p210-portable-power-station-2400w-2048wh)
 - [AFERIY P310](https://www.aferiy.com/products/aferiy-p310-portable-power-station-3300w-3840wh)
 
Basically, any power station that works with the "BrightEMS" application. You normally connect these batteries to your WIFI and they will connect to a cloud server. You then have to manage the device from the cloud this can be slow and not ideal in outage situations. Instead, you can get fast local management of your battery by loading this ESP-Home component on a small device near the battery. The device will communicate to the battery using Bluetooth and relay the data locally using WIFI.

## Features

- **Battery Monitoring**: Real-time battery state of charge (%), remaining capacity (kWh), and time remaining
- **Power Monitoring**: Track input power, output power, system consumption, and total power flow
- **Output Control**: Switch USB ports, DC outputs, AC inverter, and light on/off
- **Home Assistant Integration**: All sensors and controls automatically discovered in Home Assistant
- **Auto-reconnect**: Handles BLE disconnections and automatically reconnects

## Hardware Requirements

- I suggest the [M5Stack ATOM Light](https://shop.m5stack.com/products/atom-lite-esp32-development-kit) or the [M5StickC PLUS2 ESP32 Mini](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit) device, but many ESP32 (ESP32-WROOM, ESP32-DevKit, etc.) will do.
- A compatible battery that makes use of the "BrightEMS" application. You do not need to pair the battery to WIFI.
- The ESP32 device will need to be within range of the battery (typically 10-30 feet)

## Installation

1. Use the example configuration file `fbot-example.yaml` as a starting point.
2. Update WiFi credentials and API encryption key.
3. Flash to your ESP32 device.

## Configuration

### Sensors

All sensors are optional. Include only the ones you need:

```yaml
sensor:
  - platform: fbot
    fbot_id: my_fbot
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
    remaining_time:
      name: "Remaining Time"
```

### Binary Sensors

```yaml
binary_sensor:
  - platform: fbot
    fbot_id: my_fbot
    connected:
      name: "Fbot Connected"
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
  - platform: fbot
    fbot_id: my_fbot
    usb:
      name: "USB Output"
    dc:
      name: "DC Output"
    ac:
      name: "AC Inverter"
    light:
      name: "Light"
```