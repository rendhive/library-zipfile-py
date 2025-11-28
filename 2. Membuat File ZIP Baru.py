import zipfile

with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('file1.txt')
print("File ZIP 'archive.zip' berhasil dibuat.")
# Fungsi: Membuat archive ZIP baru dan menambahkan file ke dalamnya.
# Kondisi: Ketika Anda ingin mengarsipkan beberapa file ke dalam format ZIP.
