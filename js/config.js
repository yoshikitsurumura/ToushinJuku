// AIチャットボット設定ファイル（例）
// このファイルをコピーして config.js として保存し、実際の値を設定してください
// ⚠️ config.js は .gitignore に含まれているため、Gitにコミットされません

const CHAT_CONFIG = {
  // Google Apps Script のデプロイURL
  WEB_APP_URL: 'https://script.google.com/macros/s/AKfycbyaVrL46sjQBXGfJNgaf_OIouqX0JKIobD-D1nCVtOp6unF3vanLWC531FnBJ2Swf3y/exec'
};

// グローバルに公開（index.htmlから参照できるようにする）
window.CHAT_CONFIG = CHAT_CONFIG;
