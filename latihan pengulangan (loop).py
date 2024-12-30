kontak1 = {'nama' :'andi', 'no.HP': "0853--------", 'email' :'andisun@gmail.com' }
kontak2 = {'nama' :'susanti', 'no.HP': "0861--------", 'email' :'susantisun@gmail.com' }
kontak3 = {'nama' :'budi', 'no.HP': "0899--------", 'email' :'budisun@gmail.com' }
kontak4 = {'nama' :'asep', 'no.HP': "0801--------", 'email' :'asepsun@gmail.com' }
kontak5 = {'nama' :'aisyah', 'no.HP': "0833--------", 'email' :'aisyahsun@gmail.com' }
kontak = [kontak1,kontak2,kontak3,kontak4,kontak5]



def informasi_kontak(kontak) :
    if kontak : 
        for index, items in enumerate(kontak) : 
             print(f"\n{index+1}. {items['nama']} {items['no.HP']} , {items['email']}")
    else : 
        print('kontak anda kosong')

def menambahkan_kontak () : 
    nama = input('masukkan nama kontak baru : ')
    HP = input('masukkan nomor hp baru : ' ) 
    email = input('masukkan email baru : ' ) 
    kontak_baru = {'nama' : nama , 'no.HP' : HP , 'email' : email} 
    kontak.append(kontak_baru)
    print(f'kontak baru berhasil ditambahkan dengan nama {kontak_baru["nama"]}, no.HP {kontak_baru["no.HP"]}, email {kontak_baru["email"]} ')

def menghapus_kontak() :
    print('\ndaftar kontak')
    for index, items in enumerate(kontak) : 
        print(f"{index+1}. {items['nama baru']}, {items['no.HP baru']}, {items['email baru']}" ) 
    hapus_kontak = int(input('\nMasukkan nomor urutan kontak yang ingin dihapus: '))
    del kontak[hapus_kontak-1]
    print(f'kontak nomor {hapus_kontak} berhasil dihapus !')
    
 
print('\nPROGRAM MANAJEMEN KONTAK') 
print('------------------------')

while True :
    print('\nhalo, selamat datang di program manajemen \nkontak')
    print('\nmenu kontak : ')
    print('\n1. informasi kontak')
    print('2. menambahkan kontak baru')
    print('3. menghapus kontak')
    print('4. keluar dari kontak')

    pilihan =input('masukkan pilihan menu kontak (1,2,3 atau 4) : ')
    if pilihan == '1' : 
        informasi_kontak(kontak)

    elif pilihan == '2' : 
        menambahkan_kontak()
        
    elif pilihan == '3' : 
        menghapus_kontak()

         
    elif pilihan == '4' : 
        break
    else : 
        print ('maaf pilihan anda tidak ada di menu kontak ')
    
