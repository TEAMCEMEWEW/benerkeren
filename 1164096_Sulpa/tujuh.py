import shapefile #untuk mengimport modul yang bernama shapefile
w=shapefile.Writer() #pendeklarasian
w.shapeType #berfungsi untuk menjalankan code yang telah dibuat

w.field("kolom1","C") #nama kolom1 dengan tipe data character
w.field("kolom2","C") #nama kolom2 dengan tipe data character

w.record("ngek","satu") ##isi dari kolom 1 ngek, dan kolom 2 satu
 
 
w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE) 

w.save("soal7") #nama file