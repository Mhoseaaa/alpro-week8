def tampilkan_soal(nama_file):
    with open(nama_file, 'r') as f:
        soal_jawaban = f.readlines()

    for line in soal_jawaban:
        soal,jawaban = line.strip().split('||')
        print(soal)
        jawaban_user = input("Jawab: ")
        if jawaban_user.strip().lower() == jawaban.strip().lower():
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")

# Ganti dengan nama file teks Anda
nama_file = "baik.txt"
tampilkan_soal(nama_file)