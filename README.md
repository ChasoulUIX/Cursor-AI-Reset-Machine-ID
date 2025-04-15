# Machine ID Reset Tool

A tool to reset machine ID on both Windows and Linux systems. This tool helps you generate a new machine ID, which can be useful for various purposes such as system identification and licensing.

## ⚠️ Warning

- Always backup your important data before using this tool
- Some applications might need to be reinstalled after resetting machine ID
- Make sure you understand the implications before proceeding

## 🚀 Quick Start

### Windows Users (Online Method)

Run this command in PowerShell (Run as Administrator):
```powershell
irm https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/run_windows_online.ps1 | iex
```

### Linux Users

```bash
curl -o reset_machine_id.py https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/reset_machine_id.py
curl -o run.linux https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/run.linux
chmod +x run.linux
sudo ./run.linux
```

## 📋 Requirements

### Windows
- Windows 10/11
- PowerShell
- Python 3.x (will be checked and installed automatically if needed)

### Linux
- Python 3.x
- systemd (most modern Linux distributions)

## ⚙️ How it Works

### Windows
- Modifies the MachineGuid in Windows Registry
- Creates automatic registry backup
- Resets Windows Identity
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

## 👨‍💻 Support Owner

- Instagram: [@chasoul.uix](https://instagram.com/chasoul.uix)
- Portfolio: [https://chasouluix.my.id](https://chasouluix.my.id) 