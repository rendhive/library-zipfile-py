import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extract('file1.txt', 'custom_extracted')
print("File 'file1.txt' berhasil diekstrak ke 'custom_extracted'.")
# Fungsi: Mengekstrak file tertentu ke direktori yang ditentukan.
# Kondisi: Ketika Anda ingin mengekstrak file ke lokasi khusus.
