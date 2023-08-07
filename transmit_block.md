Go to the section of your config.json file that starts with "transmit", and replace the contents of that array with the code below.

Remember that the '55555...' block is the "don't care" value for CanEdge.

This will probe your vehicle's ECU every 60 seconds to see which PIDs it responds to.

```
{
        "name": "S01_PID_enabled_0-32",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 10,
        "id": "7DF",
        "data": "0201005555555555"
      },
      {
        "name": "S01_PID_enab_33-64",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 20,
        "id": "7DF",
        "data": "0201205555555555"
      },
      {
        "name": "S01_PID_enab_65-96",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 30,
        "id": "7DF",
        "data": "0201405555555555"
      },
      {
        "name": "S01_PID_enabl_97-128",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 40,
        "id": "7DF",
        "data": "0201605555555555"
      },
      {
        "name": "S01_PID_enab_129-160",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 50,
        "id": "7DF",
        "data": "0201805555555555"
      },
      {
        "name": "S01_PID_enab_161-192",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 60,
        "id": "7DF",
        "data": "0201A05555555555"
      },
      {
        "name": "S01_PID_enab_193-224",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 70,
        "id": "7DF",
        "data": "0201C05555555555"
      },
      {
        "name": "S05_PIDs_enabled",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 80,
        "id": "7DF",
        "data": "0205005555555555"
      },
      {
        "name": "S09_PIDs_enabled",
        "state": 1,
        "id_format": 0,
        "frame_format": 0,
        "brs": 0,
        "log": 1,
        "period": 60000,
        "delay": 90,
        "id": "7DF",
        "data": "0209005555555555"
      }
```

# UDS

> Main article: https://en.wikipedia.org/wiki/Unified_Diagnostic_Services

The block below contains the transactions needed to send UDS messages, using the Service 0x22 (Read Data By Identifier).

for the list of DIDs used, see the `docs` folder.

```
{
  "name":"ECU_manufacturing_date_via_UDS",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60040,
  "delay":0,
  "id":"7E0",
  "data":"0322F18B55555555"
},
{
  "name":"ECU_serial_number_via_UDS",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60080,
  "delay":0,
  "id":"7E0",
  "data":"0322F18C55555555"
},
{
  "name":"VIN_lookup_example_2_using_UDS",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60090,
  "delay":0,
  "id":"7E0",
  "data":"0322F19055555555"
},
{
  "name":"Flow_control_for_VIN_2",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60100,
  "delay":10,
  "id":"7E0",
  "data":"3000000000000000"
},
{
  "name":"System_or_engine_name_via_UDS",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60110,
  "delay":0,
  "id":"7E0",
  "data":"0322F19755555555"
},
{
  "name":"programming_date_via_UDS",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60050,
  "delay":0,
  "id":"7E0",
  "data":"0322F19955555555"
},
{
  "name":"calibration_date_via_UDS",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60060,
  "delay":0,
  "id":"7E0",
  "data":"0322F19B55555555"
},
{
  "name":"ECU_installation_date_via_UDS",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60070,
  "delay":0,
  "id":"7E0",
  "data":"0322F19D55555555"
},
{
  "name":"UDS_version_data_identifier",
  "state":1,
  "id_format":0,
  "frame_format":0,
  "brs":0,
  "log":1,
  "period":60120,
  "delay":0,
  "id":"7E0",
  "data":"0322FF0055555555"
}
```