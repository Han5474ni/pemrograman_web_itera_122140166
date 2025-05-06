# Library Management System

## Overview
Ini adalah sistem manajemen perpustakaan sederhana yang diimplementasikan dalam Python menggunakan konsep Pemrograman Berorientasi Objek (OOP). Sistem ini memungkinkan pengelolaan berbagai jenis item perpustakaan seperti buku dan majalah, dengan fitur untuk menambahkan, mencari, meminjam, dan mengembalikan item.

## Features
- Kelas dasar abstrak untuk item perpustakaan
- Dukungan untuk berbagai jenis item perpustakaan (Buku dan Majalah)
- Menambahkan dan menghapus item dari perpustakaan
- Mencari item berdasarkan ID atau judul
- Meminjam dan mengembalikan item
- Menampilkan item yang tersedia dan semua item di perpustakaan

## Project Structure
Proyek ini terdiri dari kelas-kelas berikut:

1. **LibraryItem (Abstract Base Class)**
   - Kelas dasar untuk semua item perpustakaan
   - Berisi atribut umum seperti ID, judul, penulis, dll.
   - Mendefinisikan metode abstrak `display_info()` yang harus diimplementasikan oleh subclass

2. **Book (Subclass of LibraryItem)**
   - Merepresentasikan buku dengan atribut khusus seperti ISBN dan genre
   - Mengimplementasikan metode `display_info()` untuk menampilkan detail buku

3. **Magazine (Subclass of LibraryItem)**
   - Merepresentasikan majalah dengan atribut khusus seperti nomor edisi dan kategori
   - Mengimplementasikan metode `display_info()` untuk menampilkan detail majalah

4. **Library**
   - Mengelola koleksi item perpustakaan
   - Menyediakan metode untuk menambahkan, menghapus, mencari, dan menampilkan item

## OOP Concepts Implemented
- **Inheritance**: Kelas Book dan Magazine mewarisi dari LibraryItem
- **Abstraction**: LibraryItem adalah kelas abstrak dengan metode abstrak
- **Encapsulation**: Atribut private dan protected dengan property decorator
- **Polymorphism**: Implementasi berbeda dari metode `display_info()` di subclass

## How to Use

### Creating a Library
```python
# Membuat perpustakaan
library = Library("My Library")
```

### Adding Items
```python
# Membuat buku
book = Book("B001", "Python Programming", "John Smith", 2020, "978-1234567890", "Programming")

# Membuat majalah
magazine = Magazine("M001", "Tech Today", "Tech Publications", 2022, "Issue 45", "Technology")

# Menambahkan item ke perpustakaan
library.add_item(book)
library.add_item(magazine)
```

### Searching for Items
```python
# Mencari berdasarkan ID
item = library.search_by_id("B001")

# Mencari berdasarkan judul
items = library.search_by_title("Python")
```

### Checking Out and Returning Items
```python
# Meminjam item
book.checkout()
print(book.display_info())  # Status akan menunjukkan "Checked Out"

# Mengembalikan item
book.return_item()
print(book.display_info())  # Status akan menunjukkan "Available"
```

### Displaying Items
```python
# Menampilkan semua item
all_items = library.display_all_items()
for item in all_items:
    print(item.display_info())
    print("-" * 40)

# Menampilkan item yang tersedia
available_items = library.display_available_items()
for item in available_items:
    print(item.display_info())
    print("-" * 40)
```

## Example Output
Berikut adalah contoh output dari program:

```
Book ID: B001
Title: Python Programming
Author: John Smith
Publication Year: 2020
ISBN: 978-1234567890
Genre: Programming
Status: Available
----------------------------------------

Magazine ID: M001
Title: Tech Today
Author: Tech Publications
Publication Year: 2022
Issue Number: Issue 45
Category: Technology
Status: Available
----------------------------------------
```