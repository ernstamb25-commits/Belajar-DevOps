# 1. Gunakan sistem operasi Linux + Python versi ringan sebagai dasar
FROM python:3.9-slim

# 2. Bikin folder khusus bernama /app di dalam server Docker-nya nanti
WORKDIR /app

# 3. Masukkan 'daftar belanja' kita ke dalam server
COPY requirements.txt .

# 4. Suruh servernya menginstal Flask sesuai daftar belanja
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy semua file kodemu (app.py, index.html, dll) ke dalam server
COPY . .

# 6. Buka port 5000 (Nah, anak TRI pasti paham konsep buka tutup port jaringan kan)
EXPOSE 5000

# 7. Tombol power untuk menyalakan aplikasinya
CMD ["python", "app.py"]