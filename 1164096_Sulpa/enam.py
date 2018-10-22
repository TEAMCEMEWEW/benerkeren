import shapefile #mengimport modul dengan nama shapefile
w=shapefile.Writer() #pendeklarasian 
w.shapeType #berfungsi untuk menjalankan code diatas

w.field("kolom1","C") #nama kolom 1 dengan tipe karakter
w.field("kolom2","C") #nama kolom 2 dengan tipe karakter

w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
 
 
w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE) 
w.save("soal6") #menyimpan nama file