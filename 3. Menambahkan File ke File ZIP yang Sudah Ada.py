import zipfile

with zipfile.ZipFile('archive.zip', 'a') as zipf:  # 'a' untuk append
    zipf.write('file2.txt')
print("file2.txt berhasil ditambahkan ke 'archive.zip'.")
# Fungsi: Menambahkan file baru ke file ZIP yang sudah ada.
# Kondisi: Ketika Anda perlu memperbarui arsip ZIP dengan file tambahan.
