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

You should see some output that starts with this:

```
Supported pids
--------------
PID num (hex) | PID num (int) | PID Name

```

This prints the list of supported Service 01 PID IDs. See: https://en.wikipedia.org/wiki/OBD-II_PIDs#Service_01_-_Show_current_data

The folder: `supported_pids_list` contains several text files, with the output of running this command for various vehicles.

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