import zipfile

with zipfile.ZipFile('compressed_archive.zip', 'r') as zipf:
    zipf.extractall('extracted_compressed')
print("Semua file dari ZIP terkompresi diekstrak ke 'extracted_compressed'.")
# Fungsi: Mengekstrak semua file dari file ZIP yang terkompresi.
# Kondisi: Ketika Anda ingin mengambil isi dari file ZIP terkompresi.
