# WIFI-QR-Code-Generator
A clean and professional Python tool that generates beautiful Wi-Fi QR codes with your custom logo and a premium white circular ring.
One scan on any phone instantly connects users to your Wi-Fi network — no need to manually type the password.


## ✨ Features

Generates scannable Wi-Fi QR codes (WPA/WPA2/WPA3 supported)
Adds your custom logo in the center with a clean white circular ring for a modern, professional look
High error correction (ERROR_CORRECT_H) so the QR remains readable even with the logo
Professional outer border with subtle inner frame
Automatically saves the QR with timestamp and network name
Shows current working folder to avoid file location issues
High-quality output (sharp and print-ready)

## 📸 Preview

🚀 How to Use

Install the required librariesOpen your terminal and run:Bashpip install qrcode[pil]
Prepare your logo
Place your logo file in the same folder as the script
Rename it to logo.png (must be PNG format, preferably with transparent background)

Run the scriptBashpython WIFI QR generator.py
When prompted:
Enter your Wi-Fi Name (SSID)
Enter your Wi-Fi Password

The QR code will be generated and saved automatically in the same folder.

## 📁 Files

wifi_qr.py → Main script
logo.png → Your brand/logo (required for best results)
Generated files → wifi_qr_YourNetworkName_YYYYMMDD_HHMMSS.png

## ⚠️ Important Notes

The QR code contains your Wi-Fi password in plain text. Share it only with trusted guests.
For better security, consider using a Guest Wi-Fi network when sharing with many people.
Always test the QR code with both Android and iPhone cameras before printing or sharing.
The logo size is automatically set to 25% of the QR code (recommended safe range).

## 🎨 Customization Options
You can easily change:

Logo size (logo_size_percent)
Ring thickness
Outer border size
QR code colors (qr_color)
Output filename format

## Requirements

Python 3.6 or higher
Libraries: qrcode and Pillow

Example Output Filename
textwifi_qr_Home_Network_20260331_142530.png

