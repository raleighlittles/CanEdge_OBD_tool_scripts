"""
File : determine_supported_service01_pids.py

Determine which of the OBD Service 1 PIDS: https://en.wikipedia.org/wiki/OBD-II_PIDs#Service_01_-_Show_current_data

are supported by the vehicle

"""

import pdb
import asammdf
import argparse
import typing

HEXADECIMAL_RADIX = 16
FORMATTED_PREFIX = "0x"


def get_enabled_pids_from_file(canedge_mf4_filename: str) -> typing.List:

    mdf = asammdf.MDF(canedge_mf4_filename)

    can_database_files = {
        "CAN": [("./dbc/CSS-Electronics-OBD2-v1.4.dbc", 0), ("./dbc/CSS-Electronics-OBD2-Extended-v1.4.dbc", 0)]
    }
    extracted_mdf = mdf.extract_bus_logging(
        database_files=can_database_files).to_dataframe()

    # These are hardcoded, but the names are common across most DBC files
    dbc_column_names_pids_supported = ["S1_PID_00_PIDsSupported_01_20", "S1_PID_20_PIDsSupported_21_40", "S1_PID_40_PIDsSupported_41_60",
                                       "S1_PID_60_PIDsSupported_61_80", "S1_PID_80_PIDsSupported_81_A0", "S1_PID_A0_PIDsSupported_A1_C0", "S1_PID_C0_PIDsSupported_C1_E0"]

    full_hex_list_pids = list()

    for col_name in dbc_column_names_pids_supported:

        try:
            # TODO Check that this value hasn't changed between the first and the last?
            raw_can_resp = extracted_mdf[col_name][0]

            # Ignore the '0x' (2 chars) prefix from each hexadecimal number
            hex_encoded_resp = str(hex(raw_can_resp))[len(FORMATTED_PREFIX):]

            print(
                f"[DEBUG] Raw CAN bus response to OBD query {col_name} was '{hex_encoded_resp}'h")
            full_hex_list_pids.append(hex_encoded_resp)

        except KeyError as e:
            print(
                f"[WARNING] '{col_name}' was not found in the provided MF4 file, it's likely that your vehicle doesn't support this OBD PID \r\n {e}")

    # Now convert the hex-encoded CAN response to a binary representation
    bin_repr_list_pids = list()

    # print(f"[DEBUG] Hex: {full_hex_list_pids}")

    supported_pid_nums = set()

    for _, hex_sequence in enumerate(full_hex_list_pids):

        current_pid_group_bin_repr = ""

        for char in hex_sequence:
            current_pid_group_bin_repr += "{:04b}".format(
                int(char, HEXADECIMAL_RADIX))

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
                corresponding_pid_num = (
                    1 + pid_idx) + (len(bin_sequence) * bin_seq_idx)
                # print(f"PID #{corresponding_pid_num} is enabled!")
                supported_pid_nums.add(corresponding_pid_num)

    return supported_pid_nums


