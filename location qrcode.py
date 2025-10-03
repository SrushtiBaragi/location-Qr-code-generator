import qrcode

# Enter the location (Google Maps link or latitude/longitude)
# Example: Bengaluru, India
location = "https://maps.app.goo.gl/NGxfk57nGerNJXx27?g_st=aw"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(location)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image
img.save("location_qr.png")

print("QR code generated and saved as location_qr.png")
import os

file_path = os.path.abspath("location_qr.png")
img.save(file_path)

print("✅ QR code saved at:", file_path)

# Auto-open (Windows only)
os.startfile(file_path)
