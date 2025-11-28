import zipfile

with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.writestr('test.txt', 'Ini adalah beberapa konten yang disimpan di file ZIP.')
print("Konten berhasil disimpan dalam 'test.txt' di 'archive.zip'.")
# Fungsi: Menyimpan string langsung sebagai file di dalam arsip ZIP.
# Kondisi: Ketika Anda ingin menambahkan data programmatically tanpa file fisik.
