# BFS-DFS

Nama : Fadhel Rahmawan
NPM : 1184064

1. DFS Depth First Search (DFS) adalah algoritma yang melakukan pencarian secara melebar yang mengunjungi simpul secara preorder yaitu mengunjungi suatu simpul kemudian mengunjungi semua simpul yang bertetangga dengan simpul tersebut terlebih dahulu. Selanjutnya, simpul yang belum dikunjungi dan bertetangga dengan simpulsimpul yang tadi dikunjungi , demikian seterusnya. Jika graf berbentuk pohon berakar, maka semua simpul pada aras d dikunjungi lebih dahulu sebelum simpul-simpul pad aras d+1.

Cara Kerja Algoritma Depth First Search (DFS) Proses pencarian pada algoritma DFS akan dilakukan pada semua anaknya terlebih dahulu, Dalam algoritma BFS, simpul anak yang telah dikunjungi disimpan dalam suatu antrian. Antrian ini digunakan untuk mengacu simpul-simpul yang bertetangga dengannya yang akan dikunjungi kemudian sesuai urutan pengantrian.
Untuk memperjelas cara kerja algoritma BFS beserta antrian yang digunakannya, berikut langkah-langkah algoritma BFS:

- Masukkan simpul ujung (akar) ke dalam antrian.
- Ambil simpul dari awal antrian, lalu cek apakah simpul merupakan solusi.
- Jika simpul merupakan solusi, pencarian selesai dan hasil dikembalikan..
- Jika simpul bukan solusi, masukkan seluruh simpul yang bertetangga dengan simpul tersebut (simpul anak) ke dalam antrian.
- Jika antrian kosong dan setiap simpul sudah dicek, pencarian selesai dan mengembalikan hasil solusi tidak ditemukan.
- Ulangi pencarian dari langkah kedua.

2. BFS (Breadth First Search) adalah salah satu algoritma yang digunakan untuk pencarian jalur. Contoh yang dibahas kali ini adalah mengenai pencarian jalur yang melalui semua titik.
Algoritma ini adalah salah satu algoritma pencarian jalur sederhana, dimana pencarian dimulai dari titik awal, kemudian dilanjutkan ke semua cabang titik tersebut secara terurut. Jika titik tujuan belum ditemukan, maka perhitungan akan diulang lagi ke masing-masing titik cabang dari masing-masing titik, sampai titik tujuan tersebut ditemukan.

3. kesimpulan
    Persamaan BFS dan DFS sama sama melakukan pencarian, sedangkan perbedaannya BFS dapat melakukan pencarian melalui lebih dari satu jalur yang bertetangga dari node. Sedangkan DFS, hanya bisa melalukan pencarian menggunakan satu jalur ke bagian terdalam dari sebuah grafik.
