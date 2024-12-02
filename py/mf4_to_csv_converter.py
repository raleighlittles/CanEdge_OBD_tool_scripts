import asammdf
import argparse
import os

if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser("Tool to convert MF4 files to CSV files in a given directory")
    argparse_parser.add_argument("-i", "---input-directory", type=str, required=True, help="The directory containing the MF4 files you want to convert to CSV")
    argparse_parser.add_argument("-o", "--output-directory", type=str, required=True, help="The directory where the CSV files will be saved")

    argparse_args = argparse_parser.parse_args()

    if not os.path.exists(argparse_args.input_directory):
        raise FileNotFoundError(f"Error! The MF4 directory '{argparse_args.input_directory}' does not exist")
    
    if not os.path.exists(argparse_args.output_directory):
        os.makedirs(argparse_args.output_directory, exist_ok=False)

    for filename in os.listdir(argparse_args.input_directory):
        if filename.lower().endswith(".mf4"):

            mf4_file_path = os.path.join(argparse_args.input_directory, filename)
            print(f"[DEBUG] Converting {filename} to CSV | File size = {os.path.getsize(mf4_file_path)} bytes")

            mdf_obj = asammdf.MDF(mf4_file_path, use_display_names=True)

            csv_filename = filename + ".csv"
            csv_file_path = os.path.join(argparse_args.output_directory, csv_filename)

            mdf_obj.export(fmt="csv", filename=csv_file_path)

