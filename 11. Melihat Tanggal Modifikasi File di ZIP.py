import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    for info in zipf.infolist():
        print(f"File: {info.filename}, Diperbarui pada: {info.date_time}")
# Fungsi: Mencetak tanggal modifikasi untuk semua file dalam file ZIP.
# Kondisi: Ketika Anda perlu mengetahui kapan file diarsipkan.
