import pdb

import asammdf
mdf = asammdf.MDF("/mnt/shares/canedge_mdf4_files/data/20230619033840_versa.MF4")
databases = {
    "CAN": [("/home/raleigh/github/CanEdge_OBD_Organizer/CSS-Electronics-OBD2-v1.4.dbc", 0), ("/home/raleigh/github/CanEdge_OBD_Organizer/CSS-Electronics-OBD2-Extended-v1.4.dbc", 0)]
}

extracted_mdf = mdf.extract_bus_logging(database_files=databases)
extracted_mdf.to_dataframe()

pdb.set_trace()