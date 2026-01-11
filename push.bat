@echo off
chcp 65001 > nul
cd /d "%~dp0"
git remote set-url origin https://github.com/yoshikitsurumura/ToushinJuku.git
git add index.html SEARCH_ENGINES.md sitemap.xml robots.txt css/style.css
git commit -m "SEO対策追加: Google/Bing/Safari対応、Apple Touch Icon、構造化データ改善"
git push origin main
pause

