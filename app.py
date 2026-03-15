from flask import Flask, render_template, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Fungsi hitung_poin (sama seperti sebelumnya)
def hitung_poin(kill, placement):
    poin_placement = {
        1: 10, 2: 6, 3: 5, 4: 4, 5: 3
    }
    poin_kill = kill * 1
    placement_didapat = poin_placement.get(placement, 0) 
    return poin_kill + placement_didapat

# Routing utama web
@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        # Mengambil data dari form HTML
        nama_tim = request.form['nama_tim']
        jumlah_kill = int(request.form['kill'])
        ranking = int(request.form['placement'])
        
        # Proses hitung
        total = hitung_poin(jumlah_kill, ranking)
        hasil = f"Tim {nama_tim} mendapatkan total: {total} poin di match ini."
        
    # Menampilkan ke browser
    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    # host='0.0.0.0' penting untuk persiapan Docker nanti
    app.run(host='0.0.0.0', port=5000, debug=True)