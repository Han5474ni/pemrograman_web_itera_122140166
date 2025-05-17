#!/bin/bash

# Script untuk menguji API Matakuliah dengan curl

# URL dasar API
BASE_URL="http://localhost:6543"

# Warna untuk output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Testing API Matakuliah ===${NC}"
echo

# 1. Login untuk mendapatkan token
echo -e "${BLUE}1. Login untuk mendapatkan token${NC}"
TOKEN=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}' \
  ${BASE_URL}/api/auth/login | grep -o '"token":"[^"]*' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
  echo -e "${RED}Login gagal. Tidak bisa mendapatkan token.${NC}"
  exit 1
else
  echo -e "${GREEN}Login berhasil. Token: ${TOKEN:0:20}...${NC}"
fi

echo

# 2. Membuat matakuliah baru (POST)
echo -e "${BLUE}2. Membuat matakuliah baru (POST /api/matakuliah)${NC}"
CREATE_RESPONSE=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "kode_mk": "IF001",
    "nama_mk": "Pemrograman Web",
    "sks": 3,
    "semester": 5
  }' \
  ${BASE_URL}/api/matakuliah)

echo -e "${GREEN}Response:${NC}"
echo $CREATE_RESPONSE | python3 -m json.tool

# Ambil ID matakuliah yang baru dibuat
MK_ID=$(echo $CREATE_RESPONSE | grep -o '"id":[0-9]*' | cut -d':' -f2)
echo -e "${GREEN}ID Matakuliah: $MK_ID${NC}"

echo

# 3. Mendapatkan daftar matakuliah (GET dengan paginasi)
echo -e "${BLUE}3. Mendapatkan daftar matakuliah (GET /api/matakuliah)${NC}"
curl -s -X GET \
  -H "Authorization: Bearer $TOKEN" \
  ${BASE_URL}/api/matakuliah?page=1&items_per_page=10 | python3 -m json.tool

echo

# 4. Mendapatkan detail matakuliah (GET by ID)
echo -e "${BLUE}4. Mendapatkan detail matakuliah (GET /api/matakuliah/$MK_ID)${NC}"
curl -s -X GET \
  -H "Authorization: Bearer $TOKEN" \
  ${BASE_URL}/api/matakuliah/$MK_ID | python3 -m json.tool

echo

# 5. Mengupdate matakuliah (PUT)
echo -e "${BLUE}5. Mengupdate matakuliah (PUT /api/matakuliah/$MK_ID)${NC}"
curl -s -X PUT \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "nama_mk": "Pemrograman Web Lanjut",
    "sks": 4
  }' \
  ${BASE_URL}/api/matakuliah/$MK_ID | python3 -m json.tool

echo

# 6. Mendapatkan detail matakuliah setelah update (GET by ID)
echo -e "${BLUE}6. Mendapatkan detail matakuliah setelah update (GET /api/matakuliah/$MK_ID)${NC}"
curl -s -X GET \
  -H "Authorization: Bearer $TOKEN" \
  ${BASE_URL}/api/matakuliah/$MK_ID | python3 -m json.tool

echo

# 7. Menghapus matakuliah (DELETE)
echo -e "${BLUE}7. Menghapus matakuliah (DELETE /api/matakuliah/$MK_ID)${NC}"
DELETE_STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE \
  -H "Authorization: Bearer $TOKEN" \
  ${BASE_URL}/api/matakuliah/$MK_ID)

if [ "$DELETE_STATUS" -eq 204 ]; then
  echo -e "${GREEN}Matakuliah berhasil dihapus. Status: $DELETE_STATUS${NC}"
else
  echo -e "${RED}Gagal menghapus matakuliah. Status: $DELETE_STATUS${NC}"
fi

echo

# 8. Mencoba mendapatkan matakuliah yang sudah dihapus (GET by ID)
echo -e "${BLUE}8. Mencoba mendapatkan matakuliah yang sudah dihapus (GET /api/matakuliah/$MK_ID)${NC}"
curl -s -X GET \
  -H "Authorization: Bearer $TOKEN" \
  ${BASE_URL}/api/matakuliah/$MK_ID | python3 -m json.tool

echo

# 9. Mencoba akses tanpa token
echo -e "${BLUE}9. Mencoba akses tanpa token (GET /api/matakuliah)${NC}"
curl -s -X GET \
  ${BASE_URL}/api/matakuliah | python3 -m json.tool

echo

# 10. Mencoba membuat matakuliah dengan data tidak valid
echo -e "${BLUE}10. Mencoba membuat matakuliah dengan data tidak valid (POST /api/matakuliah)${NC}"
curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "kode_mk": "IF",
    "nama_mk": "",
    "sks": 0,
    "semester": 20
  }' \
  ${BASE_URL}/api/matakuliah | python3 -m json.tool

echo -e "${GREEN}Testing selesai.${NC}"
