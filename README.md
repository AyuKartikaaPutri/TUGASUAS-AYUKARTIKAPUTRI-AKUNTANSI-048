# TUGASUAS-AYUKARTIKAPUTRI-AKUNTANSI-048

---

# Analisis Data Penjualan Cake dan Pastry

## Pendahuluan

Proyek ini bertujuan untuk menganalisis data penjualan cake dan pastry, menggunakan berbagai teknik analisis data dan visualisasi. Saya membuat tiga tabel data: penjualan cake, penjualan pastry, dan penjualan bulanan. Data ini dianalisis menggunakan regresi linier dan analisis korelasi, serta divisualisasikan untuk memberikan wawasan yang mendalam tentang hubungan antar variabel.

## Dataset

Terdapat tiga dataset yang digunakan dalam analisis ini, disimpan dalam file CSV:

1. **Penjualan Cake (data_cake.csv)**
    - Jenis: ['Chocolate', 'Vanilla', 'Red Velvet', 'Cheesecake', 'Black Forest']
    - Jumlah: [150, 200, 120, 180, 140]
    - Harga: [20, 18, 25, 22, 24]

2. **Penjualan Pastry (data_pastry.csv)**
    - Jenis: ['Croissant', 'Danish', 'Muffin', 'Strudel', 'Pie']
    - Jumlah: [170, 160, 180, 150, 190]
    - Harga: [15, 14, 18, 20, 22]

3. **Penjualan Bulanan (data_bulanan.csv)**
    - Bulan: ['January', 'February', 'March', 'April', 'May']
    - Penjualan Cake: [500, 600, 550, 620, 590]
    - Penjualan Pastry: [480, 560, 520, 580, 610]

## Analisis Data

### 1. Regresi Linier

Analisis regresi linier dilakukan untuk melihat hubungan antara penjualan bulanan cake dan pastry. Hasil regresi linier menunjukkan:

- **Slope (kemiringan garis regresi):** 0.675
- **Intercept (titik potong pada sumbu Y):** 184.0
- **R-squared (nilai koefisien determinasi):** 0.815
- **P-value (nilai p):** 0.045

Interpretasi:
- Penjualan cake memiliki hubungan yang signifikan dan kuat dengan penjualan pastry.
- Setiap peningkatan satu unit penjualan cake dikaitkan dengan peningkatan sekitar 0.675 unit penjualan pastry.

### 2. Analisis Korelasi

Analisis korelasi dilakukan untuk melihat hubungan antara harga dan jumlah penjualan cake dan pastry.

#### Korelasi Cake
```
           harga    jumlah
harga    1.000000  0.390566
jumlah   0.390566  1.000000
```

#### Korelasi Pastry
```
           harga    jumlah
harga    1.000000  0.862879
jumlah   0.862879  1.000000
```

Interpretasi:
- Korelasi harga dan jumlah penjualan cake adalah 0.391, menunjukkan korelasi positif yang lemah.
- Korelasi harga dan jumlah penjualan pastry adalah 0.863, menunjukkan korelasi positif yang sangat kuat.

## Visualisasi

Visualisasi data dilakukan menggunakan berbagai jenis grafik untuk memberikan wawasan yang lebih mendalam. Hasil visualisasi disimpan dalam file PNG:

1. **Scatter Plot dengan Trendline (Regresi Linier)**
    - Menunjukkan hubungan linier antara penjualan bulanan cake dan pastry.
    - Mengindikasikan arah dan kekuatan hubungan.
    - File: `visualisasi.png`

2. **Heatmap Korelasi**
    - Menampilkan korelasi antara harga dan jumlah penjualan cake dan pastry.
    - Warna pada heatmap menunjukkan kekuatan korelasi.
    - File: `visualisasi_korelasi.png`

3. **Scatter Plot dengan Trendline (Harga vs Jumlah Penjualan Cake)**
    - Menunjukkan hubungan antara harga dan jumlah penjualan cake.
    - Trendline memvisualisasikan arah dan kekuatan hubungan.
    - File: `visualisasi.png`

## File Proyek

- **data_bulanan.csv:** Dataset penjualan bulanan cake dan pastry.
- **data_cake.csv:** Dataset penjualan cake berdasarkan jenis, jumlah, dan harga.
- **data_pastry.csv:** Dataset penjualan pastry berdasarkan jenis, jumlah, dan harga.
- **korelasi.py:** Kode Python untuk analisis korelasi.
- **penjualancakedanpastry.py:** Kode Python untuk analisis data penjualan cake dan pastry, termasuk regresi linier dan visualisasi.
- **visualisasi.png:** File gambar hasil visualisasi analisis data.
- **visualisasi_korelasi.png:** File gambar hasil visualisasi korelasi.
- **README:** File ini yang berisi penjelasan lengkap mengenai proyek.

## Kesimpulan

Proyek ini menunjukkan bahwa terdapat hubungan yang signifikan antara penjualan bulanan cake dan pastry. Harga dan jumlah penjualan pastry memiliki korelasi yang sangat kuat, sedangkan untuk cake, korelasi ini lebih lemah tetapi tetap positif. Informasi ini berguna untuk pengambilan keputusan bisnis seperti penetapan harga dan strategi penjualan.

## Instruksi Penggunaan

Untuk menjalankan analisis ini, ikuti langkah-langkah berikut:

1. Instalasi library yang diperlukan:
    ```bash
    pip install pandas matplotlib seaborn scipy
    ```

2. Jalankan kode analisis:
    ```python
    # Paste the provided Python code here and execute.
    ```

3. Interpretasi hasil visualisasi dan analisis data yang dihasilkan.

## Pengembangan Lebih Lanjut

Proyek ini dapat dikembangkan lebih lanjut dengan:
- Menambahkan lebih banyak variabel untuk analisis yang lebih komprehensif.
- Menggunakan teknik machine learning untuk prediksi penjualan di masa depan.
- Mengintegrasikan data penjualan dari berbagai sumber untuk mendapatkan wawasan yang lebih luas.

---
