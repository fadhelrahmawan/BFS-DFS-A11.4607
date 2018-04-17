#Ai
#judul Denah kampus undip dengan bfs
#Rika-Nanik

petaUndip =  {
         'A':set(['F','V','C']), #vcf
         'B':set(['C']),
         'C':set(['A','D','B']),
         'D':set(['C']),
         'E':set(['V','G']),
         'F':set(['A','G']),
         'G':set(['F','H','E','L']),
         'H':set(['G','I']),
         'I':set(['H','J','S']),
         'J':set(['I','R','K']),
         'K':set(['J','Q']),
         'L':set(['M','G']),
         'M':set(['O','N','L']),
         'N':set(['Q','M']),
         'O':set(['M']),
         'P':set(['Q']),
         'Q':set(['K','P','U','N']),
         'R':set(['J']),
         'S':set(['I']),
         'T':set(['U']),
         'U':set(['Q','T']),
         'V':set(['A','E'])}

petaUndipDeskripsi = {
    'A':set(["Fakultas Hukum"]),
    'B':set(["Gedung Serba Guna"]),
    'C':set(["Gedung BTB"]),
    'D':set(["Masjid Undip"]),
    'E':set(["Fakultas Ilmu Budaya"]),
    'F':set(["Fakultas Ilmu Sosial Dan Politik"]),
    'G':set(["Fakultas Tehnik Arsitektur"]),
    'H':set(["Fakultas Tehnik Sipil"]),
    'I':set(["Fakultas Tehnik Kimia"]),
    'J':set(["Fakultas Tehnik Indurstri"]),
    'K':set(["Fakultas Tehnik Mesin"]),
    'L':set(["Fakultas Tehnik Geodesi"]),
    'M':set(["Fakultas Tehnik Elektro"]),
    'N':set(["FSM"]),
    'O':set(["Fakultas Ekonomi Dan Bisnis"]),
    'P':set(["Fakultas Psikologi"]),
    'Q':set(["Fakultas Kesehatan Masyarakat"]),
    'R':set(["Fakultas Perikanan Dan Kelautan"]),
    'S':set(["FPP"]),
    'T':set(["Fakultas Kedokteran"]),
    'U':set(["Departemen Ilmu Keperawatan"]),
    'V':set(["Sekolah Vokasi])"])
    } 


def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
           minimum = 0
           maksimum = len(jalur)
           while (minimum < maksimum):
                print(petaUndipDeskripsi[jalur[minimum]])
                minimum = minimum + 1
           print("==================BFS======================")
           print ("Jalur diatas adalah jalur untuk menuju ke ")
           print(petaUndipDeskripsi[tujuan])
           print(" dari ")
           print(petaUndipDeskripsi[mulai])
           return jalur

        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                if cabang not in visited: 
                    jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru
                print (jalur_baru)
            #tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
           print("Tidak ditemukan")


#print(bfs(petaUndip,'I','O'))
awal = 'V'
tujuan = 'T'
print("==================BFS======================")
bfs(petaUndip,awal,tujuan)
            