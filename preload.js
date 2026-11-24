// Passerelle entre Electron et la page : transmet le fichier ouvert et l'annonce de mise à jour
const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("solarDuoDesktop", {
  onOpen: cb => ipcRenderer.on("open-project", (_e, text) => cb(String(text))),
  onUpdate: cb => ipcRenderer.on("update-available", (_e, info) => cb({ version: String(info.version), url: String(info.url) })),
});
