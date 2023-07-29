Go to the section that starts with "transmit", and replace the contents of that array with the code below.

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