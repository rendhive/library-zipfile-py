import zipfile

try:
    with zipfile.ZipFile('archive.zip', 'r') as zipf:
        zipf.testzip()  # Memeriksa setiap file
    print("File ZIP valid dan tidak korup.")
except zipfile.BadZipFile:
    print("File ZIP tidak valid atau korup.")
# Fungsi: Memeriksa validitas file ZIP.
# Kondisi: Ketika Anda ingin memastikan integritas arsip ZIP.
