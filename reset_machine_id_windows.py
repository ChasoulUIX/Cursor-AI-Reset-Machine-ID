#!/usr/bin/env python3
import winreg
import uuid
import sys
import ctypes

def print_banner():
    banner = """
 ██████╗██╗  ██╗ █████╗ ███████╗ ██████╗ ██╗   ██╗██╗     ██╗   ██╗██╗██╗  ██╗
██╔════╝██║  ██║██╔══██╗██╔════╝██╔═══██╗██║   ██║██║     ██║   ██║██║╚██╗██╔╝
██║     ███████║███████║███████╗██║   ██║██║   ██║██║     ██║   ██║██║ ╚███╔╝ 
██║     ██╔══██║██╔══██║╚════██║██║   ██║██║   ██║██║     ██║   ██║██║ ██╔██╗ 
╚██████╗██║  ██║██║  ██║███████║╚██████╔╝╚██████╔╝███████╗╚██████╔╝██║██╔╝ ██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
    """
    print("\033[95m" + banner + "\033[0m")  # Warna ungu
    print("\033[93m" + "Support Owner:".center(80) + "\033[0m")  # Warna kuning
    print("\033[96m" + "Instagram: @chasoul.uix".center(80) + "\033[0m")  # Warna cyan
    print("\033[96m" + "Portfolio: https://chasouluix.my.id".center(80) + "\033[0m")  # Warna cyan
    print("\033[92m" + "=" * 80 + "\033[0m\n")  # Garis pemisah hijau

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def reset_machine_id():
    if not is_admin():
        print("Error: This script must be run as Administrator")
        print("Please right-click and select 'Run as administrator'")
        sys.exit(1)

    try:
        # Path to MachineGuid in Windows Registry
        key_path = r"SOFTWARE\Microsoft\Cryptography"
        
        # Open registry key
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
        
        # Generate new GUID
        new_guid = str(uuid.uuid4())
        
        # Set new MachineGuid
        winreg.SetValueEx(key, "MachineGuid", 0, winreg.REG_SZ, new_guid)
        
        # Close registry key
        winreg.CloseKey(key)
        
        print("Successfully reset Windows Machine GUID")
        print("\nNote: You may need to restart your computer for changes to take effect")
        
    except Exception as e:
        print(f"Error resetting Windows Machine GUID: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print_banner()
    reset_machine_id() 