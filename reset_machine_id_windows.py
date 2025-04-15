#!/usr/bin/env python3
import winreg
import uuid
import sys
import ctypes
import os
import datetime
import subprocess

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

def backup_registry():
    try:
        backup_dir = os.path.expanduser("~\\Desktop\\Registry_Backup")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        backup_file = os.path.join(backup_dir, f"registry_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.reg")
        subprocess.run(['reg', 'export', 'HKLM\\SOFTWARE\\Microsoft\\Cryptography', backup_file], check=True)
        print(f"\n✅ Registry backup created at: {backup_file}")
        return True
    except Exception as e:
        print(f"\n⚠️ Warning: Could not create registry backup: {e}")
        return False

def reset_machine_id():
    if not is_admin():
        print("\n❌ Error: This script must be run as Administrator")
        print("Please right-click and select 'Run as administrator'")
        sys.exit(1)

    print("\n🔄 Starting Machine ID reset process...")
    
    # Backup registry first
    backup_registry()
    
    try:
        # Reset MachineGuid
        crypto_key_path = r"SOFTWARE\Microsoft\Cryptography"
        crypto_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, crypto_key_path, 0, winreg.KEY_ALL_ACCESS)
        new_guid = str(uuid.uuid4())
        winreg.SetValueEx(crypto_key, "MachineGuid", 0, winreg.REG_SZ, new_guid)
        winreg.CloseKey(crypto_key)
        print("✅ Successfully reset MachineGuid")

        # Reset additional machine-specific identifiers
        try:
            # Reset Windows Identity
            subprocess.run(['net', 'stop', 'TokenBroker'], check=False)
            identity_path = os.path.expandvars("%SystemDrive%\\Windows\\ServiceProfiles\\LocalService\\AppData\\Local\\Microsoft\\Windows\\Identity")
            if os.path.exists(identity_path):
                for file in os.listdir(identity_path):
                    if file.endswith(".dat"):
                        os.remove(os.path.join(identity_path, file))
            print("✅ Successfully reset Windows Identity")
        except Exception as e:
            print(f"⚠️ Warning: Could not reset Windows Identity: {e}")

        print("\n✅ Machine ID reset completed successfully!")
        print("\n⚠️ Important Notes:")
        print("1. Please restart your computer for changes to take effect")
        print("2. Some applications might need to be reactivated")
        print("3. A registry backup has been created on your Desktop")
        
    except Exception as e:
        print(f"\n❌ Error resetting Machine ID: {e}")
        print("If you need to restore the registry, use the backup file created on your Desktop")
        sys.exit(1)

if __name__ == "__main__":
    print_banner()
    reset_machine_id() 