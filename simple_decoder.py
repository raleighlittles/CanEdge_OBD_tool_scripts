import asammdf
import argparse
import pdb


if __name__ == "__main__":
    argparse_parser = argparse.ArgumentParser()
    argparse_parser.add_argument("-i", "--canedge-mf4-file", type=str, required=True,
                                 help="The CanEdge MF4 data file you want to parse")

    argparse_args = argparse_parser.parse_args()

    can_database_files = {
        "CAN": [("./dbc/CSS-Electronics-OBD2-v1.4.dbc", 0), ("./dbc/CSS-Electronics-OBD2-Extended-v1.4.dbc", 0), ("/home/raleigh/github/others/opendbc/nissan_leaf_2018_generated.dbc", 0)]
    }


    mdf = asammdf.MDF(argparse_args.canedge_mf4_file, use_display_names=True)

    extracted_mdf = mdf.extract_bus_logging(
        database_files=can_database_files).to_dataframe()
    
    pdb.set_trace()