import zipfile

with zipfile.ZipFile('unique_archive.zip', 'w') as zipf:
    file_seen = set()
    for file in ['file1.txt', 'file2.txt', 'file1.txt']:  # Duplikat file1.txt
        if file not in file_seen:
            zipf.write(file)
            file_seen.add(file)
print("File ZIP unik berhasil dibuat dengan tidak ada duplikat.")
# Fungsi: Memastikan tidak ada file ganda dalam arsip ZIP.
# Kondisi: Ketika Anda perlu mencegah pengulangan file dalam arsip.
