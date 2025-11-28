import zipfile
import os

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted_files')
print("Semua file berhasil diekstrak ke dalam folder 'extracted_files'.")
# Fungsi: Mengekstrak semua file dari arsip ZIP ke direktori tertentu.
# Kondisi: Ketika Anda ingin mendekompresi semua isi dari ZIP ke cara yang terpisah.
