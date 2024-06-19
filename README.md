# CISCO PACKET TRACER TOPOLOGY MAKER
#### Video Demo: https://www.youtube.com/watch?v=widUMdEs4JY
#### Description:
The Cisco Packet Tracer Topology Maker is a tool designed to simplify the creation of network simulations within Cisco Packet Tracer. This program allows users to generate network topologies quickly and efficiently, making it an invaluable resource for networking students and professionals alike.

### How It Works
The program prompts the user for three key inputs:
- **Amount of devices**: Specify the number of devices (between 2 and 10).
- **Amount of switches**: Specify the number of switches (between 1 and 10).
- **Amount of cables**: Specify the number of cables (between 2 and 25).

Based on these inputs, users can select from five supported topologies:
- **Mesh**
- **Star**
- **Tree**
- **Ring**
- **Bus**

Once a topology is chosen, the program opens a pre-created CPT topology for further customization. All devices are automatically configured with IP addresses ranging from `10.0.0.1` to `10.0.0.10`. After a brief 30-second discovery period, users can interact with and modify the network (e.g., running pings between devices, adding new devices, etc.).

### Programs Needed to Run the Program:
- Python 3.6 or above
- Cisco Packet Tracer

### Additional Information About the Project:
This project contains the following files:
- **README.md**: Describes the project
- **cpt-topo-maker.py**: Main Python script that prompts user inputs and opens the selected pre-created topology
- **topos (folder/directory)**: Contains 39 topologies, varying by device amount and topology type

### Enhancing the Program with More Device Options and Topologies
To further improve the Cisco Packet Tracer Topology Maker, additional device options and topologies can be incorporated. By expanding the range of devices beyond the current 2 to 10 limit, users can create more complex and varied network simulations. Including a broader array of devices, such as routers, firewalls, and other networking equipment, would allow for more realistic and comprehensive network designs.

Moreover, adding new topology types can significantly enhance the program's versatility. While the current selection includes mesh, star, tree, ring, and bus topologies, introducing hybrid and custom topologies would provide users with even greater flexibility in designing their networks. Hybrid topologies, which combine elements of multiple standard topologies, can more accurately reflect real-world network configurations.

### Importance of Making Learning Networking Easier
Networking is a foundational skill in the IT field, and tools that simplify learning are invaluable. Cisco Packet Tracer, developed by Cisco, is one such tool that has revolutionized how networking concepts are taught and practiced. The Cisco Packet Tracer Topology Maker complements Cisco Packet Tracer by streamlining the process of creating network simulations. This synergy makes it easier for students and professionals to grasp complex networking concepts through hands-on practice.

Thank you to Cisco for creating Cisco Packet Tracer, and to me for making this program, for making it easier to create and work on topologies. Such tools democratize access to quality education and empower learners to experiment and innovate in a risk-free environment.

### Integration with AI for Enhanced Functionality
The potential integration of AI into the Cisco Packet Tracer Topology Maker could open up exciting new possibilities. By developing an API that allows direct manipulation of .pkt files from a Python script, the program could leverage AI to automate and optimize network configurations. AI algorithms could analyze network performance, predict potential issues, and suggest optimal configurations, making the deployment and testing of various topology options more efficient and effective.

For example, an AI-powered feature could recommend the best topology based on specific requirements or constraints, such as minimizing latency or maximizing redundancy. It could also automatically adjust configurations in real-time to adapt to changing network conditions, ensuring optimal performance and reliability.

In conclusion, the Cisco Packet Tracer Topology Maker is a powerful tool that simplifies the creation of network simulations, making it an excellent resource for learning and practicing networking. By expanding device options, adding new topologies, and integrating AI capabilities, this program can become even more versatile and impactful, helping users to design, deploy, and manage complex networks with ease.
