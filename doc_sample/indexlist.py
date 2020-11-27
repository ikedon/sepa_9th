import bs4
import csv # モジュール"CSV"の呼び出し

chapterlist = ["ch01.md","ch02.md","ch05.md"]
csvlist = [] # 配列を作成

for chfile in chapterlist:
	# スクレイピング対象のhtmlファイルからsoupを作成
	soup = bs4.BeautifulSoup(open(chfile, encoding="utf-8"), 'html.parser')

	links = soup.find_all('span') # 全てのspanタグ要素を取得

	for link in links: # spanタグのテキストデータを配列に格納
	    sample_txt = link.text
	    csvlist.append(sample_txt)

# 重複を削除、いちおうソート込み（後で見直すかも）
flat = []
flat = sorted(list(set(csvlist)))

# CSVファイルを開く。ファイルがない場合は新規作成
f = open("indexlist.csv", "w")
# writecsv = csv.writer(f, lineterminator='\n')

for data in flat:
#	print(data)
	f.write(data+'\n')
#    writecsv.writerow(data)

f.close() # CSVファイルを閉じる
