import feedparser
import MeCab

# RSS情報の解析
feed_url = 'https://liginc.co.jp/feed'
feed_result = feedparser.parse(feed_url)

# 記事タイトルを取得し配列に格納する
entry_array = []
for entry in feed_result.entries:
    entry_array.append(entry.title)

# 記事タイトルの形態素解析を行う
m = MeCab.Tagger()
result = m.parse(entry_array[0])
print(result)
