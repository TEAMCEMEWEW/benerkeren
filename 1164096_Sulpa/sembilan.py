import shapefile #mengimport modul
w=shapefile.Writer() #pendeklarasian
w.shapeType #untuk menjalankan modul
 
w.field("kolom1","C") #buat kolom 1
w.field("kolom2","C") #buat kolom 2
 
w.record("ngek","satu") #isi kolom 1
w.record("crot","dua") #isi kolom 2
 
  
w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], 
[1,3]]],shapeType=shapefile.POLYLINE) #titik koordinat
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], 
[1,6]]],shapeType=shapefile.POLYLINE) #titik koordinat
  
w.save("soal9") #menyimpan soal9