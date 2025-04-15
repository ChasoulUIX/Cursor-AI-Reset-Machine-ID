# Display banner
$banner = @"
 ██████╗██╗  ██╗ █████╗ ███████╗ ██████╗ ██╗   ██╗██╗     ██╗   ██╗██╗██╗  ██╗
██╔════╝██║  ██║██╔══██╗██╔════╝██╔═══██╗██║   ██║██║     ██║   ██║██║╚██╗██╔╝
██║     ███████║███████║███████╗██║   ██║██║   ██║██║     ██║   ██║██║ ╚███╔╝ 
██║     ██╔══██║██╔══██║╚════██║██║   ██║██║   ██║██║     ██║   ██║██║ ██╔██╗ 
╚██████╗██║  ██║██║  ██║███████║╚██████╔╝╚██████╔╝███████╗╚██████╔╝██║██╔╝ ██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
"@

Write-Host $banner -ForegroundColor Magenta
Write-Host "`nSupport Owner:" -ForegroundColor Yellow
Write-Host "Instagram: @chasoul.uix" -ForegroundColor Cyan
Write-Host "Portfolio: https://chasouluix.my.id" -ForegroundColor Cyan
Write-Host "`n" + ("=" * 80) -ForegroundColor Green
Write-Host "`n"

# Create a temporary Python script with enhanced output
$pythonCode = @"
import winreg
import uuid
import sys
import ctypes
import os
import datetime
import subprocess
import json

def print_success(message):
    print(f"\033[92m✅ {message}\033[0m")

def print_warning(message):
    print(f"\033[93m⚠️ {message}\033[0m")

def print_error(message):
    print(f"\033[91m❌ {message}\033[0m")

def print_info(message):
    print(f"\033[96mℹ️ {message}\033[0m")

def get_current_machine_id():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_READ)
        current_id = winreg.QueryValueEx(key, "MachineGuid")[0]
        winreg.CloseKey(key)
        return current_id
    except:
        return "Unknown"

def backup_registry():
    try:
        backup_dir = os.path.expanduser("~\\Desktop\\Registry_Backup")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        backup_file = os.path.join(backup_dir, f"registry_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.reg")
        subprocess.run(['reg', 'export', 'HKLM\\SOFTWARE\\Microsoft\\Cryptography', backup_file], check=True)
        print_success(f"Registry backup created at: {backup_file}")
        return True
    except Exception as e:
        print_warning(f"Could not create registry backup: {e}")
        return False

def reset_machine_id():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print_error("This script must be run as Administrator")
        print_info("Please right-click and select 'Run as administrator'")
        sys.exit(1)

    print_info("Starting Machine ID reset process...")
    
    # Get current Machine ID
    old_id = get_current_machine_id()
    print_info(f"Current Machine ID: {old_id}")
    
    # Backup registry first
    backup_registry()
    
    try:
        # Reset MachineGuid
        crypto_key_path = r"SOFTWARE\Microsoft\Cryptography"
        crypto_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, crypto_key_path, 0, winreg.KEY_ALL_ACCESS)
        new_guid = str(uuid.uuid4())
        winreg.SetValueEx(crypto_key, "MachineGuid", 0, winreg.REG_SZ, new_guid)
        winreg.CloseKey(crypto_key)
        print_success(f"Successfully reset MachineGuid to: {new_guid}")

        # Reset additional machine-specific identifiers
        try:
            # Reset Windows Identity
            subprocess.run(['net', 'stop', 'TokenBroker'], check=False)
            identity_path = os.path.expandvars("%SystemDrive%\\Windows\\ServiceProfiles\\LocalService\\AppData\\Local\\Microsoft\\Windows\\Identity")
            if os.path.exists(identity_path):
                for file in os.listdir(identity_path):
                    if file.endswith(".dat"):
                        os.remove(os.path.join(identity_path, file))
                print_success("Successfully reset Windows Identity files")
        except Exception as e:
            print_warning(f"Could not reset Windows Identity: {e}")

        print_success("Machine ID reset completed successfully!")
        print("\nChanges made:")
        print(f"1. Old Machine ID: {old_id}")
        print(f"2. New Machine ID: {new_guid}")
        print("3. Windows Identity files reset")
        print("\nImportant Notes:")
        print("1. Please restart your computer for changes to take effect")
        print("2. Some applications might need to be reactivated")
        print("3. A registry backup has been created on your Desktop")
        
    except Exception as e:
        print_error(f"Error resetting Machine ID: {e}")
        print_info("If you need to restore the registry, use the backup file created on your Desktop")
        sys.exit(1)

if __name__ == "__main__":
    reset_machine_id()
"@

# Save the Python code to a temporary file
$tempFile = [System.IO.Path]::GetTempFileName() + ".py"
$pythonCode | Out-File -FilePath $tempFile -Encoding UTF8

# Run the Python script with admin privileges
Start-Process -Verb RunAs powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command `"python '$tempFile'; Remove-Item '$tempFile' -Force`"" 