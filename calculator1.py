cek = "R"
while cek != "Q" :
    masukkan_nilai = input("==>")
    pisah = masukkan_nilai.split()
    if pisah[0] == "Q" :
        break
    elif pisah[1] == "+":
        hasil = int(pisah[0]) + int(pisah[2])
        print(hasil)
        cek = "R"
    elif pisah[1] == "-":
        hasil = int(pisah[0]) - int(pisah[2])
        print(hasil)
        cek = "R"
    elif pisah[1] == "*":
        hasil = int(pisah[0]) * int(pisah[2])
        print(hasil)
        cek = "R"
    elif pisah[1] == "/":
        hasil = int(pisah[0]) / int(pisah[2])
        print(hasil)
        cek = "R"