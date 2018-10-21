import shapefile 
w=shapefile.Writer(shapefile.POINTM) #deklarasi, dalam kurung bisa dikosongkan boleh diisi sesuai type disini menggunakan shapefile.POINTM
w.shapeType #berfungsi menjalankan code diatasnya
 
w.field("kolom1","C") #membuat kolom1 dengan tipe data karakter
w.field("kolom2","C") #membuat kolom2 dengan tipe data karakter
 
w.record("ngek","satu") #isi dari kolom 1
w.record("ngok","dua") #isi dari kolom 2
 
w.point(1,1) #titik koordinat 1,1
w.point(2,2) #titik koordinat 2,2
 
w.save("soal4") #menyimpan soal 4
