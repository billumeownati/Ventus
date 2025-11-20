#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QTimer
import qtawesome as qta

def get_fan_data():
    if not shutil.which("sensors"):
        return [("ERROR", "'sensors' cmd not found"), ("HINT", "Install lm-sensors")]

    try:
        output = subprocess.check_output(["sensors"], text=True)
    except Exception as e:
        return [("ERROR", "Check console")]

    fan_data = []

    for line in output.splitlines():
        line = line.strip()
        if "fan" in line.lower() and ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                raw_key = parts[0].strip()
                raw_val = parts[1].strip()

                clean_key = raw_key.replace("_", " ").replace("input", "").strip().upper()

                if "FAN" not in clean_key:
                    clean_key += " FAN"

                fan_data.append((clean_key, raw_val))

    if not fan_data:
        return [("STATUS", "No fans detected")]

    return fan_data

class FanTray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setIcon(qta.icon("mdi.fan"))

        self.menu = QMenu()
        self.fan_actions = []

        self.bottom_separator = self.menu.addSeparator()

        self.restart_action = QAction("Restart App")
        self.restart_action.triggered.connect(self.restart_app)
        self.menu.addAction(self.restart_action)

        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(lambda: sys.exit(0))
        self.menu.addAction(self.quit_action)

        self.setContextMenu(self.menu)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(3000)

        self.update_ui()

    def update_ui(self):
        data = get_fan_data()

        tooltip_lines = [f"{k}: {v}" for k, v in data]
        self.setToolTip(" | ".join(tooltip_lines))

        if len(data) != len(self.fan_actions):
            self.rebuild_fan_actions(data)
        else:
            self.update_fan_actions(data)

    def rebuild_fan_actions(self, data):
        for action in self.fan_actions:
            self.menu.removeAction(action)

        self.fan_actions.clear()

        for key, value in data:
            display_text = f"{key}:  {value}"
            action = QAction(display_text)
            action.setEnabled(False)

            self.menu.insertAction(self.bottom_separator, action)
            self.fan_actions.append(action)

    def update_fan_actions(self, data):
        for i, (key, value) in enumerate(data):
            display_text = f"{key}:  {value}"
            if self.fan_actions[i].text() != display_text:
                self.fan_actions[i].setText(display_text)

    def restart_app(self):
        python = sys.executable
        os.execv(python, [python] + sys.argv)

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    tray = FanTray()
    tray.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
