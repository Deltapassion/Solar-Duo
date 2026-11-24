## Solar Duo 1.0.0 — première version

Dimensionnement d'installations photovoltaïques, en site isolé (avec batteries) ou raccordé au réseau, pour la classe comme pour un projet réel.

- **Bilan énergétique** : appareils types, coefficients Ku et Ks (tableaux NF C 15-100 / UTE C 15-105), veille, énergie journalière.
- **Panneaux** : DualSun (FLASH) et Jinko (Tiger Neo), choix des chaînes, limite de 120 V en site isolé (UTE C 15-712-2), correction par le froid.
- **Batteries** : plomb et lithium (LiFePO₄), autonomie, profondeur de décharge, groupement série / parallèle.
- **Régulateur et onduleur** : Victron (SmartSolar, Phoenix) et Studer (VarioTrack, Xtender), jusqu'à 5 kVA.
- **Câbles** : sections et chutes de tension.
- **Protections** : coupe-circuits porte-fusibles, sectionnement, disjoncteurs courant continu, parafoudres, différentiel 30 mA type A, Legrand / Schneider / ABB ; schéma unifilaire avec la mise à la terre de toutes les masses, panneaux compris ; option « − batterie à la terre » (Victron Wiring Unlimited).
- **Documentation technique** : tout le catalogue avec les liens vers les fiches des fabricants ; un clic pour choisir le matériel.
- **Exemples corrigés** : phare de la Caravelle, pavillon F4 à Tarbes, ombrière solaire.
- Enregistrement des projets (`.solarduo.json`), impression / PDF de la synthèse.
- Interface en français, anglais et espagnol ; recherche automatique des mises à jour.

### Installer

| Système | Fichier |
|---|---|
| Windows 10 / 11 | `Solar-Duo-Windows-Setup.exe` (installeur) ou `Solar-Duo-Windows.zip` (portable) |
| macOS Apple Silicon (M1, M2…) | `Solar-Duo-macOS-AppleSilicon.zip` |
| macOS Intel | `Solar-Duo-macOS-Intel.zip` |
| Linux | `Solar-Duo-x86_64.AppImage`, `solar-duo_amd64.deb` ou `Solar-Duo-Linux-x86_64.tar.gz` |

macOS : l'application n'est pas signée par un certificat Apple. Au premier lancement, faire un clic droit sur Solar Duo → **Ouvrir**, ou dans le Terminal : `xattr -cr "/Applications/Solar Duo.app"`.

Version en ligne, sans installation : https://deltapassion.github.io/Solar-Duo/app/
