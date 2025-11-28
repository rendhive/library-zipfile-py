import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    file_list = zipf.namelist()
    print("Daftar file dalam ZIP:", file_list)
# Fungsi: Mengambil nama semua file dalam arsip ZIP.
# Kondisi: Ketika Anda perlu mengumpulkan semua nama file dari ZIP tanpa mengeluarkannya.
