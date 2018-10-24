import shapefile #mengimpor modul shapefile
w=shapefile.Writer(shapeType=1) #membuat shapefile baru
w.shapeType #setting menggunakan jenis shape apa (point/line/polygon)

#membuat tabel penyimpanan untuk koordinat x dan y berupa 2 buah kolom

w.field("kolom1","C") #w untuk write, field mendefinisikan kolom, "kolom1" mendefinisikan nama kolom dan c mendefinisikan tipe character
w.field("kolom2","C") #w untuk write, field mendefinisikan kolom, "kolom2" mendefinisikan nama kolom dan c mendefinisikan tipe character

#membuat 2 row record data untuk mengisi kolom pada database
w.record("ngek","satu") #w untuk write, record mendefinisikan perintah insert data ke kolom database
w.record("ngok","dua") #w untuk write, record mendefinisikan perintah insert data ke kolom database

#mengisi 2 # row data membuat sebuah titik untuk mengisi.shp 
w.point(1,1) # w untuk write, point mendifinisikan membuat jenis point, x=1, y=1
w.point(2,2) # w untuk write, point mendifinisikan membuat jenis point, x=2, y=2
w.save("soal2") # menyimpan soal2

