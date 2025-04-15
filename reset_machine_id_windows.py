#!/usr/bin/env python3
import winreg
import uuid
import sys
import ctypes

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
    reset_machine_id() 