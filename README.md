# Tool Reset Machine ID

Tool buat reset Machine ID di Windows dan Linux. Tool ini bantu kamu generate Machine ID baru, yang bisa dipake buat berbagai keperluan kayak identifikasi sistem dan lisensi.

## ⚠️ Peringatan

- Jangan lupa backup data penting kamu sebelum pake tool ini ya
- Beberapa aplikasi mungkin perlu diinstall ulang setelah reset Machine ID
- Pastiin kamu udah paham konsekuensinya sebelum jalanin

## 🚀 Cara Cepet Pake

### Buat User Windows (Cara Online)

Jalanin command ini di PowerShell (Run as Administrator):
```powershell
irm https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/run_windows_online.ps1 | iex
```

### Buat User Linux

```bash
curl -o reset_machine_id.py https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/reset_machine_id.py
curl -o run.linux https://raw.githubusercontent.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID/main/run.linux
chmod +x run.linux
sudo ./run.linux
```

## 📋 Yang Diperluin

### Windows
- Windows 10/11
- PowerShell
- Python 3.x (bakal dicek dan diinstall otomatis kalo belum ada)

### Linux
- Python 3.x
- systemd (kebanyakan distro Linux modern)

## ⚙️ Cara Kerjanya

### Windows
- Ngubah MachineGuid di Windows Registry
- Bikin backup registry otomatis
- Reset Windows Identity
- Lokasinya di: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography`

### Linux
- Hapus machine-id yang ada
- Generate machine-id baru pake systemd-machine-id-setup
- Lokasinya di: `/etc/machine-id`

## 🔄 Setelah Reset

- Windows: Restart komputer kamu
- Linux: Beberapa service mungkin perlu di-restart

## 📝 Lisensi

Project ini pake lisensi MIT - cek file [LICENSE](LICENSE) buat detailnya.

## ⚠️ Disclaimer

Tool ini disediain apa adanya. Pake dengan resiko sendiri ya. Pembuat gak bertanggung jawab kalo ada masalah atau kerusakan yang terjadi karena pake tool ini.

## 🔗 Repository

[https://github.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID](https://github.com/ChasoulUIX/Cursor-AI-Reset-Machine-ID)

## 👨‍💻 Support Owner

- Instagram: [@chasoul.uix](https://instagram.com/chasoul.uix)
- Portfolio: [https://chasouluix.my.id](https://chasouluix.my.id) 