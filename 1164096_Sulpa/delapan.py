import shapefile #untuk mengimport modul yang bernama shapefile
w=shapefile.Writer() #pendeklarasian
w.shapeType #untuk menjalankan modul
w.field("kolom1","C") #membuat kolom1
w.field("kolom2","C") #membuat kolom 2
w.record("ngek","satu") #mengisi kolom

w.poly(parts=[[[1,3],[5,3],[1,2],[5,2], [1,3]]],shapeType=shapefile.POLYLINE) 
w.save("soal8") #menyimpan soal8