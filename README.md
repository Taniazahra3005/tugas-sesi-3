# Tower of Hanoi (3 Piringan)

Program Python untuk memindahkan 3 piringan dari tiang A ke tiang C
dengan bantuan tiang B.

## Aturan
1. Hanya 1 piringan yang boleh dipindah setiap langkah.
2. Hanya piringan paling atas yang boleh dipindah.
3. Piringan besar tidak boleh di atas piringan kecil.

## Penjelasan Kode
- `tiang`: menyimpan kondisi tiang A, B, C.
- `tampilkan_tiang()`: mencetak isi tiap tiang.
- `pindahkan_piringan()`: memindahkan 1 piringan dan mencetak langkahnya.
- `hanoi()`: fungsi rekursif untuk menyelesaikan permainan:
  1. Pindahkan n-1 piringan dari A ke B.
  2. Pindahkan piringan terbesar dari A ke C.
  3. Pindahkan n-1 piringan dari B ke C.

## Hasil
Selesai dalam 7 langkah (2^3 - 1).
