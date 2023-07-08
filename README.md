# Background / Context

This repository contains additional tools for working with the [CANEdge 2](https://www.csselectronics.com/products/can-bus-data-logger-wifi-canedge2) data logger.

![device photo](./docs/canedge2-wifi-can-bus-data-logger-v3.jpg)

This device connects to your car's [OBD port](https://en.wikipedia.org/wiki/On-board_diagnostics) to log data.

# Repository / Code

This repository consists of 2 tools:

* A Python script for determining which PIDs your vehicle supports (`determine_supported_pids.py`)
* A Python script for generating the appropriate config file, based on the supported PIDs (`canedge_config_generator.py`) -- last tested with version 01.07 [July 2023]

Both tools should work for your vehicle, as long as your car is newer than 2008. I used these scripts for my 2018 Nissan Versa.

# Step 1: Determining supported PIDs

> Main article: https://en.wikipedia.org/wiki/OBD-II_PIDs

> Main section: https://en.wikipedia.org/wiki/OBD-II_PIDs#Service_01_PID_00_-_Show_PIDs_supported


To determine what OBD2 PIDs your vehicle supports, you'll first have to configure the CanEdge to send the PIDs with ID: 0x00, 0x20, 0x40, 0x60, 0x80, 0xA0, 0xC0. These PIDs return a 4-byte (32-bit) response bitmask that tells you which of next 32 PIDs are enabled.

You can copy the JSON from `transmit_block_for_decoding_pids.md` into your config file. Then, with the CANEdge connected, start your vehicle, and let it run for a few minutes.

Turn the car off, and remove the SD card from the unit.

Next, identify the MF4 file that was saved from this session.

Run the Python script:

```bash
$ python3 determine_supported_pids.py -i <PATH-TO-CANEDGE-MF4-FILE>
```

You should see some output that looks like this:

```
Supported pids
--------------
PID num (hex) | PID num (int) | PID Name
0x01 | 1d | Monitor status since DTCs cleared. (Includes malfunction indicator lamp (MIL), status and number of DTCs, components tests, DTC readiness checks)
0x03 | 3d | Fuel system status
0x04 | 4d | Calculated engine load
0x05 | 5d | Engine coolant temperature
0x06 | 6d | Short term fuel trim—Bank 1
0x07 | 7d | Long term fuel trim—Bank 1
0x12 | 12d | Engine speed
0x13 | 13d | Vehicle speed
0x14 | 14d | Timing advance
0x15 | 15d | Intake air temperature
0x16 | 16d | Mass air flow sensor (MAF) air flow rate
0x17 | 17d | Throttle position
0x19 | 19d | Oxygen sensors present (in 2 banks)
0x21 | 21d | Oxygen Sensor 2 A: Voltage B: Short term fuel trim
0x28 | 28d | OBD standards this vehicle conforms to
0x31 | 31d | Run time since engine start
0x32 | 32d | PIDs supported [$21 - $40]
0x33 | 33d | Distance traveled with malfunction indicator lamp (MIL) on
0x36 | 36d | Oxygen Sensor 1 AB: Air-Fuel Equivalence Ratio (lambda,λ) CD: Voltage
0x46 | 46d | Commanded evaporative purge
0x47 | 47d | Fuel Tank Level Input
0x48 | 48d | Warm-ups since codes cleared
0x49 | 49d | Distance traveled since codes cleared
0x50 | 50d | Evap. System Vapor Pressure
0x51 | 51d | Absolute Barometric Pressure
0x60 | 60d | Catalyst Temperature: Bank 1, Sensor 1
0x64 | 64d | PIDs supported [$41 - $60]
0x65 | 65d | Monitor status this drive cycle
0x66 | 66d | Control module voltage
0x67 | 67d | Absolute load value
0x68 | 68d | Commanded Air-Fuel Equivalence Ratio (lambda,λ)
0x69 | 69d | Relative throttle position
0x70 | 70d | Ambient air temperature
0x71 | 71d | Absolute throttle position B
0x73 | 73d | Accelerator pedal position D
0x74 | 74d | Accelerator pedal position E
0x76 | 76d | Commanded throttle actuator
0x77 | 77d | Time run with MIL on
0x81 | 81d | Fuel Type

```

This prints the list of supported Service 01 PID IDs. See: https://en.wikipedia.org/wiki/OBD-II_PIDs#Service_01_-_Show_current_data

# Step 2: Generating config file

Now that you have the list of supported PIDs, the next step is to tell your CanEdge to only send commands on those PIDs.

This step involves some manual processing on your end. I recommend making a spreadsheet with columns of: PID number, Message Name, Period, Delay, Response.

I have an example of the spreadsheet in the `docs` folder.

Once you're finished with the spreadsheet, replace the contents of the txt files in the `config_generator` directory with your information.

Then, run the Python script:

```bash
$ python3 canedge_config_generator.py
```

This will output text that you can copy directly into your CanEdge config file, based on the contents of your text files.