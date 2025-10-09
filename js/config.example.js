// AIチャットボット設定ファイル（例）
// このファイルをコピーして config.js として保存し、実際の値を設定してください
// ⚠️ config.js は .gitignore に含まれているため、Gitにコミットされません

const CHAT_CONFIG = {
  // Google Apps Script のデプロイURL
  // デプロイ手順: SECURE_SETUP_GUIDE.md を参照
  WEB_APP_URL: 'YOUR_GAS_DEPLOY_URL_HERE'
};

// グローバルに公開（index.htmlから参照できるようにする）
window.CHAT_CONFIG = CHAT_CONFIG;
