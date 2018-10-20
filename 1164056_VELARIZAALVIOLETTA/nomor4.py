import shapefile #modul
w=shapefile.Writer(shapefile.POINTM) #deklarasi, dalam kurung bisa dikosongkan boleh diisi sesuai type disini menggunakan shapefile.POINTM
w.shapeType #berfungsi menjalankan code diatasnya

w.field("kolom1","C") #nama kolom
w.field("kolom2","C")  #nama kolom

w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
w.record("ngok","dua") #isi dari kolom 2 ngok, dan kolom 1 dua

w.point(1,1) #titik koordinat
w.point(2,2) #titik koordinat
w.save("soal4") #nama file 