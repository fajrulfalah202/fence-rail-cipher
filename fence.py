import os
def enkripsi(pesan, kunci):
    # untuk enkripsi
    rell = [['\n' for i in range(len(pesan))]
                for j in range(kunci)]
    
    # temukan arah
    dir_down = False
    baris, kolom = 0, 0

    for i in range(len(pesan)):
        if (baris == 0 ) or (baris == kunci-1):
            dir_down= not dir_down

        rell[baris][kolom]= pesan[i]
        kolom +=1

        if dir_down:
            baris +=1
        else:
            baris-=1

    hasil =[]
    for i in range(kunci):
        for j in range(len(pesan)):
            if rell[i][j] != "\n":
                hasil.append(rell[i][j])
    return ("".join(hasil))

            
def dekripsi(pesan, kunci):
    # untuk enkripsi
    rell = [['\n' for i in range(len(pesan))]
                for j in range(kunci)]
    
    dir_down = None
    baris, kolomm = 0,0

    for i in range(len (pesan)):
        if baris ==0:
            dir_down = True
        if baris == kunci-1:
            dir_down = False

        rell[baris][kolomm]= "*"
        kolomm+=1

        if dir_down:
            baris+=1
        else:
            baris-=1

    index = 0
    for i in range(kunci):
        for j in range(len(pesan)):
            if ((rell[i][j] == "*") and (index < len (pesan))):
                rell[i][j] = pesan[index]
                index +=1

    # baca matrix
    hasil = []
    baris, kolomm = 0,0
    for i in range(len(pesan)):
        if baris == 0:
            dir_down =True
        if baris == kunci-1:
            dir_down =False
        
        if (rell[baris][kolomm]!= '*') :
            hasil.append(rell[baris][kolomm])
            kolomm+=1

        if dir_down:
            baris+=1
        else:
            baris-=1

    return("".join(hasil))



if __name__ == "__main__":
   keluar = False
   while keluar == False:
            
        os.system("cls")
        pesan= input("isi pesan: ")
        kunci= int(input("isi kunci parameter: "))
        
        os.system("cls")
        print("pilih mau apa")
        print("1. enkripsi")
        print("2. dekripsi")
        print("3. keluar")
        perintah = int(input ("pakai nomer "))

        if perintah == 1:
            print(enkripsi(pesan, kunci))
            input("press enter to continue ... ")
        if perintah == 2:
            print(dekripsi(pesan, kunci))
            input("press enter to continue ... ")
        if perintah == 3:
            print("selamat jalan")
            keluar = True
#    kunci= input("isi kuci parameter")