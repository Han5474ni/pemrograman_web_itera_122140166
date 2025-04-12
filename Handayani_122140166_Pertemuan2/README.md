# Dasboard Mahasiswa

Dasboard produktivitas pribadi untuk Mahasiswa yang dibuat dengan JavaScript.

## Fitur-fitur

### Daftar Tugas
- Menambah, mengedit, dan menghapus tugas
- Menandai tugas sebagai selesai
- Menyaring tugas berdasarkan status (Semua, Aktif, Selesai)
- Tugas diurutkan berdasarkan tanggal pembuatan (yang terbaru lebih dulu)

### Jadwal Kelas
- Menambah kelas dengan nama, waktu, durasi, dan lokasi
- Melihat jadwal berdasarkan hari dalam seminggu
- Mengedit dan menghapus kelas
- Kelas diurutkan berdasarkan waktu

### Catatan Cepat
- Membuat catatan dengan judul dan konten
- Mengedit dan menghapus catatan
- Catatan diurutkan berdasarkan tanggal pembuatan (yang terbaru terlebih dahulu)

### Jam & Tanggal Waktu Nyata
- Menampilkan waktu dan tanggal saat ini
- Memperbarui secara waktu nyata

## Implementasi Teknis

## Fitur ES6+ yang Digunakan

1. **let & const**
 - Digunakan di seluruh kode untuk deklarasi variabel yang tepat
 - `const` untuk nilai yang tidak berubah
 - `let` untuk variabel yang membutuhkan penugasan ulang

2. **Fungsi Panah**
 - Digunakan untuk event handler dan callback
 - Contoh: `setInterval(() => { ... }, 1000)`
 - Contoh: `filterButtons.forEach(button => { ... })`

3. **Template Literals**
 - Digunakan untuk rendering HTML dinamis
 - Contoh: `` `<div class="note-title">${this.escapeHtml(note.title)}</div>` ``

4. **Async/Await**
 - Digunakan untuk simulasi pengambilan data
 - Contoh: `async fetchWeatherData() { ... }`
 - Contoh: `const weatherData = await app.fetchWeatherData()`

5. **Kelas**
 - Kelas `Dashboard` utama untuk mengatur kode dan mengelola status
 - Metode untuk menangani fitur yang berbeda

6. **Destructuring**
 - Digunakan untuk mengekstraksi nilai dari array
 - Contoh: `const [jam, menit] = time24h.split(':')`

7. **Spread Operator**
 - Digunakan untuk membuat salinan array
 - Contoh: `let filteredTodos = [...this.todos]`

8. **Parameter Default**
 - Digunakan dalam beberapa definisi fungsi

9. **localStorage API**
 - Digunakan untuk penyimpanan data yang persisten
 - JSON.stringify/parse untuk serialisasi data

## Penyimpanan Data

Semua data disimpan di localStorage browser:
- Item yang harus dilakukan
- Jadwal kelas
- Catatan

## Tangkapan layar

![image](https://github.com/user-attachments/assets/78d2c15e-ca10-41de-8a86-95eeec959a78)

![image](https://github.com/user-attachments/assets/7d5651a2-e3c3-4654-9312-6c63e5e373cc)

![image](https://github.com/user-attachments/assets/0ac8a772-505b-44a6-8d7c-6fbd835abfb0)

## Bagaimana Menjalankan

1. Unduh semua file (index.html). Unduh semua file (index.html, styles.css, app.js)
2. Buka index.html di browser modern apa pun
3. Tidak ada langkah pembuatan atau ketergantungan yang diperlukan

## Kompatibilitas browser

Dapat digunakan di semua browser modern yang mendukung fitur ES6+:
- Chrome
- Firefox
- Safari
- Edge
