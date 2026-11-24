// Solar Duo — application de bureau (Electron)
// © Jacques Branas — licence GPL v3
const { app, BrowserWindow, Menu, shell, dialog, net } = require("electron");
const path = require("path");
const fs = require("fs");

const REPO = "Deltapassion/Solar-Duo";
const SITE = "https://deltapassion.github.io/Solar-Duo/";
const NOTICE = SITE + "notice/";

let win = null;
let pendingFile = null;
let pageReady = false;

// ---------- Textes du menu (fr / en / es, selon la langue du système)
const L = (() => {
  const l = (app.getLocale ? app.getLocale() : "fr").slice(0, 2);
  const T = {
    fr: { file: "Fichier", quit: "Quitter", edit: "Édition", view: "Affichage", help: "Aide",
          notice: "Notice", site: "Site de Solar Duo", upd: "Rechercher une mise à jour",
          upToDate: "Solar Duo est à jour (version {v}).", newer: "Une nouvelle version est disponible : {v}.",
          dl: "Télécharger", later: "Plus tard", ok: "OK", offline: "Impossible de joindre GitHub. Vérifiez la connexion Internet.",
          about: "À propos de Solar Duo", aboutTxt: "Solar Duo {v}\nDimensionnement d'installations photovoltaïques.\n© Jacques Branas — licence GPL v3" },
    en: { file: "File", quit: "Quit", edit: "Edit", view: "View", help: "Help",
          notice: "User guide", site: "Solar Duo website", upd: "Check for updates",
          upToDate: "Solar Duo is up to date (version {v}).", newer: "A new version is available: {v}.",
          dl: "Download", later: "Later", ok: "OK", offline: "Cannot reach GitHub. Check your Internet connection.",
          about: "About Solar Duo", aboutTxt: "Solar Duo {v}\nPhotovoltaic system sizing.\n© Jacques Branas — GPL v3 licence" },
    es: { file: "Archivo", quit: "Salir", edit: "Edición", view: "Ver", help: "Ayuda",
          notice: "Manual", site: "Sitio de Solar Duo", upd: "Buscar actualizaciones",
          upToDate: "Solar Duo está actualizado (versión {v}).", newer: "Hay una nueva versión disponible: {v}.",
          dl: "Descargar", later: "Más tarde", ok: "Aceptar", offline: "No se puede conectar con GitHub. Compruebe la conexión a Internet.",
          about: "Acerca de Solar Duo", aboutTxt: "Solar Duo {v}\nDimensionamiento de instalaciones fotovoltaicas.\n© Jacques Branas — licencia GPL v3" },
  };
  return T[l] || T.fr;
})();
const langParam = () => { const l = app.getLocale().slice(0, 2); return ["fr", "en", "es", "pt", "de", "it", "el", "zh", "ru", "uk", "ar", "sq"].includes(l) ? "?lang=" + l : ""; };

// ---------- Fichier .solarduo passé en argument (double-clic)
function fileFromArgs(argv) {
  return argv.slice(1).find(a => /\.(solarduo|json)$/i.test(a) && fs.existsSync(a)) || null;
}
function openProject(file) {
  if (!file) return;
  if (!win || !pageReady) { pendingFile = file; return; }
  try { win.webContents.send("open-project", fs.readFileSync(file, "utf8")); } catch (_) {}
}

