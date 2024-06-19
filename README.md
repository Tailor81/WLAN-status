# Network Manager
Overview
Network Manager is a user-friendly application designed to simplify the process of switching between Ethernet and Wi-Fi connections. This tool is particularly useful for organizations where users frequently need to switch network connections but lack the proficiency to navigate through the control panel settings.

# Problem Statement
Many users in organizations face challenges when switching between Ethernet and Wi-Fi connections. This is often required to access different resources such as servers on Ethernet and the internet via Wi-Fi. Manually enabling or disabling network interfaces through the control panel can be cumbersome and requires a certain level of technical proficiency, which many users lack. Network Manager addresses this issue by providing a simple graphical interface to manage network connections easily.

# Features
Display Network Status: Shows the current status of both Wi-Fi and Ethernet connections.
Enable/Disable Network Interfaces: Allows users to enable or disable Wi-Fi and Ethernet connections with the click of a button.
Automatic Status Updates: Periodically updates the status of network connections.

# Requirements
Operating System: Windows
Administrative Privileges: The application requires administrative privileges to manage network interfaces.
Python (for source code execution): Python 3.x
Python Packages: psutil, tkinter

# Installation and Execution
Running from Source Code
Ensure Python is Installed:
Ensure you have Python 3 installed on your system. You can download it from python.org.

Install Required Packages:
Open a command prompt and install the required packages using pip:
pip install psutil

Download the Source Code:
Download the Network_Manager.py file and save it to a convenient location.

Run the Script as Administrator:
The script requires administrative privileges to manage network interfaces. Run the script with elevated permissions:
python Network_Manager.py

# Running the Executable
Locate the Executable:
The NetworkManager.exe file is located in the lib folder. This is a standalone executable and does not require Python to be installed on the system.

Run the Executable as Administrator:
Right-click on the NetworkManager.exe file and select "Run as administrator" to ensure it has the necessary privileges to manage network interfaces.
 
# Conclusion
Network Manager provides a straightforward solution for users to manage their network connections without delving into complex control panel settings. This tool enhances productivity by simplifying the process of switching between Ethernet and Wi-Fi, especially in environments where such tasks are frequent.