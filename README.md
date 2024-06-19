# CISCO PACKET TRACER TOPOLOGY MAKER
#### Video Demo: https://www.youtube.com/watch?v=widUMdEs4JY
#### Description:
This program was made to ease the creation of network simulation inside Cisco Packer tracer.
It asks for 3 prompts:
- Amount of devices (*2 to 10*)
- Amount of switches (*1 to 10*)
- Amount of cables (*2 to 25*)

Based on that information, you will be asked to choose one of 5 supported topologies:
- mesh
- star
- tree
- ring
- bus

After making a choice, the program will open one of pre-created CPT topologies for you to customize.
All devices have automatically configured to use IP range `10.0.0.1` to `10.0.0.10`, and after 30 seconds
of discovery, you will be able to **interact and change it** (run ping between devices, add new devices, etc.)

#### Programs needed to run the program:
- Python 3.6 or above
- Cisco Packet Tracer

#### Additional information about the project:
This project contains these files:
- **README.md** - describes this project
- **cpt-topo-maker.py** - main Python script that asks for prompts and opens one of pre-created topologies for you
- **topos (folder/directory)** - used to store 39 topologies, varying by device amount and topology type
