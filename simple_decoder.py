import asammdf
import argparse
import pdb
import typing
import collections


def get_frequency_counts_of_data(raw_mdf_dataframe, column_names) -> typing.List:

    data_freq_list = list()

    for column in column_names:

        print("==========")

        column_data_indexed = dict()

        df_column_as_list = raw_mdf_dataframe[column].to_list()

        for idx, incoming_bytes in enumerate(df_column_as_list):

            # Lists are not a hashable type, but tuples are
            column_data_indexed[str(idx)] = tuple(incoming_bytes.tolist())

        column_data_frequencied = collections.Counter(column_data_indexed.values())

        txt_filename = str(column) + ".txt"
        with open(txt_filename, 'w') as txt_file:
            for data, frequency in column_data_frequencied.most_common():
                print(f"{data}, {frequency}", file=txt_file)

        #print(column_data_frequencied)
        print("==========")
        data_freq_list.append(column_data_frequencied)

    return data_freq_list

if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-i", "--canedge-mf4-file", type=str, required=True,
                                 help="The CanEdge MF4 data file you want to parse")

    argparse_args = argparse_parser.parse_args()

    # can_database_files = {
    #     "CAN": [("./dbc/CSS-Electronics-OBD2-v1.4.dbc", 0), ("./dbc/CSS-Electronics-OBD2-Extended-v1.4.dbc", 0), ("/home/raleigh/github/others/opendbc/nissan_leaf_2018_generated.dbc", 0)]
    # }
    # can_database_files = {
    #     "CAN": [("./dbc/2018-Nissan-Versa.dbc", 0)]
    # }
    # can_database_files = {
    #      "CAN": [("./dbc/CSS-Electronics-OBD2-v1.4.dbc", 0), ("./dbc/CSS-Electronics-OBD2-Extended-v1.4.dbc", 0), ("./dbc/2018_Nissan-Versa.dbc", 0)]
    # }
    can_database_files = {
        "CAN": [("./dbc/CSS-Electronics-OBD2-v1.4_withS9.dbc", 0), ("./dbc/CSS-Electronics-OBD2-Extended-v1.4_withS9.dbc", 0), ("./dbc/2018_Nissan-Versa.dbc", 0)]
    }

    input_file = argparse_args.canedge_mf4_file

    mdf = asammdf.MDF(input_file, use_display_names=True)

    csv_raw_traffic_filename = input_file + "ORIGINAL.csv"

    #mdf.to_dataframe().to_csv(csv_raw_traffic_filename)
    raw_traffic_mdf = mdf.to_dataframe()


    #freq_counts = get_frequency_counts_of_data(raw_traffic_mdf, ["CAN_DataFrame.CAN_DataFrame.DataBytes", "CAN_DataFrame.CAN_DataFrame.DataBytes_0"])

    extracted_mdf = mdf.extract_bus_logging(
        database_files=can_database_files).to_dataframe()
    
    pdb.set_trace()
    
    # extracted_mdf.to_csv(input_file + ".csv")


