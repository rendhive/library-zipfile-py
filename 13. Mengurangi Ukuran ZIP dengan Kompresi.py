import zipfile

with zipfile.ZipFile('large_archive.zip', 'w', compression=zipfile.ZIP_BZIP2) as zipf:
    zipf.write('huge_file.txt')
print("Arsip besar berhasil dibuat dengan kompresi BZIP2.")
# Fungsi: Membuat file ZIP dengan metode kompresi alternatif.
# Kondisi: Saat Anda ingin mengompres file yang sangat besar secara efisien.
