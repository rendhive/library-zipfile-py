import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.printdir()
# Fungsi: Mencetak daftar file dan direktori dalam arsip ZIP.
# Kondisi: Ketika Anda ingin melihat struktur lengkap dari file ZIP secara langsung.
