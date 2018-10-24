import shapefile  #mengimpor modul shapefile
w=shapefile.Writer(shapefile.POLYGON)   #membuat shapefile baru jenis polygon
w.shapeType #setting menggunakan jenis shape apa (point/line/polygon)

#membuat tabel penyimpanan untuk koordinat x dan y berupa 2 buah kolom
w.field("kolom1","C") # membuat field x ,w untuk write, field mendefinisikan kolom, "kolom1" mendefinisikan nama kolom dan c mendefinisikan tipe character
w.field("kolom2","C") #membuat field y ,w untuk write, field mendefinisikan kolom, "kolom1" mendefinisikan nama kolom dan c mendefinisikan tipe character

w.record("aku","satu")  # input pertama , w untuk write, record mendefinisikan perintah insert data ke kolom database
w.record("mereka","dua")  #input kedua, w untuk write, record mendefinisikan perintah insert data ke kolom database
w.record("kalian","tiga")  # input ketiga, w untuk write, record mendefinisikan perintah insert data ke kolom database


#mengisi 3  row data membuat sebuah polyline untuk mengisi.shp
w.poly(parts=[[[7,9],[5,1],[9,1],
[7,9]]],shapeType=shapefile.POLYGON)    #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)

w.poly(parts=[[[3,6],[1,0],[5,0],
[3,6]]],shapeType=shapefile.POLYGON)   #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)

w.poly(parts=[[[14,8],[12,1],[16,1],
[14,8]]],shapeType=shapefile.POLYGON)   #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)


w.save("soal10") # menyimpan soal10
