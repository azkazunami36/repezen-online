import os
import json

# カレントディレクトリ内のpngまたはjpgファイルを取得
png_files = [f for f in os.listdir('.') if f.endswith('.png') or f.endswith('.jpg')]

# データを辞書形式で保存
data = {"files": png_files}

# JSONファイルに書き込む
with open('files.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)
