"""

File : determine_supported_pids.py

"""

import pdb
import asammdf
import argparse
import typing

HEXADECIMAL_RADIX = 16
FORMATTED_PREFIX = "0x"

def get_enabled_pids_from_file(canedge_mf4_filename : str) -> typing.List:

    #mdf = asammdf.MDF("/home/raleigh/github/CanEdge_OBD_Organizer/data/00000001.MF4")
    mdf = asammdf.MDF(canedge_mf4_filename)

    can_database_files = {
        "CAN": [("./dbc/CSS-Electronics-OBD2-v1.4.dbc", 0), ("./dbc/CSS-Electronics-OBD2-Extended-v1.4.dbc", 0)]
    }
    extracted_mdf = mdf.extract_bus_logging(database_files=can_database_files).to_dataframe()

    # These are hardcoded, but the names are common across most DBC files
    dbc_column_names_pids_supported = ["S1_PID_00_PIDsSupported_01_20", "S1_PID_20_PIDsSupported_21_40", "S1_PID_40_PIDsSupported_41_60", "S1_PID_60_PIDsSupported_61_80", "S1_PID_80_PIDsSupported_81_A0", "S1_PID_A0_PIDsSupported_A1_C0", "S1_PID_C0_PIDsSupported_C1_E0"]

    full_hex_list_pids = list()

    for col_name in dbc_column_names_pids_supported:

        try:
            # TODO Check that this value hasn't changed between the first and the last?
            raw_can_resp = extracted_mdf[col_name][0]

            # Ignore the '0x' (2 chars) prefix from each hexadecimal number
            hex_encoded_resp = str(hex(raw_can_resp))[len(FORMATTED_PREFIX):]

            print(f"[DEBUG] Raw CAN bus response to OBD query {col_name} was '{hex_encoded_resp}'h")
            full_hex_list_pids.append(hex_encoded_resp)

        except KeyError as e:
            print(f"[WARNING] '{col_name}' was not found in the provided MF4 file, it's likely that your vehicle doesn't support this OBD PID \r\n {e}")

    # Now convert the hex-encoded CAN response to a binary representation
    bin_repr_list_pids = list()

    #print(f"[DEBUG] Hex: {full_hex_list_pids}")

    supported_pid_nums = set()

    for _, hex_sequence in enumerate(full_hex_list_pids):

        current_pid_group_bin_repr = ""

        for char in hex_sequence:
            current_pid_group_bin_repr += "{:04b}".format(int(char, HEXADECIMAL_RADIX))
            
        bin_repr_list_pids.append(current_pid_group_bin_repr)

    for bin_seq_idx, bin_sequence in enumerate(bin_repr_list_pids):

        for pid_idx, pid_num in enumerate(bin_sequence):
            
            if bool(int(pid_num)):

                # Each of the PIDs is split into a group of 32, but the PID numbers on these 32-boundaries
                # are actually the PIDs for checking which PIDs are enabled -- hence the +1
                # ie. PID #0 is for which of PIDs 1-32 (inclusive) is available
                #     PID #32 is for which of PIDs 33-64 is available, and so on
                #
                # The multiplication comes from: if you're in the 3rd group of 32-bits, you're
                # looking at what PIDs from 65 to 96 are available
                corresponding_pid_num = (1 + pid_idx) + (len(bin_sequence) * bin_seq_idx)
                #print(f"PID #{corresponding_pid_num} is enabled!")
                supported_pid_nums.add(corresponding_pid_num)

    return supported_pid_nums

if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()
    argparse_parser.add_argument("-i", "--canedge-mf4-file", type=str, required=True, help="The CanEdge MF4 data file containing the supported PIDs query")

    argparse_args = argparse_parser.parse_args()

    supported_pids = get_enabled_pids_from_file(argparse_args.canedge_mf4_file)

    print("Supported pids")
    print("--------------")

    for pid in supported_pids:
        print(f"{hex(pid)} {int(pid)}d")