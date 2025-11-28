import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extract('file1.txt', 'extracted_files')
print("file1.txt berhasil diekstrak.")
# Fungsi: Mengekstrak file tertentu dari arsip ZIP.
# Kondisi: Ketika Anda hanya ingin mendapatkan file tertentu dari ZIP.
