import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    total_size = sum(info.file_size for info in zipf.infolist())
print("Total ukuran file dalam ZIP:", total_size, "bytes")
# Fungsi: Menghitung total ukuran semua file dalam arsip ZIP.
# Kondisi: Ketika Anda perlu mengetahui seberapa besar arsip ZIP.
