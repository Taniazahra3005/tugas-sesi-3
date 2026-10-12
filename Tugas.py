"""
=====================================================
 TOWER OF HANOI (MENARA HANOI) - 3 PIRINGAN
 Bahasa : Python 3
 Tujuan : Memindahkan semua piringan dari tiang A (Start)
          ke tiang C (Finish) dengan bantuan tiang B.
=====================================================

ATURAN PERMAINAN:
1. Hanya boleh memindahkan 1 piringan setiap langkah.
2. Hanya piringan paling atas dari sebuah tiang yang boleh dipindah.
3. Piringan besar TIDAK boleh diletakkan di atas piringan yang lebih kecil.
"""

# -----------------------------------------------------
# [BAGIAN 1] VARIABEL GLOBAL
# -----------------------------------------------------
# Counter untuk menghitung nomor langkah yang sudah dilakukan.
langkah = 0

# Kondisi awal tiang. Angka = ukuran piringan (1 = kecil, 3 = besar).
# Daftar paling kiri = dasar tiang, paling kanan = paling atas.
# Start : A berisi [3, 2, 1], B dan C kosong.
tiang = {
    "A": [3, 2, 1],
    "B": [],
    "C": [],
}


# -----------------------------------------------------
# [BAGIAN 2] FUNGSI TAMPILKAN KONDISI TIANG
# -----------------------------------------------------
def tampilkan_tiang():
    """Mencetak isi tiang A, B, C saat ini agar progres mudah dilihat."""
    for nama, isi in tiang.items():
        print(f"   Tiang {nama}: {isi}")
    print()


# -----------------------------------------------------
# [BAGIAN 3] FUNGSI MEMINDAHKAN 1 PIRINGAN
# -----------------------------------------------------
def pindahkan_piringan(asal, tujuan):
    """Memindahkan 1 piringan teratas dari tiang 'asal' ke tiang 'tujuan'."""
    global langkah
    langkah += 1

    # Ambil piringan paling atas dari tiang asal
    piringan = tiang[asal].pop()
    # Letakkan di tiang tujuan
    tiang[tujuan].append(piringan)

    # Cetak langkah yang dilakukan
    print(f"Langkah {langkah}: Pindahkan piringan {piringan} dari {asal} -> {tujuan}")
    # Cetak kondisi tiang setelah dipindah
    tampilkan_tiang()


# -----------------------------------------------------
# [BAGIAN 4] FUNGSI UTAMA (REKURSIF)
# -----------------------------------------------------
def hanoi(n, asal, bantu, tujuan):
    """
    Menyelesaikan Tower of Hanoi secara rekursif.

    n      : jumlah piringan yang akan dipindah
    asal   : tiang tempat piringan berada sekarang
    bantu  : tiang perantara (penampung sementara)
    tujuan : tiang tujuan akhir
    """
    # BASE CASE: jika tidak ada piringan, berhenti.
    if n == 0:
        return

    # Langkah 1: Pindahkan (n-1) piringan di atas dari 'asal' ke 'bantu'
    #            (menggunakan 'tujuan' sebagai perantara)
    hanoi(n - 1, asal, tujuan, bantu)

    # Langkah 2: Pindahkan piringan terbesar (ke-n) dari 'asal' ke 'tujuan'
    pindahkan_piringan(asal, tujuan)

    # Langkah 3: Pindahkan (n-1) piringan dari 'bantu' ke 'tujuan'
    #            (menggunakan 'asal' sebagai perantara)
    hanoi(n - 1, bantu, asal, tujuan)


# -----------------------------------------------------
# [BAGIAN 5] PROGRAM UTAMA
# -----------------------------------------------------
if __name__ == "__main__":
    jumlah_piringan = 3

    print("=== TOWER OF HANOI ===")
    print("KONDISI AWAL (Start):")
    tampilkan_tiang()

    # Jalankan penyelesaian: A (asal) -> C (tujuan), B (bantu)
    hanoi(jumlah_piringan, "A", "B", "C")

    print("KONDISI AKHIR (Finish):")
    tampilkan_tiang()
    print(f"Selesai! Total langkah: {langkah} (rumus minimum: 2^n - 1 = {2**jumlah_piringan - 1})")