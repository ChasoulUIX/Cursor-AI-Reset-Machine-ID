#!/usr/bin/env python3
import subprocess
import os
import sys
import datetime

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

def print_success(message):
    print(f"\033[92m✅ {message}\033[0m")

def print_warning(message):
    print(f"\033[93m⚠️ {message}\033[0m")

def print_error(message):
    print(f"\033[91m❌ {message}\033[0m")

def print_info(message):
    print(f"\033[96mℹ️ {message}\033[0m")

def check_root():
    if os.geteuid() != 0:
        print_error("This script must be run as root (sudo)")
        sys.exit(1)

def get_current_machine_id():
    try:
        with open('/etc/machine-id', 'r') as f:
            return f.read().strip()
    except:
        return "Unknown"

def backup_machine_id():
    try:
        backup_dir = os.path.expanduser("~/Desktop/MachineID_Backup")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        backup_file = os.path.join(backup_dir, f"machine-id_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
        subprocess.run(['cp', '/etc/machine-id', backup_file], check=True)
        print_success(f"Machine ID backup created at: {backup_file}")
        return True
    except Exception as e:
        print_warning(f"Could not create machine ID backup: {e}")
        return False

def reset_machine_id():
    try:
        print_info("Starting Machine ID reset process...")
        
        # Get current Machine ID
        old_id = get_current_machine_id()
        print_info(f"Current Machine ID: {old_id}")
        
        # Backup current machine-id
        backup_machine_id()
        
        # Remove existing machine-id
        subprocess.run(['rm', '/etc/machine-id'], check=True)
        print_success("Successfully removed /etc/machine-id")
        
        # Generate new machine-id
        subprocess.run(['systemd-machine-id-setup'], check=True)
        new_id = get_current_machine_id()
        print_success(f"Successfully generated new machine-id: {new_id}")
        
        print_success("Machine ID reset completed successfully!")
        print("\nChanges made:")
        print(f"1. Old Machine ID: {old_id}")
        print(f"2. New Machine ID: {new_id}")
        print("\nImportant Notes:")
        print("1. Some services might need to be restarted")
        print("2. A backup of your old machine ID has been created")
        print("3. Some applications might need to be reactivated")
        
    except subprocess.CalledProcessError as e:
        print_error(f"Error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print_banner()
    check_root()
    reset_machine_id() 