import zipfile

with zipfile.ZipFile('compressed_archive.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('file1.txt')
print("File ZIP terkompresi telah dibuat.")
# Fungsi: Menggunakan kompresi untuk menghasilkan file ZIP.
# Kondisi: Ketika Anda ingin mengurangi ukuran file dengan kompresi.
