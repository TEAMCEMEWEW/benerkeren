import shapefile  #mengimpor modul shapefile
w=shapefile.Writer(shapefile.POLYGON)   #membuat shapefile baru jenis polygon
w.shapeType #setting menggunakan jenis shape apa (point/line/polygon) #membuat tabel penyimpanan untuk koordinat x dan y berupa 2 buah kolom

w.field("kolom1","C") # membuat field x ,w untuk write, field mendefinisikan kolom, "kolom1" mendefinisikan nama kolom dan c mendefinisikan tipe character
w.field("kolom2","C") #membuat field y ,w untuk write, field mendefinisikan kolom, "kolom1" mendefinisikan nama kolom dan c mendefinisikan tipe character

w.record("Segitiga Sama kaki","satu") # input pertama , w untuk write, record mendefinisikan perintah insert data ke kolom database
w.record("Segitiga Sama kaki","dua") # input kedua , w untuk write, record mendefinisikan perintah insert data ke kolom database
w.record("Segitiga Sama kaki","tiga") # input ketiga , w untuk write, record mendefinisikan perintah insert data ke kolom database
w.record("Segitiga Sama kaki","empat") # input empat , w untuk write, record mendefinisikan perintah insert data ke kolom database
w.record("Segitiga Sama kaki","lima") # input lima , w untuk write, record mendefinisikan perintah insert data ke kolom database

#membuat 5 row
w.poly(parts=[[[-7,4],[-5,4], [-6,1],[-7,4]]],shapeType=shapefile.POLYGON) #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)
w.poly(parts=[[[-4,1],[-2,1], [-3,4],[-4,1]]],shapeType=shapefile.POLYGON) #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)
w.poly(parts=[[[-7,5],[-7,7], [-4,6],[-7,5]]],shapeType=shapefile.POLYGON) #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)
w.poly(parts=[[[1,-1],[3,-1], [2,-4],[1,-1]]],shapeType=shapefile.POLYGON) #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)
w.poly(parts=[[[4,-1],[5,-4], [3,-4],[4,-1]]],shapeType=shapefile.POLYGON) #w untuk write, polygon mendifinisikan membuat polyline dengan (x,y)

w.save("soal10") #menyimpan soal10