def get_pid_name_from_number(pid_num : int) -> str:

    # Generated from `all_pids_and_names_from_wikipedia.csv`

    all_s01_pids = {'0': 'PIDs supported [$01 - $20]', '1': 'Monitor status since DTCs cleared. (Includes malfunction indicator lamp (MIL), status and number of DTCs, components tests, DTC readiness checks)', '2': 'DTC that caused freeze frame to be stored.', '3': 'Fuel system status', '4': 'Calculated engine load', '5': 'Engine coolant temperature', '6': 'Short term fuel trim—Bank 1', '7': 'Long term fuel trim—Bank 1', '8': 'Short term fuel trim—Bank 2', '9': 'Long term fuel trim—Bank 2', '10': 'Fuel pressure (gauge pressure)', '11': 'Intake manifold absolute pressure', '12': 'Engine speed', '13': 'Vehicle speed', '14': 'Timing advance', '15': 'Intake air temperature', '16': 'Mass air flow sensor (MAF) air flow rate', '17': 'Throttle position', '18': 'Commanded secondary air status', '19': 'Oxygen sensors present (in 2 banks)', '20': 'Oxygen Sensor 1\nA: Voltage\nB: Short term fuel trim', '21': 'Oxygen Sensor 2\nA: Voltage\nB: Short term fuel trim', '22': 'Oxygen Sensor 3\nA: Voltage\nB: Short term fuel trim', '23': 'Oxygen Sensor 4\nA: Voltage\nB: Short term fuel trim', '24': 'Oxygen Sensor 5\nA: Voltage\nB: Short term fuel trim', '25': 'Oxygen Sensor 6\nA: Voltage\nB: Short term fuel trim', '26': 'Oxygen Sensor 7\nA: Voltage\nB: Short term fuel trim', '27': 'Oxygen Sensor 8\nA: Voltage\nB: Short term fuel trim', '28': 'OBD standards this vehicle conforms to', '29': 'Oxygen sensors present (in 4 banks)', '30': 'Auxiliary input status', '31': 'Run time since engine start', '32': 'PIDs supported [$21 - $40]', '33': 'Distance traveled with malfunction indicator lamp (MIL) on', '34': 'Fuel Rail Pressure (relative to manifold vacuum)', '35': 'Fuel Rail Gauge Pressure (diesel, or gasoline direct injection)', '36': 'Oxygen Sensor 1\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '37': 'Oxygen Sensor 2\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '38': 'Oxygen Sensor 3\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '39': 'Oxygen Sensor 4\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '40': 'Oxygen Sensor 5\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '41': 'Oxygen Sensor 6\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '42': 'Oxygen Sensor 7\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '43': 'Oxygen Sensor 8\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Voltage', '44': 'Commanded EGR', '45': 'EGR Error', '46': 'Commanded evaporative purge', '47': 'Fuel Tank Level Input', '48': 'Warm-ups since codes cleared', '49': 'Distance traveled since codes cleared', '50': 'Evap. System Vapor Pressure', '51': 'Absolute Barometric Pressure', '52': 'Oxygen Sensor 1\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '53': 'Oxygen Sensor 2\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '54': 'Oxygen Sensor 3\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '55': 'Oxygen Sensor 4\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '56': 'Oxygen Sensor 5\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '57': 'Oxygen Sensor 6\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '58': 'Oxygen Sensor 7\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '59': 'Oxygen Sensor 8\nAB: Air-Fuel Equivalence Ratio (lambda,λ)\nCD: Current', '60': 'Catalyst Temperature: Bank 1, Sensor 1', '61': 'Catalyst Temperature: Bank 2, Sensor 1', '62': 'Catalyst Temperature: Bank 1, Sensor 2', '63': 'Catalyst Temperature: Bank 2, Sensor 2', '64': 'PIDs supported [$41 - $60]', '65': 'Monitor status this drive cycle', '66': 'Control module voltage', '67': 'Absolute load value', '68': 'Commanded Air-Fuel Equivalence Ratio (lambda,λ)', '69': 'Relative throttle position', '70': 'Ambient air temperature', '71': 'Absolute throttle position B', '72': 'Absolute throttle position C', '73': 'Accelerator pedal position D', '74': 'Accelerator pedal position E', '75': 'Accelerator pedal position F', '76': 'Commanded throttle actuator', '77': 'Time run with MIL on', '78': 'Time since trouble codes cleared', '79': 'Maximum value for Fuel–Air equivalence ratio, oxygen sensor voltage, oxygen sensor current, and intake manifold absolute pressure', '80': 'Maximum value for air flow rate from mass air flow sensor', '81': 'Fuel Type', '82': 'Ethanol fuel %', '83': 'Absolute Evap system Vapor Pressure', '84': 'Evap system vapor pressure', '85': 'Short term secondary oxygen sensor trim, A: bank 1, B: bank 3', '86': 'Long term secondary oxygen sensor trim, A: bank 1, B: bank 3', '87': 'Short term secondary oxygen sensor trim, A: bank 2, B: bank 4', '88': 'Long term secondary oxygen sensor trim, A: bank 2, B: bank 4', '89': 'Fuel rail absolute pressure', '90': 'Relative accelerator pedal position', '91': 'Hybrid battery pack remaining life', '92': 'Engine oil temperature', '93': 'Fuel injection timing', '94': 'Engine fuel rate', '95': 'Emission requirements to which vehicle is designed', '96': 'PIDs supported [$61 - $80]', '97': "Driver's demand engine - percent torque", '98': 'Actual engine - percent torque', '99': 'Engine reference torque', '100': 'Engine percent torque data', '101': 'Auxiliary input / output supported', '102': 'Mass air flow sensor', '103': 'Engine coolant temperature', '104': 'Intake air temperature sensor', '105': 'Actual EGR, Commanded EGR, and EGR Error', '106': 'Commanded Diesel intake air flow control and relative intake air flow position', '107': 'Exhaust gas recirculation temperature', '108': 'Commanded throttle actuator control and relative throttle position', '109': 'Fuel pressure control system', '110': 'Injection pressure control system', '111': 'Turbocharger compressor inlet pressure', '112': 'Boost pressure control', '113': 'Variable Geometry turbo (VGT) control', '114': 'Wastegate control', '115': 'Exhaust pressure', '116': 'Turbocharger RPM', '117': 'Turbocharger temperature', '118': 'Turbocharger temperature', '119': 'Charge air cooler temperature (CACT)', '120': 'Exhaust Gas temperature (EGT) Bank 1', '121': 'Exhaust Gas temperature (EGT) Bank 2', '122': 'Diesel particulate filter (DPF)differential pressure', '123': 'Diesel particulate filter (DPF)', '124': 'Diesel Particulate filter (DPF) temperature', '125': 'NOx NTE (Not-To-Exceed) control area status', '126': 'PM NTE (Not-To-Exceed) control area status', '127': 'Engine run time [b]', '128': 'PIDs supported [$81 - $A0]', '129': 'Engine run time for Auxiliary Emissions Control Device(AECD)', '130': 'Engine run time for Auxiliary Emissions Control Device(AECD)', '131': 'NOx sensor', '132': 'Manifold surface temperature', '133': 'NOx reagent system', '134': 'Particulate matter (PM) sensor', '135': 'Intake manifold absolute pressure', '136': 'SCR Induce System', '137': 'Run Time for AECD #11-#15', '138': 'Run Time for AECD #16-#20', '139': 'Diesel Aftertreatment', '140': 'O2 Sensor (Wide Range)', '141': 'Throttle Position G', '142': 'Engine Friction - Percent Torque', '143': 'PM Sensor Bank 1 & 2', '144': 'WWH-OBD Vehicle OBD System Information', '145': 'WWH-OBD Vehicle OBD System Information', '146': 'Fuel System Control', '147': 'WWH-OBD Vehicle OBD Counters support', '148': 'NOx Warning And Inducement System', '152': 'Exhaust Gas Temperature Sensor', '153': 'Exhaust Gas Temperature Sensor', '154': 'Hybrid/EV Vehicle System Data, Battery, Voltage', '155': 'Diesel Exhaust Fluid Sensor Data', '156': 'O2 Sensor Data', '157': 'Engine Fuel Rate', '158': 'Engine Exhaust Flow Rate', '159': 'Fuel System Percentage Use', '160': 'PIDs supported [$A1 - $C0]', '161': 'NOx Sensor Corrected Data', '162': 'Cylinder Fuel Rate', '163': 'Evap System Vapor Pressure', '164': 'Transmission Actual Gear', '165': 'Commanded Diesel Exhaust Fluid Dosing', '166': 'Odometer [c]', '167': 'NOx Sensor Concentration Sensors 3 and 4', '168': 'NOx Sensor Corrected Concentration Sensors 3 and 4', '169': 'ABS Disable Switch State', '192': 'PIDs supported [$C1 - $E0]', '195': '?', '196': '?'}

    return all_s01_pids[str(pid_num)].replace("\n", " ")


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()
    argparse_parser.add_argument("-i", "--canedge-mf4-file", type=str, required=True,
                                 help="The CanEdge MF4 data file containing the supported PIDs query")

    argparse_args = argparse_parser.parse_args()

    supported_pids = get_enabled_pids_from_file(argparse_args.canedge_mf4_file)

    print("Supported pids")
    print("--------------")
    print("PID num (hex) | PID num (int) | PID Name")

    # Read through the "master list" of PIDs
    pids_id_and_name = dict()

    for pid in supported_pids:

        pid_hex = "0x{:02x}".format(int(pid))
        print(f"{pid_hex} | {int(pid)}d | {get_pid_name_from_number(pid)}".format(hex(pid)))