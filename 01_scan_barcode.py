import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def scan_barcode(image_path):
    image = cv2.imread(image_path)
    barcodes = decode(image)

    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(f"📦 Barcode Type: {barcode_type}")
        print(f"🔍 Barcode Data: {barcode_data}")
        return barcode_data

    print("❌ No barcode found.")
    return None

# Test it
if __name__ == "__main__":
    image_file = input("Enter path to medicine image (with barcode): ")
    result = scan_barcode(image_file)
    if result:
        print(f"✅ Scanned: {result}")
