import shapefile #mengimport modul shapefile
w=shapefile.Writer(shapeType=1) #sebagai penndeklarasian variabel dengan shapetipenya adalah 1
w.shapeType #menjalankan perintah pendeklarasian variabel 
w.shapeType=3 #berfungsi menjalankan code diatasnya = 3
w.shapeType #menjalankan perintah pendeklarasian variabel 
 
w.field("kolom1","C") #nama kolom
w.field("kolom2","C") #nama kolom
 
w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
w.record("ngok","dua") #isi dari kolom 2 ngok, dan kolom 1 dua
 
w.point(1,1) #titik koordinat 1,1
w.point(2,2) #titik koordinat 2,2
 
w.save("soal3") #menyimpan nama file soal 3