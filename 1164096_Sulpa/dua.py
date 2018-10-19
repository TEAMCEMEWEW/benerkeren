import shapefile #menginport modul yang bernama shapefile
w=shapefile.Writer(shapeType=1) #sebagai penndeklarasian variabel dengan shapefilenya adalah 1
w.shapeType #menjalankan perintah pendeklarasian variabel diatas
 
w.field("kolom1","C") #membuat field/kolom1 dengan type data character
w.field("kolom2","C") #membuat field/kolom2 dengan type data character
 
w.record("ngek","satu") #mengisi kolom1 yang telah dibuat diatas
w.record("ngok","dua") #mengisi kolom2 yang telah dibuat diatas
 
w.point(1,1) #membuat titik 1,1
w.point(2,2) #membuat titik 1,2
 
w.save("soal2") #untuk menyimpan soal2