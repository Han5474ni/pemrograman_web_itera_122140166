# Program Pengelolaan Data Nilai Mahasiswa

def hitung_nilai_akhir(nilai_uts, nilai_uas, nilai_tugas):
    """
    Menghitung nilai akhir berdasarkan bobot:
    30% UTS + 40% UAS + 30% Tugas
    
    Args:
        nilai_uts (float): Nilai UTS
        nilai_uas (float): Nilai UAS
        nilai_tugas (float): Nilai Tugas
        
    Returns:
        float: Nilai akhir
    """
    return (0.3 * nilai_uts) + (0.4 * nilai_uas) + (0.3 * nilai_tugas)

def tentukan_grade(nilai_akhir):
    """
    Menentukan grade berdasarkan nilai akhir
    
    Args:
        nilai_akhir (float): Nilai akhir mahasiswa
        
    Returns:
        str: Grade (A, B, C, D, atau E)
    """
    if nilai_akhir >= 80:
        return "A"
    elif 70 <= nilai_akhir < 80:
        return "B"
    elif 60 <= nilai_akhir < 70:
        return "C"
    elif 50 <= nilai_akhir < 60:
        return "D"
    else:  # nilai_akhir < 50
        return "E"

def main():
    # Data mahasiswa (list yang berisi dictionary)
    data_mahasiswa = [
        {"nama": "Budi Santoso", "nim": "122140001", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
        {"nama": "Ani Wijaya", "nim": "122140002", "nilai_uts": 75, "nilai_uas": 80, "nilai_tugas": 78},
        {"nama": "Dedi Kurniawan", "nim": "122140003", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 68},
        {"nama": "Rina Putri", "nim": "122140004", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
        {"nama": "Eko Prasetyo", "nim": "122140005", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 48}
    ]
    
    # Hitung nilai akhir dan tentukan grade untuk setiap mahasiswa
    for mahasiswa in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(mahasiswa["nilai_uts"], mahasiswa["nilai_uas"], mahasiswa["nilai_tugas"])
        mahasiswa["nilai_akhir"] = nilai_akhir
        mahasiswa["grade"] = tentukan_grade(nilai_akhir)
    
    # Tampilkan data dalam bentuk tabel
    print("\n" + "=" * 80)
    print("                         DATA NILAI MAHASISWA")
    print("=" * 80)
    print("{:<5} {:<20} {:<12} {:<8} {:<8} {:<8} {:<12} {:<5}".format(
        "No", "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Grade"))
    print("-" * 80)
    
    for i, mahasiswa in enumerate(data_mahasiswa, 1):
        print("{:<5} {:<20} {:<12} {:<8} {:<8} {:<8} {:<12.2f} {:<5}".format(
            i,
            mahasiswa["nama"],
            mahasiswa["nim"],
            mahasiswa["nilai_uts"],
            mahasiswa["nilai_uas"],
            mahasiswa["nilai_tugas"],
            mahasiswa["nilai_akhir"],
            mahasiswa["grade"]
        ))
    
    print("-" * 80)
    
    # Cari mahasiswa dengan nilai tertinggi dan terendah
    nilai_tertinggi = max(data_mahasiswa, key=lambda x: x["nilai_akhir"])
    nilai_terendah = min(data_mahasiswa, key=lambda x: x["nilai_akhir"])
    
    # Tampilkan mahasiswa dengan nilai tertinggi dan terendah
    print("\nMahasiswa dengan nilai tertinggi:")
    print(f"Nama: {nilai_tertinggi['nama']}")
    print(f"NIM: {nilai_tertinggi['nim']}")
    print(f"Nilai Akhir: {nilai_tertinggi['nilai_akhir']:.2f}")
    print(f"Grade: {nilai_tertinggi['grade']}")
    
    print("\nMahasiswa dengan nilai terendah:")
    print(f"Nama: {nilai_terendah['nama']}")
    print(f"NIM: {nilai_terendah['nim']}")
    print(f"Nilai Akhir: {nilai_terendah['nilai_akhir']:.2f}")
    print(f"Grade: {nilai_terendah['grade']}")

if __name__ == "__main__":
    main()