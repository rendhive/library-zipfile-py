import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    file_info = zipf.getinfo('file1.txt')
    print("Informasi file:", file_info)
# Fungsi: Mendapatkan informasi seperti ukuran file, tanggal, dll.
# Kondisi: Ketika Anda ingin mendapatkan detail spesifik tentang file dalam ZIP.
