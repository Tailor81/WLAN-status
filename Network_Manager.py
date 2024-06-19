import ctypes
import psutil
import subprocess
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class NetworkManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Network Manager")

        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the x and y coordinates to position the window to the top right corner
        window_width = 300
        window_height = 170
        x = screen_width - window_width
        y = 0

        # Set the geometry of the window
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        # Status label
        status_label = ttk.Label(self, text="Network Status:")
        status_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.wifi_status = ttk.Label(self, text="Wi-Fi: Unknown")
        self.wifi_status.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.ethernet_status = ttk.Label(self, text="Ethernet: Unknown")
        self.ethernet_status.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Enable/Disable Ethernet buttons
        enable_ethernet_button = ttk.Button(self, text="Enable Ethernet", command=self.enable_ethernet)
        enable_ethernet_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        disable_ethernet_button = ttk.Button(self, text="Disable Ethernet", command=self.disable_ethernet)
        disable_ethernet_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Enable/Disable Wi-Fi buttons
        enable_wifi_button = ttk.Button(self, text="Enable Wi-Fi", command=self.enable_wifi)
        enable_wifi_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        disable_wifi_button = ttk.Button(self, text="Disable Wi-Fi", command=self.disable_wifi)
        disable_wifi_button.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    def get_network_type(self):
        interfaces = psutil.net_if_addrs()
        connections = psutil.net_connections(kind='inet')

        wifi = False
        ethernet = False

        for interface in interfaces:
            for conn in connections:
                if conn.status == 'ESTABLISHED' and conn.laddr[0] in [addr.address for addr in interfaces[interface]]:
                    if 'Wi-Fi' in interface or 'Wireless' in interface or 'WLAN' in interface:
                        wifi = True
                    elif 'Ethernet' in interface:
                        ethernet = True

        return wifi, ethernet

    def toggle_ethernet(self, state):
        if state.lower() == 'on':
            shortcut_path = r"C:\Users\DarkTailor\Ethernet.lnk"
            if os.path.exists(shortcut_path):
                print(f"Executing shortcut at {shortcut_path}")  # Debug statement
                os.startfile(shortcut_path)
            else:
                print(f"Ethernet shortcut not found at {shortcut_path}")
        elif state.lower() == 'off':
            interface_name = self.get_interface_name('Ethernet')
            if interface_name:
                self.run_command(["netsh", "interface", "set", "interface", interface_name, "admin=disabled"])

    def toggle_wifi(self, state):
        interface_name = self.get_interface_name('Wi-Fi')
        if interface_name:
            if state.lower() == 'on':
                self.run_command(["netsh", "interface", "set", "interface", interface_name, "admin=enabled"])
            elif state.lower() == 'off':
                self.run_command(["netsh", "interface", "set", "interface", interface_name, "admin=disabled"])
        else:
            print("No Wi-Fi interface detected.")

    def get_interface_name(self, type_):
        interfaces = psutil.net_if_addrs()
        for interface in interfaces:
            if type_ in interface or type_.lower() in interface:
                print(f"Identified {type_} interface: {interface}")  # Debug statement
                return interface
        print(f"No {type_} interface found")  # Debug statement
        return None

    def run_command(self, command):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"Command '{' '.join(command)}' executed successfully. Output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Command '{' '.join(command)}' failed. Error: {e.stderr}")
            messagebox.showerror("Error", f"Failed to execute command. Error: {e.stderr}")

    def enable_ethernet(self):
        self.toggle_ethernet('on')
        self.update_status()

    def disable_ethernet(self):
        self.toggle_ethernet('off')
        self.update_status()

    def enable_wifi(self):
        self.toggle_wifi('on')
        self.update_status()

    def disable_wifi(self):
        self.toggle_wifi('off')
        self.update_status()

    def update_status(self):
        wifi, ethernet = self.get_network_type()
        self.wifi_status.config(text=f"Wi-Fi: {'Connected' if wifi else 'Not Connected'}")
        self.ethernet_status.config(text=f"Ethernet: {'Connected' if ethernet else 'Not Connected'}")

        # Schedule the next status update
        self.after(2000, self.update_status)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        app = NetworkManagerApp()
        app.mainloop()
    else:
        if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    run_as_admin()
