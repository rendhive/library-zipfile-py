import zipfile

file_names = ['file1.txt', 'file2.txt']

with zipfile.ZipFile('multi_file_archive.zip', 'w') as zipf:
    for file in file_names:
        zipf.write(file)
print("Beberapa file berhasil disimpan dalam 'multi_file_archive.zip'.")
# Fungsi: Menyimpan beberapa file ke dalam satu arsip ZIP.
# Kondisi: Ketika Anda perlu mengarsipkan lebih dari satu file sekaligus.
