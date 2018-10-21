import shapefile #modul
w=shapefile.Writer() #deklarasi, dalam kurung bisa dikosongkan boleh diisi sesuai type
w.shapeType #berfungsi menjalankan code diatasnya

w.field("kolom1","C") #nama kolom
w.field("kolom2","C") #nama kolom

w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
 
 
w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE) 
w.save("soal6") #nama file