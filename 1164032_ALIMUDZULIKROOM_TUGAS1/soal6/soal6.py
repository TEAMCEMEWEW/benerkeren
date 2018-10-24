import shapefile #mengimpor modul shapefile
w=shapefile.Writer() #membuat shapefile baru
w.shapeType #setting menggunakan jenis shape apa (point/line/polygon)

#membuat tabel penyimpanan untuk koordinat x dan y berupa 2 buah kolom
w.field("kolom1","C")#w untuk write, field mendefinisikan kolom, "kolom1" mendefinisikan nama kolom dan c mendefinisikan tipe character
w.field("kolom2","C")#w untuk write, field mendefinisikan kolom, "kolom2" mendefinisikan nama kolom dan c mendefinisikan tipe character

#membuat 1 row record data untuk mengisi kolom pada database
w.record("ngek","satu") #w untuk write, record mendefinisikan perintah insert data ke kolom database

#mengisi 1  row data membuat sebuah polyline untuk mengisi.shp 
w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE)#w untuk write, polyline mendifinisikan membuat polyline dengan (x,y)
w.save("soal6") #menyimpan soal6