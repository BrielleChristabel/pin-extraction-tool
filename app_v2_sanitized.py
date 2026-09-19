'''Module Name: Secure PIN Extraction Tool (Version 2)
   Description: Membaca teks input, melakukan validasi & sanitasi data, serta mengenerate 4-Digit PIN menggunakan enkripsi SHA-256.
   Autor: [Brielle Alexis Christabel]'''

import hashlib

def process_text_to_pin(raw_text: str) -> str:
    '''Mengambil teks mentah, melakukan sanitasi, dan mengahsilkan PIn 4 digit menggunakan SHA-256.'''
    # --- TAHAP 1: VAlIDASI & SANITASI DATA ---
    if not isinstance(raw_text, str):
        raise TypeError("Input harus berupa string.")
    raw_text = raw_text.strip() # Menghapus spasi di awal dan akhir
    if not raw_text:
        raise ValueError("Input tidak boleh kosong setelah sanitasi.")
    # --- TAHAP 2: PEMROSESAN TEKS ---
    teks_list = raw_text.splitlines()
    pin = ''
    for teks in teks_list:
        # --- TAHAP 3: ENKRIPSI SHA-256 ---
        hash_hex = hashlib.sha256(teks.encode()).hexdigest()
        pin += str(int(hash_hex, 16))[:4] # Mengambil 4 digit pertama dari hasil enkripsi SHA-256
    return pin
# --- TAHAP 4: PENGUJIAN KODE ---
if __name__ == "__main__":
    # Contoh penggunaa fungsi process_text_to_pin
    try:
        with open('document.txt', 'r') as file:
            isi_teks = file.read()
            pin_hasil = process_text_to_pin(isi_teks)
            print("PIN:", pin_hasil)
    except FileNotFoundError:
        print("Error: File 'document.txt' tidak ditemukan.")
    except (ValueError, TypeError) as e:
        print(f"Error Validasi: {e}")