// ---------- Recherche de mise à jour (GitHub, dernière version publiée)
const newer = (a, b) => {
  const pa = a.split(".").map(n => parseInt(n, 10) || 0), pb = b.split(".").map(n => parseInt(n, 10) || 0);
  for (let i = 0; i < 3; i++) { if ((pa[i] || 0) !== (pb[i] || 0)) return (pa[i] || 0) > (pb[i] || 0); }
  return false;
};
async function latestRelease() {
  const r = await net.fetch(`https://api.github.com/repos/${REPO}/releases/latest`, { headers: { "User-Agent": "Solar-Duo" } });
  if (!r.ok) throw new Error(r.status);
  const j = await r.json();
  return { version: String(j.tag_name || "").replace(/^v/i, ""), url: j.html_url || SITE };
}
async function checkUpdate(manual) {
  const cur = app.getVersion();
  try {
    const rel = await latestRelease();
    if (rel.version && newer(rel.version, cur)) {
      const info = { version: rel.version, url: SITE + "#telecharger" };
      if (manual) {
        const { response } = await dialog.showMessageBox(win, { type: "info", buttons: [L.dl, L.later], defaultId: 0, message: L.newer.replace("{v}", rel.version) });
        if (response === 0) shell.openExternal(info.url);
      } else if (win) win.webContents.send("update-available", info);
    } else if (manual) {
      dialog.showMessageBox(win, { type: "info", buttons: [L.ok], message: L.upToDate.replace("{v}", cur) });
    }
  } catch (_) {
    if (manual) dialog.showMessageBox(win, { type: "warning", buttons: [L.ok], message: L.offline });
  }
}

// ---------- Menu
function buildMenu() {
  const isMac = process.platform === "darwin";
  const tpl = [
    ...(isMac ? [{ role: "appMenu" }] : []),
    { label: L.file, submenu: [isMac ? { role: "close" } : { role: "quit", label: L.quit }] },
    { label: L.edit, role: "editMenu" },
    { label: L.view, submenu: [{ role: "reload" }, { type: "separator" }, { role: "resetZoom" }, { role: "zoomIn" }, { role: "zoomOut" }, { type: "separator" }, { role: "togglefullscreen" }] },
    { label: L.help, role: "help", submenu: [
      { label: L.notice, click: () => shell.openExternal(NOTICE + langParam()) },
      { label: L.site, click: () => shell.openExternal(SITE + langParam()) },
      { type: "separator" },
      { label: L.upd, click: () => checkUpdate(true) },
      ...(isMac ? [] : [{ label: L.about, click: () => dialog.showMessageBox(win, { type: "info", buttons: [L.ok], title: L.about, message: L.aboutTxt.replace("{v}", app.getVersion()) }) }]),
    ] },
  ];
  Menu.setApplicationMenu(Menu.buildFromTemplate(tpl));
}

// ---------- Fenêtre
function createWindow() {
  win = new BrowserWindow({
    width: 1280, height: 860, minWidth: 900, minHeight: 600,
    title: "Solar Duo",
    icon: path.join(__dirname, "build", "icon.png"),
    backgroundColor: "#0e2a47",
    webPreferences: { preload: path.join(__dirname, "preload.js"), contextIsolation: true, nodeIntegration: false, sandbox: true },
  });
  win.loadFile(path.join(__dirname, "src", "solar-duo.html"));

  // liens externes (fiches techniques, site) dans le navigateur
  win.webContents.setWindowOpenHandler(({ url }) => { if (/^https?:/i.test(url)) shell.openExternal(url); return { action: "deny" }; });
  win.webContents.on("will-navigate", (e, url) => { if (/^https?:/i.test(url)) { e.preventDefault(); shell.openExternal(url); } });

  win.webContents.on("did-start-loading", () => { pageReady = false; });
  win.webContents.on("did-finish-load", () => {
    pageReady = true;
    if (pendingFile) { const f = pendingFile; pendingFile = null; openProject(f); }
    setTimeout(() => checkUpdate(false), 3000);
  });
  win.on("closed", () => { win = null; });
}

// ---------- Démarrage
if (!app.requestSingleInstanceLock()) {
  app.quit();
} else {
  app.on("second-instance", (_e, argv) => {
    if (win) { if (win.isMinimized()) win.restore(); win.focus(); }
    openProject(fileFromArgs(argv));
  });
  app.on("open-file", (e, file) => { e.preventDefault(); openProject(file); }); // macOS
  pendingFile = fileFromArgs(process.argv);
  app.whenReady().then(() => {
    buildMenu();
    createWindow();
    app.on("activate", () => { if (!BrowserWindow.getAllWindows().length) createWindow(); });
  });
  app.on("window-all-closed", () => { if (process.platform !== "darwin") app.quit(); });
}
