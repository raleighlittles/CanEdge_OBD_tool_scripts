"""

Last tested with config version 01.07

"""

import os
import json
import typing
import pdb
import sys

PID_NAMES_FILE = "pid_names.txt"
PID_PERIODS_FILE = "pid_periods.txt"
PID_DELAYS_FILE = "pid_delays.txt"
PID_RESPONSE_DATA_FILE = "pid_responses.txt"
CANEDGE_CANBUS_TRANSMIT_REQ_TYPE = "7DF"


def generate_canedge_config(pid_names: typing.List, pid_periods: typing.List, pid_delays: typing.List, pid_response_data: typing.List) -> dict:
    transmit_blocks = dict()
    transmit_blocks["transmit"] = list()

    for idx in range(0, len(pid_names)):

        pid_transmission_obj = dict()

        # Most fields are hardcoded from the config. Make sure to load this into the Canedge config
        # tester to verify, before use: https://canlogger.csselectronics.com/simple-editor/

        pid_transmission_obj["name"] = pid_names[idx]
        pid_transmission_obj["state"] = 1
        pid_transmission_obj["id_format"] = 0
        pid_transmission_obj["frame_format"] = 0
        pid_transmission_obj["brs"] = 0
        # controls whether the CAN frame itself gets logged or not (?)
        pid_transmission_obj["log"] = 1
        pid_transmission_obj["period"] = int(pid_periods[idx])
        pid_transmission_obj["delay"] = int(pid_delays[idx])
        pid_transmission_obj["id"] = CANEDGE_CANBUS_TRANSMIT_REQ_TYPE
        pid_transmission_obj["data"] = pid_response_data[idx]

        transmit_blocks["transmit"].append(pid_transmission_obj)

    return transmit_blocks


def get_lines_from_file(filename: str) -> typing.List:

    lines_from_file = list()

    with open(filename, 'r') as file_obj:
        for line in file_obj:
            lines_from_file.append(line.strip())

    return lines_from_file


if __name__ == "__main__":

    pid_names = get_lines_from_file(PID_NAMES_FILE)
    pid_periods = get_lines_from_file(PID_PERIODS_FILE)
    pid_delays = get_lines_from_file(PID_DELAYS_FILE)
    pid_response_data = get_lines_from_file(PID_RESPONSE_DATA_FILE)

    if not (len(pid_names) == len(pid_periods) == len(pid_delays) == len(pid_response_data)):
        print("[ERROR] Mismatch in size between text files -- can't create config")
        sys.exit(3)

    else:
        # Doesn't look like there's a good way to easily prettyprint/format the JSON
        # https://stackoverflow.com/questions/12943819/
        print(json.dumps(generate_canedge_config(
            pid_names, pid_periods, pid_delays, pid_response_data)))
