import qrcode
from PIL import Image, ImageDraw
from datetime import datetime
import os


current_folder = os.getcwd()
print("=" * 70)
print("📁 CURRENT FOLDER:")
print(f"   {current_folder}")
print("→ Make sure 'logo.png' is in this folder!")
print("=" * 70)


print("\n=== Wi-Fi QR Code Generator ===\n")

ssid = input("Enter Wi-Fi Name (SSID): ").strip()
password = input("Enter Wi-Fi Password: ").strip()

# Security type: Usually "WPA" works for both WPA2 and WPA3
security = "WPA"

# Optional: Add "R:1;" if your network is WPA3-only (most people can leave it as is)
wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

print(f"\nGenerating Wi-Fi QR for network: {ssid}")

# ====================== SETTINGS ======================
logo_path = "logo.png"
output_filename = f"wifi_qr_{ssid.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

qr_color = "black"
bg_color = "white"
logo_size_percent = 0.25          # 25% of QR width (safe range 20-30%)
outer_border = 50
ring_thickness = 12

# ====================== GENERATE QR CODE ======================
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,   # High for logo
    box_size=12,
    border=4,
)

qr.add_data(wifi_data)
qr.make(fit=True)

img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert("RGB")
qr_width, qr_height = img.size

# ====================== ADD WHITE CIRCULAR RING + LOGO ======================
try:
    logo = Image.open(logo_path).convert("RGBA")
    logo_size = int(qr_width * logo_size_percent)
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

    # White circular ring
    ring_size = logo_size + ring_thickness * 2
    ring = Image.new("RGBA", (ring_size, ring_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(ring)
    draw.ellipse([0, 0, ring_size, ring_size], fill="white")

    # Paste ring then logo in center
    ring_pos = ((qr_width - ring_size) // 2, (qr_height - ring_size) // 2)
    img.paste(ring, ring_pos, mask=ring)

    logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    img.paste(logo, logo_pos, mask=logo)
    
    print(f"✅ Logo + white circular ring added successfully!")

except FileNotFoundError:
    print(f"⚠️ Logo file '{logo_path}' not found. QR generated without logo.")
    print("   Tip: Put your logo.png in the folder shown above.")

except Exception as e:
    print(f"⚠️ Logo error: {e}")

# ====================== ADD OUTER BORDER ======================
final_size = (qr_width + 2 * outer_border, qr_height + 2 * outer_border)
final_img = Image.new("RGB", final_size, color=bg_color)
final_img.paste(img, (outer_border, outer_border))

# Thin inner frame for premium look
draw = ImageDraw.Draw(final_img)
draw.rectangle(
    [outer_border-3, outer_border-3, 
     final_img.size[0]-outer_border+2, final_img.size[1]-outer_border+2],
    outline="#E5E7EB", width=6
)

# ====================== SAVE ======================
final_img.save(output_filename, quality=95)

print(f"\n🎉 Wi-Fi QR Code created successfully!")
print(f"   📁 Saved as: {output_filename}")
print(f"   📍 Location: {current_folder}")
print(f"   🔗 Network: {ssid}")
print("\n✅ Test it: Open your phone camera and scan the QR code — it should prompt to connect to Wi-Fi.")