import shapefile #mengimpor modul shapefil
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)
#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bidang","Bidang Ke")
w.field("Nama Bidang","Bidang Ke")
#membuat dbs dengan 2 field, berupa kolom
w.record("Segitiga Sama kaki","satu")
w.record("Segitiga Sama kaki","dua")
w.record("Segitiga Sama kaki","tiga")
w.record("Segitiga Sama kaki","empat")
w.record("Segitiga Sama kaki","lima")
w.record("Segitiga Sama kaki","enam")
w.record("Segitiga Sama kaki","tujuh")
w.record("Segitiga Sama kaki","delapan")
w.record("Segitiga Sama kaki","sembilan")


#membuat 9 row karena menggunakan 
w.poly(parts=[[[-7,4],[-5,4], [-6,1],[-7,4]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-4,1],[-2,1], [-3,4],[-4,1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-7,5],[-7,7], [-4,6],[-7,5]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[1,-1],[3,-1], [2,-4],[1,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[4,-1],[5,-4], [3,-4],[4,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[1,-6],[4,-5], [4,-7],[1,-6]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[1,-8],[4,-9], [1,-10],[1,-8]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-7,-1],[-3,-2], [-7,-3],[-7,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-4,-3],[-2,-3], [-3,-6],[-4,-3]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.save("soal10")#melakukan save dengan nama (soal1)