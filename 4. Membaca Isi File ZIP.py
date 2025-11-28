import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    print("File dalam ZIP:", zipf.namelist())
# Fungsi: Membaca nama-nama file dalam arsip ZIP.
# Kondisi: Ketika Anda ingin mengetahui isi file ZIP tanpa mengekstraknya.
