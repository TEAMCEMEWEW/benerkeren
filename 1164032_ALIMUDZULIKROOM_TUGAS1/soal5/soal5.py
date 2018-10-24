import shapefile #mengimpor modul shapefile
w=shapefile.Writer() #membuat shapefile baru
w.shapeType #setting menggunakan jenis shape apa (point/line/polygon)

#membuat tabel penyimpanan untuk koordinat x dan y berupa 2 buah kolom
w.field("kolom1","C") #w untuk write, field mendefinisikan kolom, "kolom1" mendefinisikan nama kolom dan c mendefinisikan tipe character
w.field("kolom2","C") #w untuk write, field mendefinisikan kolom, "kolom2" mendefinisikan nama kolom dan c mendefinisikan tipe character


#membuat 1 row record data untuk mengisi kolom pada database
w.record("ngek","satu") #w untuk write, record mendefinisikan perintah insert data ke kolom database

#mengisi 1  row data membuat sebuah garis untuk mengisi.shp 
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #w untuk write, line mendifinisikan membuat line dengan (x,y)

w.save("soal5") #menyimpan soal5