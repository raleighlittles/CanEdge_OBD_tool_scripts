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

    num_files_converted = 0

    for candidate_filename in os.listdir(argparse_args.input_directory):

        if candidate_filename.lower().endswith(".mf4"):

            mf4_file_path = os.path.join(argparse_args.input_directory, candidate_filename)
            print(f"[DEBUG] Converting {candidate_filename} to CSV(s) | File size = {os.path.getsize(mf4_file_path)} bytes")

            mdf_obj = asammdf.MDF(mf4_file_path, use_display_names=True)

            # There will be multiple CSV files created for each MF4; one for each channel
            csv_file_directory = os.path.join(argparse_args.output_directory, candidate_filename)
            os.makedirs(csv_file_directory, exist_ok=False)

            mdf_obj.export(fmt="csv", filename=os.path.join(csv_file_directory, candidate_filename))
            num_files_converted += 1

    print(f"Finished converting {num_files_converted} files to CSV")