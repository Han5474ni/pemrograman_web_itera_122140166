# Modul Matematika - math_operations.py

# Konstanta PI
PI = 3.14159

# Fungsi untuk menghitung luas dan keliling persegi
def luas_persegi(sisi):
    """
    Menghitung luas persegi
    
    Args:
        sisi (float): Panjang sisi persegi
        
    Returns:
        float: Luas persegi
    """
    return sisi * sisi

def keliling_persegi(sisi):
    """
    Menghitung keliling persegi
    
    Args:
        sisi (float): Panjang sisi persegi
        
    Returns:
        float: Keliling persegi
    """
    return 4 * sisi

# Fungsi untuk menghitung luas dan keliling persegi panjang
def luas_persegi_panjang(panjang, lebar):
    """
    Menghitung luas persegi panjang
    
    Args:
        panjang (float): Panjang persegi panjang
        lebar (float): Lebar persegi panjang
        
    Returns:
        float: Luas persegi panjang
    """
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    """
    Menghitung keliling persegi panjang
    
    Args:
        panjang (float): Panjang persegi panjang
        lebar (float): Lebar persegi panjang
        
    Returns:
        float: Keliling persegi panjang
    """
    return 2 * (panjang + lebar)

# Fungsi untuk menghitung luas dan keliling lingkaran
def luas_lingkaran(jari_jari):
    """
    Menghitung luas lingkaran
    
    Args:
        jari_jari (float): Jari-jari lingkaran
        
    Returns:
        float: Luas lingkaran
    """
    return PI * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    """
    Menghitung keliling lingkaran
    
    Args:
        jari_jari (float): Jari-jari lingkaran
        
    Returns:
        float: Keliling lingkaran
    """
    return 2 * PI * jari_jari

# Fungsi konversi suhu
def celsius_ke_fahrenheit(celsius):
    """
    Mengkonversi suhu dari Celsius ke Fahrenheit
    
    Args:
        celsius (float): Suhu dalam Celsius
        
    Returns:
        float: Suhu dalam Fahrenheit
    """
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius):
    """
    Mengkonversi suhu dari Celsius ke Kelvin
    
    Args:
        celsius (float): Suhu dalam Celsius
        
    Returns:
        float: Suhu dalam Kelvin
    """
    return celsius + 273.15