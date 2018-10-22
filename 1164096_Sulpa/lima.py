import shapefile #untuk mengimport modul yang bernama shapefile
w=shapefile.Writer() #deklarasi, dalam kurung bisa dikosongkan boleh diisi sesuai type
w.shapeType #berfungsi menjalankan code diatasnya
 
w.field("kolom1","C") #nama kolom1 dengan tipe data character
w.field("kolom2","C") #nama kolom2 dengan tipe data character
 
w.record("ngek","satu") #isi dari kolom 1 ngek, dan kolom 2 satu
w.record()
 
 
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) 
w.save("soal5") #nama file