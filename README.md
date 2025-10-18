# 燈心塾 ランディングページ

秋田発のオンライン専門塾「燈心塾」の公式ランディングページです。

## 🎯 概要

AI×個別指導で効率よく伸ばすオンライン専門塾のLPです。講師歴10年のプロによる最適化された学習計画と伴走指導で、目標達成までしっかりサポートします。

## ✨ 主な機能

- **レスポンシブデザイン**: モバイル・タブレット・デスクトップに完全対応
- **AIチャットボット**: あきたいぬAI「灯（あかり）ちゃん」が質問に対応（準備中）
- **スムーズなアニメーション**: AOS.jsを使用した洗練されたスクロールアニメーション
- **SEO最適化**: メタタグ・構造化データ完備

## 🚀 技術スタック

- **HTML5**: セマンティックマークアップ
- **CSS3**: カスタムプロパティ、Flexbox、Grid
- **JavaScript**: バニラJS
- **Bootstrap 5.3.3**: レスポンシブグリッドとコンポーネント
- **AOS.js**: スクロールアニメーション
- **Particles.js**: 背景エフェクト

## 📁 ファイル構造

```
1_landing_page/
├── index.html              # メインHTMLファイル
├── css/
│   └── style.css          # カスタムスタイル
├── js/
│   ├── script.js          # メインJavaScript
│   ├── config.js          # チャットボット設定
│   └── config.example.js  # 設定ファイルのサンプル
├── images/                # 画像ファイル
│   ├── icon.png          # ロゴ
│   ├── ai_assistant_icon.png  # AIアシスタントアイコン
│   ├── hero_image.jpg    # ヒーローセクション画像
│   ├── female_teacher_icon.png  # 女性講師アイコン
│   ├── tsurumura.png     # 代表講師写真
│   └── line_qr.png       # LINE QRコード
├── particles-config.json  # Particles.js設定
├── robots.txt            # クローラー設定
├── sitemap.xml           # サイトマップ
└── README.md             # このファイル
```

## 🔧 セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/yoshikitsurumura/ToushinJuku_LP.git
cd ToushinJuku_LP
```

### 2. チャットボット設定（オプション）

AIチャットボット機能を有効化する場合：

```bash
cp js/config.example.js js/config.js
```

`js/config.js`を編集してAPIエンドポイントを設定します。

### 3. ローカルサーバーで起動

任意のローカルサーバーで起動してください：

```bash
# Python 3の場合
python -m http.server 8000

# Node.jsのhttp-serverの場合
npx http-server
```

ブラウザで `http://localhost:8000` にアクセス。

## 🎨 カスタマイズ

### カラースキーム

`css/style.css`のCSS変数を編集：

```css
:root {
    --primary-color: #38B6FF;  /* Light Blue */
    --accent-color: #FF7A00;   /* Orange */
    --text-color: #333;
    --bg-color: #FFFFFF;
}
```

### 画像の変更

`images/`フォルダ内の画像を差し替えて、`index.html`内のパスを更新してください。

## 📱 対応ブラウザ

- Chrome（最新版）
- Firefox（最新版）
- Safari（最新版）
- Edge（最新版）

## 🌐 デプロイ

### GitHub Pagesでデプロイ

1. GitHubリポジトリの Settings → Pages
2. Source を `main` ブランチに設定
3. 公開URLが生成されます

### その他のホスティング

- Netlify
- Vercel
- AWS S3 + CloudFront

## 📝 ライセンス

このプロジェクトは燈心塾の所有物です。

## 👤 制作者

- **燈心塾** - [公式サイト](https://yoshikitsurumura.github.io/ToushinJuku_LP/)

## 📞 お問い合わせ

質問や提案がある場合は、LINEまたはメールでお問い合わせください。

---

© 2025 燈心塾. All rights reserved.
