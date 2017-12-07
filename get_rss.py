import feedparser

# RSS情報の解析
feed_url = 'https://liginc.co.jp/feed'
feed_result = feedparser.parse(feed_url)

# 記事タイトルを取得し表示する
for entry in feed_result.entries:
    print(entry.title)
