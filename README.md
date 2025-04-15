# Machine ID Reset Tool

A tool to reset machine ID on both Windows and Linux systems. This tool helps you generate a new machine ID, which can be useful for various purposes such as system identification and licensing.

## ⚠️ Warning

- Always backup your important data before using this tool
- Some applications might need to be reinstalled after resetting machine ID
- Make sure you understand the implications before proceeding

## 🚀 Quick Start

### For Windows Users

1. Download the Windows version:
   ```powershell
   curl -o reset_machine_id_windows.py https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/reset_machine_id_windows.py
   curl -o run.windows https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/run.windows
   ```

2. Run as Administrator:
   - Right-click on `run.windows`
   - Select "Run as administrator"

### For Linux Users

1. Download the Linux version:
   ```bash
   curl -o reset_machine_id.py https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/reset_machine_id_linux.py
   curl -o run.linux https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/run.linux
   chmod +x run.linux
   ```

2. Run with sudo:
   ```bash
   sudo ./run.linux
   ```

## 📋 Requirements

- Python 3.x
- Administrator/Root privileges
- Windows: `pywin32` package (`pip install pywin32`)
- Linux: `systemd` (most modern Linux distributions)

## 🔧 Installation

### Windows
```powershell
# Install required Python package
pip install pywin32
```

### Linux
```bash
# Make sure systemd is installed (usually pre-installed)
sudo apt-get update
sudo apt-get install systemd
```

## ⚙️ How it Works

### Windows
- Modifies the MachineGuid in Windows Registry
- Located at: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography`

### Linux
- Removes existing machine-id
- Generates new machine-id using systemd-machine-id-setup
- Located at: `/etc/machine-id`

## 🔄 After Reset

- Windows: Restart your computer
- Linux: Some services might need to be restarted

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is provided as-is. Use at your own risk. The authors are not responsible for any damage or issues that may arise from using this tool.

## 🔗 Repository

[https://github.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID](https://github.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID) 