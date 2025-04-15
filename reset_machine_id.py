#!/usr/bin/env python3
import subprocess
import os
import sys

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

def check_root():
    if os.geteuid() != 0:
        print("Error: This script must be run as root (sudo)")
        sys.exit(1)

def reset_machine_id():
    try:
        # Remove existing machine-id
        subprocess.run(['rm', '/etc/machine-id'], check=True)
        print("Successfully removed /etc/machine-id")
        
        # Generate new machine-id
        subprocess.run(['systemd-machine-id-setup'], check=True)
        print("Successfully generated new machine-id")
        
        print("\nMachine ID has been successfully reset!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print_banner()
    check_root()
    reset_machine_id() 