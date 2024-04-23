def is_anagram(word1, word2):
    # Mengubah kata menjadi lowercase dan menghapus spasi
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    # Mengurutkan huruf-huruf dalam kata
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    # Membandingkan kata yang sudah diurutkan
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False

# Contoh penggunaan
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if is_anagram(kata1, kata2):
    print("Kedua kata adalah anagram.")
else:
    print("Kedua kata bukan anagram.")