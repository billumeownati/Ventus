# 🌬️ Ventus

> **The minimalist fan speed monitor for Linux.**

**Ventus** is a sleek system tray application that brings real-time hardware fan monitoring to your Linux desktop. 

Designed to be unobtrusive and lightweight, it sits quietly in your system tray, acting as a modern GUI bridge for the powerful `lm-sensors` utility. Whether you are diagnosing airflow issues or just like keeping an eye on your thermals, Ventus provides the data you need without the clutter.



## ✨ Features

- **Real-time Metrics:** Polls hardware sensors every 1.5 seconds for up-to-date RPM readings.
- **Smart Discovery:** Automatically detects active fans (CPU, GPU, Chassis) and adapts the menu dynamically.
- **Zero Configuration:** No config files or setup wizards. It just works.
- **Intelligent Formatting:** Transforms raw sensor IDs (e.g., `fan1_input`) into human-readable labels (e.g., `CPU FAN`).
- **Native Integration:** Uses system theme icons to blend perfectly with GNOME, KDE, XFCE, and other desktop environments.
- **Resource Efficient:** Built with Python and PyQt6 to remain lightweight in the background.

## 🛠️ Prerequisites

Ventus relies on standard Linux hardware monitoring tools. Ensure you have the following installed:

1.  **Python 3.8+**
2.  **lm-sensors** (The core utility for reading hardware chips)
3.  **PyQt6** (The GUI framework)

## 📦 Installation

### 1. Install System Dependencies

First, install `lm-sensors`.

**Debian / Ubuntu / Mint:**
```bash
sudo apt update
sudo apt install lm-sensors python3-pip
```
**Fedora:**
```bash
sudo dnf install lm_sensors python3-pip
```
**Arch Linux:**
```bash
sudo pacman -S lm_sensors python-pip
```

### 2. Detect Sensors (Important!)

If you haven't done this before, you must tell Linux to scan your motherboard for sensors:
```bash
sudo sensors-detect
```
- Tip: You can generally press `ENTER` to accept the defaults (YES) for all questions. A reboot may be required after this step.

### 3. Install Python Libraries
```bash
pip install pyqt6 qtawesome
```

### 4. Clone & Run
```bash
git clone https://github.com/billumeownati/Ventus.git
cd Ventus
python3 code.py
```

## 🚀 Usage

Once running, Ventus lives in your system tray.

- **Hover:** See a quick pipe-separated summary (e.g., `CPU FAN: 1200 RPM | GPU: 0 RPM`).
- **Click:** Open the detailed menu to see all detected fans listed individually.
- **Dynamic Updates:** If a fan stops or starts (common with GPU "0dB" modes), the menu updates automatically.

## ❓ Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **"No fans detected"** | Run `sensors` in a terminal. If it's empty, run `sudo sensors-detect` again or check your BIOS settings. |
| **"sensors cmd not found"** | You are missing the base package. Install `lm-sensors`. |
| **ModuleNotFoundError** | Ensure you installed PyQt6 via `pip install PyQt6` or your distro's package manager. |

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ for the Linux community.
</p>