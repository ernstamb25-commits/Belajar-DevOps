def hitung_poin(kill, placement):
    # Simulasi distribusi poin placement (Top 5)
    # Bisa diubah sesuai format turnamen yang sedang berjalan
    poin_placement = {
        1: 10,  # WWCD / Posisi 1
        2: 6,
        3: 5,
        4: 4,
        5: 3
    }
    
    # Aturan standar: 1 kill = 1 poin
    poin_kill = kill * 1
    
    # Ambil poin placement, jika di luar Top 5 otomatis dapat 0 (atau bisa diatur nanti)
    placement_didapat = poin_placement.get(placement, 0) 
    
    total_poin = poin_kill + placement_didapat
    return total_poin

print("--- Kalkulator Poin Turnamen E-Sports ---")
nama_tim = input("Masukkan nama tim: ")
jumlah_kill = int(input("Jumlah Kill: "))
ranking = int(input("Placement (Ranking 1-16): "))

total = hitung_poin(jumlah_kill, ranking)
print(f"--> Tim {nama_tim} mendapatkan total: {total} poin di match ini.")