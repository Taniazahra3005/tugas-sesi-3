# Tower of Hanoi 3 Piringan (Python)

Di tugas ini aku bikin program Python buat nyelesain permainan Tower of Hanoi.
Tujuannya mindahin 3 piringan dari tiang A ke tiang C, dan tiang B dipakai
sebagai tempat singgah sementara.

## Aturan mainnya
1. Sekali jalan cuma boleh mindahin 1 piringan.
2. Yang boleh dipindah cuma piringan paling atas di tiap tiang.
3. Piringan besar nggak boleh ditaruh di atas piringan yang lebih kecil.

## Penjelasan kodenya

**1. Variabel global**
Ada variabel `langkah` yang dipakai buat ngitung udah berapa kali piringan dipindah.
Terus ada `tiang`, isinya tiga list buat tiang A, B, dan C. Angka di dalam list itu
ukuran piringannya (1 paling kecil, 3 paling besar). Di awal, tiang A isinya
`[3, 2, 1]` dan tiang B sama C masih kosong.

**2. Fungsi `tampilkan_tiang()`**
Fungsi ini tugasnya cuma nge-print isi tiang A, B, dan C. Aku pakai ini biar tiap
habis pindah piringan, kelihatan posisi piringannya sekarang ada di mana.

**3. Fungsi `pindahkan_piringan(asal, tujuan)`**
Ini fungsi buat mindahin satu piringan. Cara kerjanya, piringan paling atas diambil
dari tiang asal pakai `pop()`, terus ditaruh di tiang tujuan pakai `append()`.
Nomor langkah juga ditambah, lalu hasilnya di-print.

**4. Fungsi `hanoi(n, asal, bantu, tujuan)`**
Ini bagian utamanya, pakai rekursi (fungsi yang manggil dirinya sendiri).
Kalau `n` sudah 0 berarti nggak ada piringan lagi, jadi fungsinya berhenti.
Kalau belum, urutannya begini:
- pindahin `n-1` piringan di atas dari tiang asal ke tiang bantu,
- pindahin piringan paling besar dari tiang asal ke tiang tujuan,
- pindahin lagi `n-1` piringan tadi dari tiang bantu ke tiang tujuan.

**5. Program utama**
Di sini jumlah piringan diset 3. Program nampilin kondisi awal, lalu manggil
`hanoi(3, "A", "B", "C")`, dan terakhir nampilin kondisi akhir sama total langkahnya.

## Cara jalaninnya
```
python tower_of_hanoi.py
```

## Hasilnya
```
Langkah 1: Pindahkan piringan 1 dari A -> C
Langkah 2: Pindahkan piringan 2 dari A -> B
Langkah 3: Pindahkan piringan 1 dari C -> B
Langkah 4: Pindahkan piringan 3 dari A -> C
Langkah 5: Pindahkan piringan 1 dari B -> A
Langkah 6: Pindahkan piringan 2 dari B -> C
Langkah 7: Pindahkan piringan 1 dari A -> C
```

Total ada 7 langkah. Ini sama dengan rumus minimal langkah Tower of Hanoi,
yaitu 2^n - 1, jadi 2^3 - 1 = 7.
