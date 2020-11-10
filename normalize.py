import csv
from modulenorm.modNormalize import normalize
from modulenorm.modTokenizing import tokenize
filename = 'Covid19-Sentiment.csv'
f = open(filename,'r', encoding='utf8')
reader = csv.reader(f)

for row in reader:
	text = row[0].encode("utf-8")
	text_decode = str(text.decode("utf-8"))

	usenorm = normalize()
	text_norm = usenorm.enterNormalize(text_decode) # normalisasi enter, 1 revw 1 baris
	# text_norm = usenorm.lowerNormalize(text_norm) # normalisasi huruf besar ke kecil
	text_norm = usenorm.repeatcharNormalize(text_norm) # normalisasi titik yang berulang
	text_norm = usenorm.linkNormalize(text_norm) # normalisasi link dalam text
	text_norm = usenorm.spacecharNormalize(text_norm) # normalisasi spasi karakter
	text_norm = usenorm.ellipsisNormalize(text_norm) # normalisasi elepsis (…)

	tok = tokenize() # panggil modul tokenisasi
	text_norm = tok.WordTokenize(text_norm) # pisah tiap kata pada kalimat

	text_norm = usenorm.spellNormalize(text_norm) # cek spell dari kata perkata
	text_norm = usenorm.wordcNormalize(text_norm,2) # menyambung kata (malam-malam) (param: textlist, jmlh_loop)
	# text_norm = usenorm.stemmingNormalize(text_norm,'word') # mengubah ke bentuk kata dasar (text, type_data)

	text_norm = ' '.join(text_norm) # menggabung kalimat tokenize dengan separate spasi

	text_norm = usenorm.emoticonNormalize(text_norm) # menggabung struktur emoticon yang terpisah ([: - )] = [:-)])

	# walking2
	# konfer @ ke at untuk penunjuk tempat

	output = open("output.txt","a")
	output.write(str(text_norm))
	output.write('\n')
	output.close()
	
	# print(no)
	no += 1
