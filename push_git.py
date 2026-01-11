# -*- coding: utf-8 -*-
import os
import subprocess
import sys

# UTF-8エンコーディング設定
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

# このスクリプトがあるディレクトリに移動
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print(f"Current directory: {os.getcwd()}")

# git remote設定
subprocess.run(["git", "remote", "set-url", "origin", "https://github.com/yoshikitsurumura/ToushinJuku.git"], check=True)
print("Remote URL set")

# ファイルをステージング
files = ["index.html", "SEARCH_ENGINES.md", "sitemap.xml", "robots.txt", "css/style.css"]
for file in files:
    if os.path.exists(file):
        subprocess.run(["git", "add", file], check=True)
        print(f"Added: {file}")

# ステータス確認
result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, encoding='utf-8')
print("\nGit status:")
print(result.stdout)

# コミット
commit_message = "SEO対策追加: Google/Bing/Safari対応、Apple Touch Icon、構造化データ改善"
subprocess.run(["git", "commit", "-m", commit_message], check=True)
print("Committed")

# Push
subprocess.run(["git", "push", "origin", "main"], check=True)
print("Pushed to origin/main")

print("\nAll done!")

