import zipfile
from io import BytesIO

# Mengambil data zip dari memory
zip_buffer = BytesIO()
with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.writestr('in_memory_file.txt', 'Konten dari file yang ada di memory.')

# Membaca kembali data dari buffer
zip_buffer.seek(0)  # Reset ke awal buffer
with zipfile.ZipFile(zip_buffer, 'r') as zipf:
    zipped_content = zipf.read('in_memory_file.txt')
    print("Konten dari file:", zipped_content.decode())
# Fungsi: Membuat dan membaca file ZIP langsung dari memory.
# Kondisi: Ketika Anda ingin bekerja dengan file ZIP tanpa menyimpannya ke disk.
