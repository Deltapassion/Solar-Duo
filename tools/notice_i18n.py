"""Textes de la notice (docs/notice/index.html) en 12 langues → docs/notice/notice-text.js
    python tools/notice_i18n.py
"""
import json
from pathlib import Path

# Image de chaque section (préfixe de langue ajouté par la page : fr, en, es ; en pour les autres langues)
IMG = [None, None, "01-site", "02-loads", "03-pv", "04-bat", "05-conv", "06-cab", "07-prot", "07b-schema", "08-doc", "09-sum", "10-reseau", None]

F_WIN = "<code>Solar-Duo-Windows-Setup.exe</code>"
F_ZIP = "<code>Solar-Duo-Windows.zip</code>"
F_MAC = "<code>Solar-Duo-macOS-AppleSilicon.zip</code> / <code>Solar-Duo-macOS-Intel.zip</code>"
F_DEB = "<code>solar-duo_amd64.deb</code>"
F_APP = "<code>Solar-Duo-x86_64.AppImage</code>"
XATTR = '<code>xattr -cr "/Applications/Solar Duo.app"</code>'
URL = '<a href="../app/">deltapassion.github.io/Solar-Duo/app</a>'
PC = "P<sub>c</sub> = E<sub>ch</sub> / (N<sub>e</sub> × η<sub>ph</sub>)"
CB = "C = E<sub>ch</sub> × J / (U × D)"
SC = "S = ρ × 2L × I / (ΔU × U)"
REFS = "NF C 15-100 ; UTE C 15-712-2 ; UTE C 15-105 ; Schneider Electric, <i>Guide de l'installation électrique</i> ; Victron Energy, <i>Wiring Unlimited</i>"

N = {}

N["fr"] = dict(title="Notice d'utilisation", sub="Dimensionnement d'installations photovoltaïques — version 1.0", toc="Sommaire",
 site="Site de Solar Duo", app="Version en ligne", dl="Télécharger", note="", print="Imprimer", s=[
("Présentation", f"""<p>Solar Duo dimensionne une installation photovoltaïque en suivant la méthode du cours : bilan énergétique, puissance crête, panneaux, batteries, régulateur, onduleur, câbles et protections.</p>
<p>Deux types d'installation : <b>site isolé</b> (autonome, avec batteries) et <b>raccordée au réseau</b> (autoconsommation, sans batterie). Chaque résultat affiche sa formule avec les valeurs, pour pouvoir refaire le calcul. L'interface est en français, en anglais et en espagnol : boutons FR / EN / ES en haut à droite.</p>"""),
("Installer et mettre à jour", f"""<ul><li><b>Windows</b> : {F_WIN} (installeur) ou {F_ZIP} (portable, sans installation). Si Windows affiche « Windows a protégé votre ordinateur », cliquez sur <i>Informations complémentaires</i> › <i>Exécuter quand même</i>.</li>
<li><b>macOS</b> : {F_MAC}. Décompressez, glissez Solar Duo dans Applications. Au premier lancement : clic droit › <i>Ouvrir</i> (l'application n'est pas signée par Apple) ; sinon, dans le Terminal : {XATTR}.</li>
<li><b>Linux</b> : {F_DEB} (double-clic, ou <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (rendre exécutable puis lancer) ou l'archive <code>.tar.gz</code>.</li>
<li><b>En ligne</b>, sans installation : {URL}.</li></ul>
<p>Au démarrage, le logiciel vérifie s'il existe une nouvelle version et l'annonce par un bandeau en haut de la fenêtre. Menu <i>Aide › Rechercher une mise à jour</i>.</p>"""),
("La fenêtre et le projet", """<p>En haut : <b>Nouveau</b>, <b>Ouvrir</b>, <b>Enregistrer</b>, <b>Imprimer / PDF</b> et la langue. Les onglets numérotés suivent la démarche ; les boutons <i>Précédent</i> / <i>Suivant</i> en bas de chaque onglet passent d'une étape à l'autre.</p>
<p>Dans <b>Projet et site</b> : nom du projet, auteur, type d'installation, lieu et période d'utilisation (toute l'année — mois le plus défavorable —, d'avril à septembre, ou moyenne annuelle). Les valeurs d'ensoleillement sont indicatives : pour un projet réel, vérifiez-les sur PVGIS et saisissez les vôtres. La liste <b>Exemples de TD</b> charge l'un des trois exemples corrigés.</p>"""),
("Bilan énergétique", """<p>Ajoutez les appareils (liste d'appareils types ou nouvelle ligne) : puissance, puissance de veille, quantité, durée d'utilisation par jour (J) ou par semaine (S, divisée par 7), Ku, Ks et type de courant (AC ou DC). La veille est comptée sur le reste de la journée.</p>
<p>Le logiciel calcule l'énergie de chaque appareil et l'énergie journalière E<sub>ch</sub>. Ku (facteur d'utilisation) et Ks (facteur de simultanéité) donnent la puissance appelée, qui sert à choisir l'onduleur, les câbles et les protections. Les <b>tableaux Ku et Ks</b> de référence s'ouvrent en haut de l'onglet.</p>"""),
("Panneaux", f"""<p>Choisissez le modèle : DualSun FLASH (fabricant français), Jinko Tiger Neo, ou les modules génériques des TD. Le rendement η<sub>ph</sub> = 0,75 tient compte des pertes (salissure, température, régulateur, batterie, onduleur).</p>
<p>Puissance crête : <b>{PC}</b>. Le logiciel propose la tension du système (12 V jusqu'à 500 Wc, 24 V jusqu'à 2 000 Wc, 48 V au-delà) et le nombre de modules en série et en parallèle. En site isolé, la tension à vide du champ multipliée par 1,2 (grand froid) doit rester sous 120 V (UTE C 15-712-2).</p>"""),
("Batteries", f"""<p>Choisissez la technologie (plomb AGM / GEL / OPzV ou lithium LiFePO₄), la batterie, le nombre de jours d'autonomie J et la profondeur de décharge D (0,7 en plomb, 0,8 en lithium).</p>
<p>Capacité : <b>{CB}</b>. Le logiciel donne le nombre de batteries, leur couplage série / parallèle, l'autonomie réelle et le courant de court-circuit du parc, qui sert à vérifier le pouvoir de coupure des protections.</p>"""),
("Régulateur et onduleur", """<p>Choisissez la marque : <b>Victron</b> (SmartSolar MPPT, Phoenix) ou <b>Studer</b> (VarioTrack, Xtender), jusqu'à 5 kVA, ou un modèle générique (calibre seul).</p>
<p>Le logiciel retient le plus petit modèle qui convient d'après les fiches des fabricants : courant de charge, tension PV maximale par grand froid, puissance PV à la tension batterie ; pour l'onduleur, la puissance appelée et la tension batterie. Si un régulateur ne suffit pas, il en place plusieurs en parallèle, chacun avec son groupe de chaînes.</p>"""),
("Câbles", f"""<p>Indiquez la longueur aller de chaque liaison (panneaux → régulateur, régulateur → batteries, batteries → onduleur) et la chute de tension admise.</p>
<p>Section : <b>{SC}</b>, avec ρ = 0,023 Ω·mm²/m (cuivre), arrondie à la section normalisée supérieure. Vérifiez aussi le courant admissible du câble.</p>"""),
("Protections", """<p>Réglages : marque des protections (Legrand ou Schneider), marque des disjoncteurs courant continu, I<sub>RM</sub> (fusible série maximal, sur la fiche du module), densité de foudroiement Ng, type de bâtiment, paratonnerre et liaison du − batterie.</p>
<p>Pour chaque protection — coupe-circuits porte-fusibles de chaîne (obligatoires), interrupteur-sectionneur, protection batterie, parafoudres DC et AC, différentiel 30 mA type A, mise à la terre — le logiciel affiche la règle de choix, le calcul et la référence du fabricant. Les messages signalent les cas hors gamme.</p>"""),
("Le schéma des protections", """<p>Le schéma unifilaire se dessine automatiquement. Coupe-circuits : fusible sur la lame. Disjoncteurs : croix sur la borne, liaison mécanique en pointillés, déclencheur thermique (carré non fermé) puis magnétique (bosse) sur le pôle protégé. Le − en continu et le neutre en alternatif sont toujours coupés mais pas protégés ; ils sont à gauche.</p>
<p>Le conducteur vert/jaune relie toutes les masses, cadres des panneaux compris, à la barrette et au piquet de terre. Option <b>− batterie relié à la terre</b> (Victron, <i>Wiring Unlimited</i> § 7.7) : une seule liaison, au plus près de la batterie. Option <b>flottant</b> : protections sur les deux polarités et contrôleur d'isolement.</p>"""),
("Documentation technique", """<p>Tout le catalogue : modules, régulateurs, onduleurs, batteries et protections, avec leurs caractéristiques et le lien ↗ vers la fiche du fabricant.</p>
<p>Cliquez sur une ligne pour choisir ce matériel : il est surligné et utilisé dans les calculs. Les lignes grisées ne conviennent pas à l'installation calculée. Le bouton <i>Revenir au choix automatique</i> annule le choix.</p>"""),
("Synthèse, impression et fichiers", """<p>La synthèse rassemble les chiffres clés, le synoptique, la nomenclature du matériel, le schéma et le détail des calculs.</p>
<p><b>Imprimer / PDF</b> imprime la synthèse ; choisissez « Enregistrer au format PDF » comme imprimante pour obtenir un fichier PDF. <b>Enregistrer</b> crée un fichier <code>.solarduo</code> que <b>Ouvrir</b> recharge ; avec l'application installée, un double-clic sur ce fichier l'ouvre aussi.</p>"""),
("Installation raccordée au réseau", """<p>Choisissez <i>Raccordé au réseau</i> dans Projet et site. Les onglets Batteries, Régulateur et onduleur, et Protections sont masqués.</p>
<p>La puissance crête se calcule à partir de la consommation annuelle, de la part à couvrir (souvent 20 à 50 % en autoconsommation), de l'irradiation, du ratio de performance PR (0,75 à 0,85) et du facteur d'orientation / inclinaison (optimum : plein sud, 30°). L'onduleur réseau est choisi entre 0,8 et 1 fois la puissance crête.</p>"""),
("Références et limites", f"""<p>{REFS} ; fiches techniques DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo est une aide au dimensionnement pour la formation. Avant toute réalisation, vérifiez les fiches techniques à jour et les textes en vigueur, et faites valider l'installation par un professionnel qualifié. Signaler une erreur : <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> ou <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["en"] = dict(title="User guide", sub="Photovoltaic system sizing — version 1.0", toc="Contents",
 site="Solar Duo website", app="Online version", dl="Download", note="", print="Print", s=[
("Overview", """<p>Solar Duo sizes a photovoltaic system following the course method: energy balance, peak power, panels, batteries, charge controller, inverter, cables and protection.</p>
<p>Two system types: <b>off-grid</b> (stand-alone, with batteries) and <b>grid-connected</b> (self-consumption, no battery). Every result shows its formula with the values, so the calculation can be checked. The interface is in French, English and Spanish: FR / EN / ES buttons at the top right.</p>"""),
("Install and update", f"""<ul><li><b>Windows</b>: {F_WIN} (installer) or {F_ZIP} (portable, no installation). If Windows shows “Windows protected your PC”, click <i>More info</i> › <i>Run anyway</i>.</li>
<li><b>macOS</b>: {F_MAC}. Unzip and drag Solar Duo to Applications. The first time: right-click › <i>Open</i> (the app is not signed by Apple); otherwise, in Terminal: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (double-click, or <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (make executable then run) or the <code>.tar.gz</code> archive.</li>
<li><b>Online</b>, nothing to install: {URL}.</li></ul>
<p>At start-up the program checks for a new version and shows a banner at the top of the window. Menu <i>Help › Check for updates</i>.</p>"""),
("The window and the project", """<p>At the top: <b>New</b>, <b>Open</b>, <b>Save</b>, <b>Print / PDF</b> and the language. The numbered tabs follow the method; the <i>Previous</i> / <i>Next</i> buttons at the bottom of each tab move between steps.</p>
<p>In <b>Project &amp; site</b>: project name, author, system type, location and period of use (all year — worst month —, April to September, or yearly average). Solar irradiation values are indicative: for a real project, check them on PVGIS and enter your own. The <b>Worked examples</b> list loads one of the three examples.</p>"""),
("Energy balance", """<p>Add the appliances (typical appliance list or new row): power, standby power, quantity, hours of use per day (D) or per week (W, divided by 7), Ku, Ks and current type (AC or DC). Standby is counted over the rest of the day.</p>
<p>The program calculates the energy of each appliance and the daily energy E<sub>ch</sub>. Ku (utilisation factor) and Ks (diversity factor) give the demand power, used to choose the inverter, cables and protection. The reference <b>Ku and Ks tables</b> open at the top of the tab.</p>"""),
("Panels", f"""<p>Choose the model: DualSun FLASH (French manufacturer), Jinko Tiger Neo, or the generic modules from the exercises. The efficiency η<sub>ph</sub> = 0.75 covers losses (soiling, temperature, controller, battery, inverter).</p>
<p>Peak power: <b>{PC}</b>. The program suggests the system voltage (12 V up to 500 Wp, 24 V up to 2,000 Wp, 48 V above) and the number of modules in series and in parallel. Off-grid, the array open-circuit voltage multiplied by 1.2 (extreme cold) must stay below 120 V (UTE C 15-712-2).</p>"""),
("Batteries", f"""<p>Choose the technology (lead-acid AGM / GEL / OPzV or lithium LiFePO₄), the battery, the days of autonomy J and the depth of discharge D (0.7 for lead-acid, 0.8 for lithium).</p>
<p>Capacity: <b>{CB}</b>. The program gives the number of batteries, their series / parallel connection, the actual autonomy and the bank short-circuit current, used to check the breaking capacity of the protection.</p>"""),
("Charge controller and inverter", """<p>Choose the brand: <b>Victron</b> (SmartSolar MPPT, Phoenix) or <b>Studer</b> (VarioTrack, Xtender), up to 5 kVA, or a generic model (rating only).</p>
<p>The program picks the smallest suitable model from the manufacturers' datasheets: charging current, maximum PV voltage in extreme cold, PV power at the battery voltage; for the inverter, the demand power and battery voltage. If one controller is not enough, it uses several in parallel, each with its own group of strings.</p>"""),
("Cables", f"""<p>Enter the one-way length of each link (panels → controller, controller → batteries, batteries → inverter) and the allowed voltage drop.</p>
<p>Cross-section: <b>{SC}</b>, with ρ = 0.023 Ω·mm²/m (copper), rounded up to the next standard size. Also check the cable's current-carrying capacity.</p>"""),
("Protection", """<p>Settings: protection brand (Legrand or Schneider), DC breaker brand, I<sub>RM</sub> (maximum series fuse, on the module datasheet), lightning density Ng, building type, lightning rod and battery − connection.</p>
<p>For each device — string fuse holders (mandatory), switch-disconnector, battery protection, DC and AC surge protectors, 30 mA type A RCD, earthing — the program shows the selection rule, the calculation and the manufacturer's reference. Messages flag out-of-range cases.</p>"""),
("The protection diagram", """<p>The single-line diagram is drawn automatically. Fuse holders: fuse on the blade. Circuit breakers: cross on the terminal, dashed mechanical link, thermal release (open square) then magnetic release (bump) on the protected pole. The − (DC) and the neutral (AC) are always switched but not protected; they are on the left.</p>
<p>The green/yellow conductor links all exposed conductive parts, panel frames included, to the earth bar and earth rod. Option <b>battery − to earth</b> (Victron, <i>Wiring Unlimited</i> § 7.7): a single connection, as close as possible to the battery. Option <b>floating</b>: protection on both polarities and an insulation monitor.</p>"""),
("Technical documentation", """<p>The whole catalogue: modules, controllers, inverters, batteries and protection, with their data and the ↗ link to the manufacturer's datasheet.</p>
<p>Click a row to choose that equipment: it is highlighted and used in the calculations. Greyed rows do not suit the calculated system. The <i>Back to automatic choice</i> button cancels the choice.</p>"""),
("Summary, printing and files", """<p>The summary gathers the key figures, the block diagram, the bill of materials, the diagram and the detailed calculations.</p>
<p><b>Print / PDF</b> prints the summary; choose “Save as PDF” as the printer to get a PDF file. <b>Save</b> creates a <code>.solarduo</code> file that <b>Open</b> reloads; with the installed app, double-clicking the file also opens it.</p>"""),
("Grid-connected system", """<p>Choose <i>Grid-connected</i> in Project &amp; site. The Batteries, Charge controller &amp; inverter and Protection tabs are hidden.</p>
<p>Peak power is calculated from the yearly consumption, the share to cover (often 20 to 50 % for self-consumption), the irradiation, the performance ratio PR (0.75 to 0.85) and the orientation / tilt factor (optimum: due south, 30°). The grid inverter is chosen between 0.8 and 1 times the peak power.</p>"""),
("References and limits", f"""<p>{REFS.replace("Guide de l'installation électrique", "Electrical Installation Guide")}; datasheets from DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo is a sizing aid for training. Before any installation, check the current datasheets and the regulations in force, and have the installation approved by a qualified professional. Report an error: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> or <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["es"] = dict(title="Manual de uso", sub="Dimensionamiento de instalaciones fotovoltaicas — versión 1.0", toc="Índice",
 site="Sitio de Solar Duo", app="Versión en línea", dl="Descargar", note="", print="Imprimir", s=[
("Presentación", """<p>Solar Duo dimensiona una instalación fotovoltaica siguiendo el método del curso: balance energético, potencia pico, paneles, baterías, regulador, inversor, cables y protecciones.</p>
<p>Dos tipos de instalación: <b>aislada</b> (autónoma, con baterías) y <b>conectada a la red</b> (autoconsumo, sin batería). Cada resultado muestra su fórmula con los valores, para poder rehacer el cálculo. La interfaz está en francés, inglés y español: botones FR / EN / ES arriba a la derecha.</p>"""),
("Instalar y actualizar", f"""<ul><li><b>Windows</b>: {F_WIN} (instalador) o {F_ZIP} (portátil, sin instalación). Si Windows muestra «Windows protegió su PC», haga clic en <i>Más información</i> › <i>Ejecutar de todas formas</i>.</li>
<li><b>macOS</b>: {F_MAC}. Descomprima y arrastre Solar Duo a Aplicaciones. La primera vez: clic derecho › <i>Abrir</i> (la aplicación no está firmada por Apple); si no, en el Terminal: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (doble clic, o <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (hacer ejecutable y lanzar) o el archivo <code>.tar.gz</code>.</li>
<li><b>En línea</b>, sin instalar nada: {URL}.</li></ul>
<p>Al arrancar, el programa comprueba si hay una nueva versión y la anuncia con una banda en la parte superior de la ventana. Menú <i>Ayuda › Buscar actualizaciones</i>.</p>"""),
("La ventana y el proyecto", """<p>Arriba: <b>Nuevo</b>, <b>Abrir</b>, <b>Guardar</b>, <b>Imprimir / PDF</b> y el idioma. Las pestañas numeradas siguen el método; los botones <i>Anterior</i> / <i>Siguiente</i> al pie de cada pestaña pasan de una etapa a otra.</p>
<p>En <b>Proyecto y sitio</b>: nombre del proyecto, autor, tipo de instalación, lugar y periodo de uso (todo el año — peor mes —, de abril a septiembre o media anual). Los valores de irradiación son indicativos: para un proyecto real, compruébelos en PVGIS e introduzca los suyos. La lista <b>Ejemplos de TD</b> carga uno de los tres ejemplos resueltos.</p>"""),
("Balance energético", """<p>Añada los aparatos (lista de aparatos tipo o nueva fila): potencia, potencia en espera, cantidad, horas de uso por día (D) o por semana (S, dividida entre 7), Ku, Ks y tipo de corriente (CA o CC). La espera se cuenta en el resto del día.</p>
<p>El programa calcula la energía de cada aparato y la energía diaria E<sub>ch</sub>. Ku (factor de utilización) y Ks (factor de simultaneidad) dan la potencia demandada, que sirve para elegir el inversor, los cables y las protecciones. Las <b>tablas Ku y Ks</b> de referencia se abren en la parte superior de la pestaña.</p>"""),
("Paneles", f"""<p>Elija el modelo: DualSun FLASH (fabricante francés), Jinko Tiger Neo o los módulos genéricos de los ejercicios. El rendimiento η<sub>ph</sub> = 0,75 tiene en cuenta las pérdidas (suciedad, temperatura, regulador, batería, inversor).</p>
<p>Potencia pico: <b>{PC}</b>. El programa propone la tensión del sistema (12 V hasta 500 Wp, 24 V hasta 2000 Wp, 48 V por encima) y el número de módulos en serie y en paralelo. En aislada, la tensión en vacío del campo multiplicada por 1,2 (frío extremo) debe quedar por debajo de 120 V (UTE C 15-712-2).</p>"""),
("Baterías", f"""<p>Elija la tecnología (plomo AGM / GEL / OPzV o litio LiFePO₄), la batería, los días de autonomía J y la profundidad de descarga D (0,7 en plomo, 0,8 en litio).</p>
<p>Capacidad: <b>{CB}</b>. El programa da el número de baterías, su conexión serie / paralelo, la autonomía real y la corriente de cortocircuito del banco, que sirve para comprobar el poder de corte de las protecciones.</p>"""),
("Regulador e inversor", """<p>Elija la marca: <b>Victron</b> (SmartSolar MPPT, Phoenix) o <b>Studer</b> (VarioTrack, Xtender), hasta 5 kVA, o un modelo genérico (solo calibre).</p>
<p>El programa elige el modelo más pequeño que conviene según las fichas de los fabricantes: corriente de carga, tensión FV máxima con frío extremo, potencia FV a la tensión de batería; para el inversor, la potencia demandada y la tensión de batería. Si un regulador no basta, coloca varios en paralelo, cada uno con su grupo de cadenas.</p>"""),
("Cables", f"""<p>Indique la longitud de ida de cada enlace (paneles → regulador, regulador → baterías, baterías → inversor) y la caída de tensión admitida.</p>
<p>Sección: <b>{SC}</b>, con ρ = 0,023 Ω·mm²/m (cobre), redondeada a la sección normalizada superior. Compruebe también la intensidad admisible del cable.</p>"""),
("Protecciones", """<p>Ajustes: marca de las protecciones (Legrand o Schneider), marca de los interruptores de continua, I<sub>RM</sub> (fusible serie máximo, en la ficha del módulo), densidad de rayos Ng, tipo de edificio, pararrayos y conexión del − de batería.</p>
<p>Para cada protección — portafusibles de cadena (obligatorios), interruptor-seccionador, protección de batería, descargadores CC y CA, diferencial 30 mA tipo A, puesta a tierra — el programa muestra la regla de elección, el cálculo y la referencia del fabricante. Los mensajes señalan los casos fuera de gama.</p>"""),
("El esquema de protecciones", """<p>El esquema unifilar se dibuja automáticamente. Portafusibles: fusible sobre la cuchilla. Interruptores automáticos: cruz en el borne, enlace mecánico en línea discontinua, disparador térmico (cuadrado abierto) y luego magnético (joroba) en el polo protegido. El − en continua y el neutro en alterna siempre se cortan pero no se protegen; están a la izquierda.</p>
<p>El conductor verde/amarillo une todas las masas, marcos de los paneles incluidos, a la pletina y a la pica de tierra. Opción <b>− de batería a tierra</b> (Victron, <i>Wiring Unlimited</i> § 7.7): una sola conexión, lo más cerca posible de la batería. Opción <b>flotante</b>: protecciones en las dos polaridades y controlador de aislamiento.</p>"""),
("Documentación técnica", """<p>Todo el catálogo: módulos, reguladores, inversores, baterías y protecciones, con sus características y el enlace ↗ a la ficha del fabricante.</p>
<p>Haga clic en una fila para elegir ese material: queda resaltado y se usa en los cálculos. Las filas grises no convienen a la instalación calculada. El botón <i>Volver a la elección automática</i> anula la elección.</p>"""),
("Síntesis, impresión y archivos", """<p>La síntesis reúne las cifras clave, el sinóptico, la lista de material, el esquema y el detalle de los cálculos.</p>
<p><b>Imprimir / PDF</b> imprime la síntesis; elija «Guardar como PDF» como impresora para obtener un archivo PDF. <b>Guardar</b> crea un archivo <code>.solarduo</code> que <b>Abrir</b> vuelve a cargar; con la aplicación instalada, un doble clic en el archivo también lo abre.</p>"""),
("Instalación conectada a la red", """<p>Elija <i>Conectada a red</i> en Proyecto y sitio. Las pestañas Baterías, Regulador e inversor y Protecciones se ocultan.</p>
<p>La potencia pico se calcula a partir del consumo anual, la parte que se quiere cubrir (a menudo 20 a 50 % en autoconsumo), la irradiación, el rendimiento global PR (0,75 a 0,85) y el factor de orientación / inclinación (óptimo: al sur, 30°). El inversor de red se elige entre 0,8 y 1 vez la potencia pico.</p>"""),
("Referencias y límites", f"""<p>{REFS.replace("Guide de l'installation électrique", "Guía de la instalación eléctrica")}; fichas técnicas de DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo es una ayuda al dimensionamiento para la formación. Antes de cualquier instalación, compruebe las fichas técnicas actualizadas y la normativa vigente, y haga validar la instalación por un profesional cualificado. Informar de un error: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> o <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

# Pour les langues suivantes, l'interface du logiciel s'affiche en anglais : les noms des boutons sont donnés en anglais.
N["pt"] = dict(title="Manual de utilização", sub="Dimensionamento de instalações fotovoltaicas — versão 1.0", toc="Índice",
 site="Sítio do Solar Duo", app="Versão online", dl="Transferir", print="Imprimir",
 note="A interface do programa existe em francês, inglês e espanhol; as capturas mostram a versão inglesa.", s=[
("Apresentação", """<p>O Solar Duo dimensiona uma instalação fotovoltaica seguindo o método do curso: balanço energético, potência de pico, painéis, baterias, regulador, inversor, cabos e proteções.</p>
<p>Dois tipos de instalação: <b>isolada</b> (autónoma, com baterias) e <b>ligada à rede</b> (autoconsumo, sem bateria). Cada resultado mostra a fórmula com os valores, para se poder refazer o cálculo. Interface em francês, inglês e espanhol: botões FR / EN / ES no canto superior direito.</p>"""),
("Instalar e atualizar", f"""<ul><li><b>Windows</b>: {F_WIN} (instalador) ou {F_ZIP} (portátil, sem instalação). Se o Windows mostrar «O Windows protegeu o seu PC», clique em <i>Mais informações</i> › <i>Executar mesmo assim</i>.</li>
<li><b>macOS</b>: {F_MAC}. Descompacte e arraste o Solar Duo para Aplicações. Na primeira vez: clique direito › <i>Abrir</i> (a aplicação não está assinada pela Apple); senão, no Terminal: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (duplo clique, ou <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (tornar executável e iniciar) ou o arquivo <code>.tar.gz</code>.</li>
<li><b>Online</b>, sem instalar nada: {URL}.</li></ul>
<p>Ao arrancar, o programa verifica se existe uma nova versão e anuncia-a numa faixa no topo da janela. Menu <i>Help › Check for updates</i>.</p>"""),
("A janela e o projeto", """<p>No topo: <b>New</b> (novo), <b>Open</b> (abrir), <b>Save</b> (guardar), <b>Print / PDF</b> e a língua. Os separadores numerados seguem o método; os botões <i>Previous</i> / <i>Next</i> no fundo de cada separador passam de uma etapa para a outra.</p>
<p>Em <b>Project &amp; site</b>: nome do projeto, autor, tipo de instalação, local e período de utilização (todo o ano — pior mês —, de abril a setembro, ou média anual). Os valores de irradiação são indicativos: num projeto real, verifique-os no PVGIS e introduza os seus. A lista <b>Worked examples</b> carrega um dos três exemplos resolvidos.</p>"""),
("Balanço energético", """<p>Acrescente os aparelhos (lista de aparelhos típicos ou nova linha): potência, potência em espera, quantidade, horas de utilização por dia (D) ou por semana (W, dividida por 7), Ku, Ks e tipo de corrente (AC ou DC). A espera é contada no resto do dia.</p>
<p>O programa calcula a energia de cada aparelho e a energia diária E<sub>ch</sub>. Ku (fator de utilização) e Ks (fator de simultaneidade) dão a potência solicitada, que serve para escolher o inversor, os cabos e as proteções. As <b>tabelas Ku e Ks</b> de referência abrem-se no topo do separador.</p>"""),
("Painéis", f"""<p>Escolha o modelo: DualSun FLASH (fabricante francês), Jinko Tiger Neo ou os módulos genéricos dos exercícios. O rendimento η<sub>ph</sub> = 0,75 tem em conta as perdas (sujidade, temperatura, regulador, bateria, inversor).</p>
<p>Potência de pico: <b>{PC}</b>. O programa propõe a tensão do sistema (12 V até 500 Wp, 24 V até 2000 Wp, 48 V acima) e o número de módulos em série e em paralelo. Em instalação isolada, a tensão em vazio do campo multiplicada por 1,2 (frio extremo) tem de ficar abaixo de 120 V (UTE C 15-712-2).</p>"""),
("Baterias", f"""<p>Escolha a tecnologia (chumbo AGM / GEL / OPzV ou lítio LiFePO₄), a bateria, os dias de autonomia J e a profundidade de descarga D (0,7 no chumbo, 0,8 no lítio).</p>
<p>Capacidade: <b>{CB}</b>. O programa indica o número de baterias, a ligação série / paralelo, a autonomia real e a corrente de curto-circuito do banco, que serve para verificar o poder de corte das proteções.</p>"""),
("Regulador e inversor", """<p>Escolha a marca: <b>Victron</b> (SmartSolar MPPT, Phoenix) ou <b>Studer</b> (VarioTrack, Xtender), até 5 kVA, ou um modelo genérico (apenas calibre).</p>
<p>O programa escolhe o modelo mais pequeno adequado segundo as fichas dos fabricantes: corrente de carga, tensão FV máxima com frio extremo, potência FV à tensão da bateria; para o inversor, a potência solicitada e a tensão da bateria. Se um regulador não bastar, coloca vários em paralelo, cada um com o seu grupo de fileiras.</p>"""),
("Cabos", f"""<p>Indique o comprimento de ida de cada ligação (painéis → regulador, regulador → baterias, baterias → inversor) e a queda de tensão admitida.</p>
<p>Secção: <b>{SC}</b>, com ρ = 0,023 Ω·mm²/m (cobre), arredondada à secção normalizada superior. Verifique também a corrente admissível do cabo.</p>"""),
("Proteções", """<p>Definições: marca das proteções (Legrand ou Schneider), marca dos disjuntores de corrente contínua, I<sub>RM</sub> (fusível série máximo, na ficha do módulo), densidade de descargas atmosféricas Ng, tipo de edifício, para-raios e ligação do − da bateria.</p>
<p>Para cada proteção — porta-fusíveis de fileira (obrigatórios), interruptor-seccionador, proteção da bateria, descarregadores DC e AC, diferencial 30 mA tipo A, ligação à terra — o programa mostra a regra de escolha, o cálculo e a referência do fabricante. As mensagens assinalam os casos fora de gama.</p>"""),
("O esquema das proteções", """<p>O esquema unifilar é desenhado automaticamente. Porta-fusíveis: fusível sobre a lâmina. Disjuntores: cruz no borne, ligação mecânica a tracejado, disparador térmico (quadrado aberto) e depois magnético (bossa) no polo protegido. O − em contínua e o neutro em alternada são sempre cortados mas não protegidos; ficam à esquerda.</p>
<p>O condutor verde/amarelo liga todas as massas, incluindo as molduras dos painéis, ao barramento e ao elétrodo de terra. Opção <b>− da bateria à terra</b> (Victron, <i>Wiring Unlimited</i> § 7.7): uma única ligação, o mais perto possível da bateria. Opção <b>flutuante</b>: proteções nas duas polaridades e controlador de isolamento.</p>"""),
("Documentação técnica", """<p>Todo o catálogo: módulos, reguladores, inversores, baterias e proteções, com as características e a ligação ↗ para a ficha do fabricante.</p>
<p>Clique numa linha para escolher esse material: fica realçado e é usado nos cálculos. As linhas a cinzento não convêm à instalação calculada. O botão <i>Back to automatic choice</i> anula a escolha.</p>"""),
("Síntese, impressão e ficheiros", """<p>A síntese reúne os valores principais, o sinóptico, a lista de material, o esquema e o detalhe dos cálculos.</p>
<p><b>Print / PDF</b> imprime a síntese; escolha «Guardar como PDF» como impressora para obter um ficheiro PDF. <b>Save</b> cria um ficheiro <code>.solarduo</code> que <b>Open</b> volta a carregar; com a aplicação instalada, um duplo clique no ficheiro também o abre.</p>"""),
("Instalação ligada à rede", """<p>Escolha <i>Grid-connected</i> em Project &amp; site. Os separadores das baterias, do regulador e inversor e das proteções ficam ocultos.</p>
<p>A potência de pico calcula-se a partir do consumo anual, da parte a cobrir (muitas vezes 20 a 50 % em autoconsumo), da irradiação, do índice de desempenho PR (0,75 a 0,85) e do fator de orientação / inclinação (ótimo: virado a sul, 30°). O inversor de rede é escolhido entre 0,8 e 1 vez a potência de pico.</p>"""),
("Referências e limites", f"""<p>{REFS} ; fichas técnicas DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>O Solar Duo é uma ajuda ao dimensionamento para a formação. Antes de qualquer realização, verifique as fichas técnicas atualizadas e a regulamentação em vigor, e mande validar a instalação por um profissional qualificado. Comunicar um erro: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> ou <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["de"] = dict(title="Bedienungsanleitung", sub="Auslegung von Photovoltaikanlagen — Version 1.0", toc="Inhalt",
 site="Website von Solar Duo", app="Online-Version", dl="Herunterladen", print="Drucken",
 note="Die Programmoberfläche gibt es auf Französisch, Englisch und Spanisch; die Bilder zeigen die englische Fassung.", s=[
("Überblick", """<p>Solar Duo legt eine Photovoltaikanlage nach der Methode aus dem Unterricht aus: Energiebilanz, Spitzenleistung, Module, Batterien, Laderegler, Wechselrichter, Kabel und Schutzeinrichtungen.</p>
<p>Zwei Anlagentypen: <b>Inselanlage</b> (autark, mit Batterien) und <b>netzgekoppelt</b> (Eigenverbrauch, ohne Batterie). Jedes Ergebnis zeigt seine Formel mit den Werten, damit die Rechnung nachvollzogen werden kann. Oberfläche auf Französisch, Englisch und Spanisch: Schaltflächen FR / EN / ES oben rechts.</p>"""),
("Installieren und aktualisieren", f"""<ul><li><b>Windows</b>: {F_WIN} (Installationsprogramm) oder {F_ZIP} (portabel, ohne Installation). Zeigt Windows „Der Computer wurde durch Windows geschützt“, auf <i>Weitere Informationen</i> › <i>Trotzdem ausführen</i> klicken.</li>
<li><b>macOS</b>: {F_MAC}. Entpacken und Solar Duo in „Programme“ ziehen. Beim ersten Start: Rechtsklick › <i>Öffnen</i> (die App ist nicht von Apple signiert); sonst im Terminal: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (Doppelklick oder <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (ausführbar machen und starten) oder das Archiv <code>.tar.gz</code>.</li>
<li><b>Online</b>, ohne Installation: {URL}.</li></ul>
<p>Beim Start prüft das Programm, ob es eine neue Version gibt, und zeigt dann oben im Fenster einen Hinweis. Menü <i>Help › Check for updates</i>.</p>"""),
("Das Fenster und das Projekt", """<p>Oben: <b>New</b> (neu), <b>Open</b> (öffnen), <b>Save</b> (speichern), <b>Print / PDF</b> und die Sprache. Die nummerierten Reiter folgen dem Vorgehen; die Schaltflächen <i>Previous</i> / <i>Next</i> unten auf jedem Reiter führen von Schritt zu Schritt.</p>
<p>Unter <b>Project &amp; site</b>: Projektname, Verfasser, Anlagentyp, Standort und Nutzungszeitraum (ganzjährig — ungünstigster Monat —, April bis September oder Jahresmittel). Die Einstrahlungswerte sind Richtwerte: Prüfen Sie sie für ein echtes Projekt mit PVGIS und geben Sie Ihre eigenen ein. Die Liste <b>Worked examples</b> lädt eines der drei durchgerechneten Beispiele.</p>"""),
("Energiebilanz", """<p>Geräte hinzufügen (Liste typischer Geräte oder neue Zeile): Leistung, Standby-Leistung, Anzahl, Nutzungsdauer pro Tag (D) oder pro Woche (W, geteilt durch 7), Ku, Ks und Stromart (AC oder DC). Der Standby zählt für den Rest des Tages.</p>
<p>Das Programm berechnet die Energie jedes Geräts und die Tagesenergie E<sub>ch</sub>. Ku (Ausnutzungsfaktor) und Ks (Gleichzeitigkeitsfaktor) ergeben den Leistungsbedarf, nach dem Wechselrichter, Kabel und Schutzeinrichtungen gewählt werden. Die <b>Ku- und Ks-Tabellen</b> öffnen sich oben im Reiter.</p>"""),
("Module", f"""<p>Modell wählen: DualSun FLASH (französischer Hersteller), Jinko Tiger Neo oder die allgemeinen Module aus den Übungen. Der Wirkungsgrad η<sub>ph</sub> = 0,75 berücksichtigt die Verluste (Verschmutzung, Temperatur, Regler, Batterie, Wechselrichter).</p>
<p>Spitzenleistung: <b>{PC}</b>. Das Programm schlägt die Systemspannung vor (12 V bis 500 Wp, 24 V bis 2000 Wp, darüber 48 V) sowie die Zahl der Module in Reihe und parallel. Bei Inselanlagen muss die Leerlaufspannung des Generators mal 1,2 (strenge Kälte) unter 120 V bleiben (UTE C 15-712-2).</p>"""),
("Batterien", f"""<p>Technologie (Blei AGM / GEL / OPzV oder Lithium LiFePO₄), Batterie, Autonomietage J und Entladetiefe D (0,7 bei Blei, 0,8 bei Lithium) wählen.</p>
<p>Kapazität: <b>{CB}</b>. Das Programm gibt die Zahl der Batterien, ihre Reihen- / Parallelschaltung, die tatsächliche Autonomie und den Kurzschlussstrom der Batteriebank an, mit dem das Ausschaltvermögen der Schutzeinrichtungen geprüft wird.</p>"""),
("Laderegler und Wechselrichter", """<p>Marke wählen: <b>Victron</b> (SmartSolar MPPT, Phoenix) oder <b>Studer</b> (VarioTrack, Xtender), bis 5 kVA, oder ein allgemeines Modell (nur Bemessungswert).</p>
<p>Das Programm wählt nach den Herstellerdatenblättern das kleinste passende Modell: Ladestrom, maximale PV-Spannung bei strenger Kälte, PV-Leistung bei Batteriespannung; beim Wechselrichter den Leistungsbedarf und die Batteriespannung. Reicht ein Regler nicht, werden mehrere parallel eingesetzt, jeder mit seiner Stranggruppe.</p>"""),
("Kabel", f"""<p>Die einfache Länge jeder Verbindung (Module → Regler, Regler → Batterien, Batterien → Wechselrichter) und den zulässigen Spannungsfall eingeben.</p>
<p>Querschnitt: <b>{SC}</b>, mit ρ = 0,023 Ω·mm²/m (Kupfer), aufgerundet auf den nächsten Normquerschnitt. Auch die Strombelastbarkeit des Kabels prüfen.</p>"""),
("Schutzeinrichtungen", """<p>Einstellungen: Marke der Schutzeinrichtungen (Legrand oder Schneider), Marke der DC-Leitungsschutzschalter, I<sub>RM</sub> (maximale Reihensicherung, auf dem Moduldatenblatt), Blitzdichte Ng, Gebäudeart, Blitzableiter und Anschluss des Batterie-Minus.</p>
<p>Für jede Einrichtung — Strangsicherungstrenner (Pflicht), Lasttrennschalter, Batterieschutz, DC- und AC-Überspannungsschutz, FI 30 mA Typ A, Erdung — zeigt das Programm Auswahlregel, Berechnung und Herstellerartikel. Meldungen weisen auf Fälle außerhalb des Sortiments hin.</p>"""),
("Der Schaltplan", """<p>Das Einliniendiagramm wird automatisch gezeichnet. Sicherungstrenner: Sicherung auf dem Schaltmesser. Leitungsschutzschalter: Kreuz an der Klemme, gestrichelte mechanische Verbindung, thermischer Auslöser (offenes Quadrat) und darunter magnetischer Auslöser (Bogen) am geschützten Pol. Das Minus bei Gleichstrom und der Neutralleiter bei Wechselstrom werden immer geschaltet, aber nicht geschützt; sie liegen links.</p>
<p>Der grün-gelbe Leiter verbindet alle Körper, Modulrahmen eingeschlossen, mit der Erdungsschiene und dem Erder. Option <b>Batterie-Minus geerdet</b> (Victron, <i>Wiring Unlimited</i> § 7.7): eine einzige Verbindung, möglichst nah an der Batterie. Option <b>erdfrei</b>: Schutz auf beiden Polen und Isolationsüberwachung.</p>"""),
("Technische Dokumentation", """<p>Der ganze Katalog: Module, Regler, Wechselrichter, Batterien und Schutzeinrichtungen, mit Kenndaten und dem Link ↗ zum Herstellerdatenblatt.</p>
<p>Ein Klick auf eine Zeile wählt dieses Material: Es wird hervorgehoben und in den Berechnungen verwendet. Grau dargestellte Zeilen passen nicht zur berechneten Anlage. Die Schaltfläche <i>Back to automatic choice</i> hebt die Wahl auf.</p>"""),
("Zusammenfassung, Druck und Dateien", """<p>Die Zusammenfassung enthält die wichtigsten Werte, die Übersicht, die Materialliste, den Schaltplan und die ausführliche Berechnung.</p>
<p><b>Print / PDF</b> druckt die Zusammenfassung; als Drucker „Als PDF speichern“ wählen, um eine PDF-Datei zu erhalten. <b>Save</b> erzeugt eine Datei <code>.solarduo</code>, die <b>Open</b> wieder lädt; mit der installierten Anwendung öffnet auch ein Doppelklick auf die Datei.</p>"""),
("Netzgekoppelte Anlage", """<p>Unter Project &amp; site <i>Grid-connected</i> wählen. Die Reiter für Batterien, Laderegler und Wechselrichter sowie Schutzeinrichtungen werden ausgeblendet.</p>
<p>Die Spitzenleistung ergibt sich aus dem Jahresverbrauch, dem zu deckenden Anteil (beim Eigenverbrauch oft 20 bis 50 %), der Einstrahlung, der Performance Ratio PR (0,75 bis 0,85) und dem Ausrichtungs- / Neigungsfaktor (optimal: Süden, 30°). Der Netzwechselrichter wird zwischen dem 0,8- und 1-Fachen der Spitzenleistung gewählt.</p>"""),
("Quellen und Grenzen", f"""<p>{REFS} ; Datenblätter von DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo ist eine Auslegungshilfe für die Ausbildung. Vor jeder Ausführung die aktuellen Datenblätter und geltenden Vorschriften prüfen und die Anlage von einer Fachkraft abnehmen lassen. Fehler melden: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> oder <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["it"] = dict(title="Manuale d'uso", sub="Dimensionamento di impianti fotovoltaici — versione 1.0", toc="Indice",
 site="Sito di Solar Duo", app="Versione online", dl="Scarica", print="Stampa",
 note="L'interfaccia del programma è in francese, inglese e spagnolo; le immagini mostrano la versione inglese.", s=[
("Presentazione", """<p>Solar Duo dimensiona un impianto fotovoltaico seguendo il metodo del corso: bilancio energetico, potenza di picco, pannelli, batterie, regolatore, inverter, cavi e protezioni.</p>
<p>Due tipi di impianto: <b>isolato</b> (autonomo, con batterie) e <b>connesso alla rete</b> (autoconsumo, senza batteria). Ogni risultato mostra la formula con i valori, per poter rifare il calcolo. Interfaccia in francese, inglese e spagnolo: pulsanti FR / EN / ES in alto a destra.</p>"""),
("Installare e aggiornare", f"""<ul><li><b>Windows</b>: {F_WIN} (programma di installazione) o {F_ZIP} (portatile, senza installazione). Se Windows mostra «PC protetto da Windows», fare clic su <i>Ulteriori informazioni</i> › <i>Esegui comunque</i>.</li>
<li><b>macOS</b>: {F_MAC}. Decomprimere e trascinare Solar Duo in Applicazioni. Al primo avvio: clic destro › <i>Apri</i> (l'app non è firmata da Apple); altrimenti, nel Terminale: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (doppio clic, oppure <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (renderlo eseguibile e avviarlo) o l'archivio <code>.tar.gz</code>.</li>
<li><b>Online</b>, senza installare nulla: {URL}.</li></ul>
<p>All'avvio il programma verifica se esiste una nuova versione e la segnala con una banda in cima alla finestra. Menu <i>Help › Check for updates</i>.</p>"""),
("La finestra e il progetto", """<p>In alto: <b>New</b> (nuovo), <b>Open</b> (apri), <b>Save</b> (salva), <b>Print / PDF</b> e la lingua. Le schede numerate seguono il metodo; i pulsanti <i>Previous</i> / <i>Next</i> in fondo a ogni scheda passano da una fase all'altra.</p>
<p>In <b>Project &amp; site</b>: nome del progetto, autore, tipo di impianto, luogo e periodo di utilizzo (tutto l'anno — mese peggiore —, da aprile a settembre o media annua). I valori di irraggiamento sono indicativi: per un progetto reale, verificarli su PVGIS e inserire i propri. L'elenco <b>Worked examples</b> carica uno dei tre esempi svolti.</p>"""),
("Bilancio energetico", """<p>Aggiungere gli apparecchi (elenco di apparecchi tipo o nuova riga): potenza, potenza in standby, quantità, ore di utilizzo al giorno (D) o alla settimana (W, divise per 7), Ku, Ks e tipo di corrente (AC o DC). Lo standby è contato sul resto della giornata.</p>
<p>Il programma calcola l'energia di ogni apparecchio e l'energia giornaliera E<sub>ch</sub>. Ku (fattore di utilizzazione) e Ks (fattore di contemporaneità) danno la potenza richiesta, che serve a scegliere inverter, cavi e protezioni. Le <b>tabelle Ku e Ks</b> di riferimento si aprono in cima alla scheda.</p>"""),
("Pannelli", f"""<p>Scegliere il modello: DualSun FLASH (produttore francese), Jinko Tiger Neo o i moduli generici degli esercizi. Il rendimento η<sub>ph</sub> = 0,75 tiene conto delle perdite (sporcizia, temperatura, regolatore, batteria, inverter).</p>
<p>Potenza di picco: <b>{PC}</b>. Il programma propone la tensione del sistema (12 V fino a 500 Wp, 24 V fino a 2000 Wp, 48 V oltre) e il numero di moduli in serie e in parallelo. Negli impianti isolati la tensione a vuoto del campo moltiplicata per 1,2 (freddo intenso) deve restare sotto 120 V (UTE C 15-712-2).</p>"""),
("Batterie", f"""<p>Scegliere la tecnologia (piombo AGM / GEL / OPzV o litio LiFePO₄), la batteria, i giorni di autonomia J e la profondità di scarica D (0,7 per il piombo, 0,8 per il litio).</p>
<p>Capacità: <b>{CB}</b>. Il programma indica il numero di batterie, il collegamento serie / parallelo, l'autonomia reale e la corrente di cortocircuito del banco, che serve a verificare il potere di interruzione delle protezioni.</p>"""),
("Regolatore e inverter", """<p>Scegliere la marca: <b>Victron</b> (SmartSolar MPPT, Phoenix) o <b>Studer</b> (VarioTrack, Xtender), fino a 5 kVA, o un modello generico (solo taglia).</p>
<p>Il programma sceglie il modello più piccolo adatto secondo le schede dei produttori: corrente di carica, tensione FV massima con freddo intenso, potenza FV alla tensione della batteria; per l'inverter, la potenza richiesta e la tensione della batteria. Se un regolatore non basta, ne mette diversi in parallelo, ciascuno con il proprio gruppo di stringhe.</p>"""),
("Cavi", f"""<p>Indicare la lunghezza di andata di ogni collegamento (pannelli → regolatore, regolatore → batterie, batterie → inverter) e la caduta di tensione ammessa.</p>
<p>Sezione: <b>{SC}</b>, con ρ = 0,023 Ω·mm²/m (rame), arrotondata alla sezione normalizzata superiore. Verificare anche la portata del cavo.</p>"""),
("Protezioni", """<p>Impostazioni: marca delle protezioni (Legrand o Schneider), marca degli interruttori in corrente continua, I<sub>RM</sub> (fusibile serie massimo, sulla scheda del modulo), densità di fulminazione Ng, tipo di edificio, parafulmine e collegamento del − della batteria.</p>
<p>Per ogni protezione — portafusibili di stringa (obbligatori), interruttore-sezionatore, protezione della batteria, scaricatori DC e AC, differenziale 30 mA tipo A, messa a terra — il programma mostra la regola di scelta, il calcolo e il codice del produttore. I messaggi segnalano i casi fuori gamma.</p>"""),
("Lo schema delle protezioni", """<p>Lo schema unifilare si disegna automaticamente. Portafusibili: fusibile sulla lama. Interruttori automatici: croce sul morsetto, collegamento meccanico tratteggiato, sganciatore termico (quadrato aperto) e poi magnetico (gobba) sul polo protetto. Il − in continua e il neutro in alternata sono sempre sezionati ma non protetti; si trovano a sinistra.</p>
<p>Il conduttore giallo-verde collega tutte le masse, cornici dei pannelli comprese, alla barra e al dispersore di terra. Opzione <b>− batteria a terra</b> (Victron, <i>Wiring Unlimited</i> § 7.7): un solo collegamento, il più vicino possibile alla batteria. Opzione <b>flottante</b>: protezioni su entrambe le polarità e controllore di isolamento.</p>"""),
("Documentazione tecnica", """<p>Tutto il catalogo: moduli, regolatori, inverter, batterie e protezioni, con le caratteristiche e il link ↗ alla scheda del produttore.</p>
<p>Fare clic su una riga per scegliere quel materiale: viene evidenziato e usato nei calcoli. Le righe in grigio non sono adatte all'impianto calcolato. Il pulsante <i>Back to automatic choice</i> annulla la scelta.</p>"""),
("Sintesi, stampa e file", """<p>La sintesi riunisce i valori principali, il sinottico, la distinta dei materiali, lo schema e il dettaglio dei calcoli.</p>
<p><b>Print / PDF</b> stampa la sintesi; scegliere «Salva come PDF» come stampante per ottenere un file PDF. <b>Save</b> crea un file <code>.solarduo</code> che <b>Open</b> ricarica; con l'applicazione installata, anche un doppio clic sul file lo apre.</p>"""),
("Impianto connesso alla rete", """<p>Scegliere <i>Grid-connected</i> in Project &amp; site. Le schede delle batterie, del regolatore e inverter e delle protezioni vengono nascoste.</p>
<p>La potenza di picco si calcola dal consumo annuo, dalla quota da coprire (spesso dal 20 al 50 % in autoconsumo), dall'irraggiamento, dal performance ratio PR (0,75–0,85) e dal fattore di orientamento / inclinazione (ottimo: sud, 30°). L'inverter di rete è scelto tra 0,8 e 1 volta la potenza di picco.</p>"""),
("Riferimenti e limiti", f"""<p>{REFS} ; schede tecniche DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo è un aiuto al dimensionamento per la formazione. Prima di ogni realizzazione verificare le schede tecniche aggiornate e le norme in vigore, e far validare l'impianto da un professionista qualificato. Segnalare un errore: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> o <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["el"] = dict(title="Εγχειρίδιο χρήσης", sub="Διαστασιολόγηση φωτοβολταϊκών εγκαταστάσεων — έκδοση 1.0", toc="Περιεχόμενα",
 site="Ιστότοπος του Solar Duo", app="Online έκδοση", dl="Λήψη", print="Εκτύπωση",
 note="Η διεπαφή του προγράμματος υπάρχει στα γαλλικά, αγγλικά και ισπανικά· οι εικόνες δείχνουν την αγγλική έκδοση.", s=[
("Παρουσίαση", """<p>Το Solar Duo διαστασιολογεί μια φωτοβολταϊκή εγκατάσταση ακολουθώντας τη μέθοδο του μαθήματος: ενεργειακό ισοζύγιο, ισχύς αιχμής, πάνελ, μπαταρίες, ρυθμιστής φόρτισης, αντιστροφέας, καλώδια και προστασίες.</p>
<p>Δύο τύποι εγκατάστασης: <b>αυτόνομη</b> (με μπαταρίες) και <b>συνδεδεμένη στο δίκτυο</b> (ιδιοκατανάλωση, χωρίς μπαταρία). Κάθε αποτέλεσμα δείχνει τον τύπο με τις τιμές, ώστε να μπορεί να ελεγχθεί ο υπολογισμός. Διεπαφή στα γαλλικά, αγγλικά και ισπανικά: κουμπιά FR / EN / ES πάνω δεξιά.</p>"""),
("Εγκατάσταση και ενημέρωση", f"""<ul><li><b>Windows</b>: {F_WIN} (πρόγραμμα εγκατάστασης) ή {F_ZIP} (φορητό, χωρίς εγκατάσταση). Αν τα Windows εμφανίσουν «Τα Windows προστάτευσαν τον υπολογιστή σας», πατήστε <i>Περισσότερες πληροφορίες</i> › <i>Εκτέλεση οπωσδήποτε</i>.</li>
<li><b>macOS</b>: {F_MAC}. Αποσυμπιέστε και σύρετε το Solar Duo στις Εφαρμογές. Την πρώτη φορά: δεξί κλικ › <i>Άνοιγμα</i> (η εφαρμογή δεν είναι υπογεγραμμένη από την Apple)· αλλιώς, στο Τερματικό: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (διπλό κλικ ή <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (κάντε το εκτελέσιμο και εκκινήστε) ή το αρχείο <code>.tar.gz</code>.</li>
<li><b>Online</b>, χωρίς εγκατάσταση: {URL}.</li></ul>
<p>Κατά την εκκίνηση το πρόγραμμα ελέγχει αν υπάρχει νέα έκδοση και την ανακοινώνει σε μια λωρίδα στο πάνω μέρος του παραθύρου. Μενού <i>Help › Check for updates</i>.</p>"""),
("Το παράθυρο και το έργο", """<p>Επάνω: <b>New</b> (νέο), <b>Open</b> (άνοιγμα), <b>Save</b> (αποθήκευση), <b>Print / PDF</b> και η γλώσσα. Οι αριθμημένες καρτέλες ακολουθούν τη μέθοδο· τα κουμπιά <i>Previous</i> / <i>Next</i> στο κάτω μέρος κάθε καρτέλας περνούν από βήμα σε βήμα.</p>
<p>Στο <b>Project &amp; site</b>: όνομα έργου, συντάκτης, τύπος εγκατάστασης, τοποθεσία και περίοδος χρήσης (όλο το έτος — χειρότερος μήνας —, Απρίλιος έως Σεπτέμβριος ή ετήσιος μέσος όρος). Οι τιμές ακτινοβολίας είναι ενδεικτικές: για πραγματικό έργο ελέγξτε τες στο PVGIS και εισάγετε τις δικές σας. Η λίστα <b>Worked examples</b> φορτώνει ένα από τα τρία λυμένα παραδείγματα.</p>"""),
("Ενεργειακό ισοζύγιο", """<p>Προσθέστε τις συσκευές (λίστα τυπικών συσκευών ή νέα γραμμή): ισχύς, ισχύς αναμονής, ποσότητα, ώρες χρήσης ανά ημέρα (D) ή ανά εβδομάδα (W, διαιρούμενες με 7), Ku, Ks και είδος ρεύματος (AC ή DC). Η αναμονή μετράει για το υπόλοιπο της ημέρας.</p>
<p>Το πρόγραμμα υπολογίζει την ενέργεια κάθε συσκευής και την ημερήσια ενέργεια E<sub>ch</sub>. Οι Ku (συντελεστής χρήσης) και Ks (συντελεστής ταυτοχρονισμού) δίνουν την απαιτούμενη ισχύ, με την οποία επιλέγονται ο αντιστροφέας, τα καλώδια και οι προστασίες. Οι <b>πίνακες Ku και Ks</b> ανοίγουν στο πάνω μέρος της καρτέλας.</p>"""),
("Πάνελ", f"""<p>Επιλέξτε μοντέλο: DualSun FLASH (γαλλικός κατασκευαστής), Jinko Tiger Neo ή τα γενικά πλαίσια των ασκήσεων. Ο βαθμός απόδοσης η<sub>ph</sub> = 0,75 καλύπτει τις απώλειες (ρύπανση, θερμοκρασία, ρυθμιστής, μπαταρία, αντιστροφέας).</p>
<p>Ισχύς αιχμής: <b>{PC}</b>. Το πρόγραμμα προτείνει την τάση του συστήματος (12 V έως 500 Wp, 24 V έως 2000 Wp, 48 V πάνω από αυτό) και τον αριθμό πλαισίων σε σειρά και παράλληλα. Σε αυτόνομη εγκατάσταση, η τάση ανοιχτοκυκλώματος του πεδίου επί 1,2 (έντονο κρύο) πρέπει να μένει κάτω από 120 V (UTE C 15-712-2).</p>"""),
("Μπαταρίες", f"""<p>Επιλέξτε τεχνολογία (μολύβδου AGM / GEL / OPzV ή λιθίου LiFePO₄), μπαταρία, ημέρες αυτονομίας J και βάθος εκφόρτισης D (0,7 για μόλυβδο, 0,8 για λίθιο).</p>
<p>Χωρητικότητα: <b>{CB}</b>. Το πρόγραμμα δίνει τον αριθμό μπαταριών, τη σύνδεση σε σειρά / παράλληλα, την πραγματική αυτονομία και το ρεύμα βραχυκύκλωσης της συστοιχίας, με το οποίο ελέγχεται η ικανότητα διακοπής των προστασιών.</p>"""),
("Ρυθμιστής και αντιστροφέας", """<p>Επιλέξτε μάρκα: <b>Victron</b> (SmartSolar MPPT, Phoenix) ή <b>Studer</b> (VarioTrack, Xtender), έως 5 kVA, ή γενικό μοντέλο (μόνο ονομαστική τιμή).</p>
<p>Το πρόγραμμα επιλέγει το μικρότερο κατάλληλο μοντέλο από τα φύλλα δεδομένων: ρεύμα φόρτισης, μέγιστη τάση ΦΒ σε έντονο κρύο, ισχύς ΦΒ στην τάση μπαταρίας· για τον αντιστροφέα, την απαιτούμενη ισχύ και την τάση μπαταρίας. Αν ένας ρυθμιστής δεν αρκεί, τοποθετεί περισσότερους παράλληλα, ο καθένας με τη δική του ομάδα στοιχειοσειρών.</p>"""),
("Καλώδια", f"""<p>Δώστε το μήκος μετάβασης κάθε σύνδεσης (πάνελ → ρυθμιστής, ρυθμιστής → μπαταρίες, μπαταρίες → αντιστροφέας) και την επιτρεπόμενη πτώση τάσης.</p>
<p>Διατομή: <b>{SC}</b>, με ρ = 0,023 Ω·mm²/m (χαλκός), στρογγυλεμένη στην επόμενη τυποποιημένη διατομή. Ελέγξτε και την επιτρεπόμενη ένταση του καλωδίου.</p>"""),
("Προστασίες", """<p>Ρυθμίσεις: μάρκα προστασιών (Legrand ή Schneider), μάρκα αυτόματων διακοπτών DC, I<sub>RM</sub> (μέγιστη ασφάλεια σειράς, στο φύλλο δεδομένων του πλαισίου), πυκνότητα κεραυνών Ng, τύπος κτιρίου, αλεξικέραυνο και σύνδεση του − της μπαταρίας.</p>
<p>Για κάθε προστασία — ασφαλειοαποζεύκτες στοιχειοσειράς (υποχρεωτικοί), διακόπτης-αποζεύκτης, προστασία μπαταρίας, απαγωγοί DC και AC, διαφορικό 30 mA τύπου A, γείωση — το πρόγραμμα δείχνει τον κανόνα επιλογής, τον υπολογισμό και τον κωδικό του κατασκευαστή. Τα μηνύματα επισημαίνουν περιπτώσεις εκτός γκάμας.</p>"""),
("Το σχέδιο των προστασιών", """<p>Το μονογραμμικό σχέδιο σχεδιάζεται αυτόματα. Ασφαλειοαποζεύκτες: ασφάλεια πάνω στο μαχαίρι. Αυτόματοι διακόπτες: σταυρός στον ακροδέκτη, διακεκομμένη μηχανική σύνδεση, θερμικό στοιχείο (ανοιχτό τετράγωνο) και έπειτα μαγνητικό (καμπύλη) στον προστατευμένο πόλο. Το − στο συνεχές και ο ουδέτερος στο εναλλασσόμενο διακόπτονται πάντα αλλά δεν προστατεύονται· βρίσκονται αριστερά.</p>
<p>Ο πράσινος/κίτρινος αγωγός συνδέει όλα τα εκτεθειμένα αγώγιμα μέρη, μαζί με τα πλαίσια των πάνελ, με τη μπάρα και το ηλεκτρόδιο γείωσης. Επιλογή <b>− μπαταρίας στη γη</b> (Victron, <i>Wiring Unlimited</i> § 7.7): μία μόνο σύνδεση, όσο πιο κοντά στη μπαταρία. Επιλογή <b>αγείωτο</b>: προστασίες και στις δύο πολικότητες και επιτηρητής μόνωσης.</p>"""),
("Τεχνική τεκμηρίωση", """<p>Όλος ο κατάλογος: πλαίσια, ρυθμιστές, αντιστροφείς, μπαταρίες και προστασίες, με τα χαρακτηριστικά τους και τον σύνδεσμο ↗ προς το φύλλο δεδομένων.</p>
<p>Κάντε κλικ σε μια γραμμή για να επιλέξετε αυτόν τον εξοπλισμό: επισημαίνεται και χρησιμοποιείται στους υπολογισμούς. Οι γκρίζες γραμμές δεν ταιριάζουν στην υπολογισμένη εγκατάσταση. Το κουμπί <i>Back to automatic choice</i> ακυρώνει την επιλογή.</p>"""),
("Σύνοψη, εκτύπωση και αρχεία", """<p>Η σύνοψη συγκεντρώνει τα βασικά μεγέθη, το συνοπτικό διάγραμμα, τον κατάλογο υλικών, το σχέδιο και την ανάλυση των υπολογισμών.</p>
<p>Το <b>Print / PDF</b> εκτυπώνει τη σύνοψη· επιλέξτε «Αποθήκευση ως PDF» ως εκτυπωτή για να πάρετε αρχείο PDF. Το <b>Save</b> δημιουργεί ένα αρχείο <code>.solarduo</code> που το <b>Open</b> ξαναφορτώνει· με την εγκατεστημένη εφαρμογή, το αρχείο ανοίγει και με διπλό κλικ.</p>"""),
("Εγκατάσταση συνδεδεμένη στο δίκτυο", """<p>Επιλέξτε <i>Grid-connected</i> στο Project &amp; site. Οι καρτέλες για τις μπαταρίες, τον ρυθμιστή και τον αντιστροφέα και τις προστασίες κρύβονται.</p>
<p>Η ισχύς αιχμής υπολογίζεται από την ετήσια κατανάλωση, το ποσοστό που θα καλυφθεί (συχνά 20 έως 50 % στην ιδιοκατανάλωση), την ακτινοβολία, τον λόγο απόδοσης PR (0,75 έως 0,85) και τον συντελεστή προσανατολισμού / κλίσης (βέλτιστο: νότος, 30°). Ο αντιστροφέας δικτύου επιλέγεται μεταξύ 0,8 και 1 φοράς την ισχύ αιχμής.</p>"""),
("Αναφορές και όρια", f"""<p>{REFS} ; φύλλα δεδομένων DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Το Solar Duo είναι βοήθημα διαστασιολόγησης για την εκπαίδευση. Πριν από κάθε εγκατάσταση, ελέγξτε τα τρέχοντα φύλλα δεδομένων και τους ισχύοντες κανονισμούς και ζητήστε έγκριση της εγκατάστασης από αδειούχο επαγγελματία. Αναφορά σφάλματος: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> ή <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["zh"] = dict(title="使用手册", sub="光伏系统设计计算 — 1.0 版", toc="目录",
 site="Solar Duo 网站", app="在线版", dl="下载", print="打印",
 note="软件界面提供法语、英语和西班牙语；截图为英文界面。", s=[
("简介", """<p>Solar Duo 按照课程方法进行光伏系统设计计算：能耗统计、峰值功率、光伏组件、蓄电池、充电控制器、逆变器、电缆和保护电器。</p>
<p>两种系统类型：<b>离网</b>（独立运行，带蓄电池）和<b>并网</b>（自发自用，不带蓄电池）。每个结果都显示公式和代入的数值，便于核对计算。界面提供法语、英语和西班牙语：右上角的 FR / EN / ES 按钮。</p>"""),
("安装与更新", f"""<ul><li><b>Windows</b>：{F_WIN}（安装程序）或 {F_ZIP}（便携版，无需安装）。如果 Windows 显示“Windows 已保护你的电脑”，请点击<i>更多信息</i> › <i>仍要运行</i>。</li>
<li><b>macOS</b>：{F_MAC}。解压后将 Solar Duo 拖入“应用程序”。首次打开：右键 › <i>打开</i>（该应用未经 Apple 签名）；或在终端中执行：{XATTR}。</li>
<li><b>Linux</b>：{F_DEB}（双击，或 <code>sudo apt install ./solar-duo_amd64.deb</code>）、{F_APP}（设为可执行后运行）或 <code>.tar.gz</code> 压缩包。</li>
<li><b>在线版</b>，无需安装：{URL}。</li></ul>
<p>启动时，软件会检查是否有新版本，并在窗口顶部显示提示条。菜单：<i>Help › Check for updates</i>。</p>"""),
("窗口与项目", """<p>顶部：<b>New</b>（新建）、<b>Open</b>（打开）、<b>Save</b>（保存）、<b>Print / PDF</b> 以及语言。带编号的选项卡按计算步骤排列；每个选项卡底部的 <i>Previous</i> / <i>Next</i> 按钮用于切换步骤。</p>
<p>在 <b>Project &amp; site</b> 中：项目名称、作者、系统类型、地点和使用时段（全年——最不利月份——、4 月至 9 月，或年平均）。日照数值仅供参考：实际项目请在 PVGIS 上核对并输入自己的数据。<b>Worked examples</b> 列表可载入三个已解答的例题之一。</p>"""),
("能耗统计", """<p>添加电器（从常用电器列表中选择或新建一行）：功率、待机功率、数量、每天（D）或每周（W，除以 7）的使用小时数、Ku、Ks 以及电流类型（AC 或 DC）。待机功耗按当天剩余时间计算。</p>
<p>软件计算每台电器的能耗和日耗电量 E<sub>ch</sub>。Ku（利用系数）和 Ks（同时系数）得出需用功率，用于选择逆变器、电缆和保护电器。选项卡顶部可展开 <b>Ku 和 Ks 参考表</b>。</p>"""),
("光伏组件", f"""<p>选择型号：DualSun FLASH（法国制造商）、晶科 Tiger Neo，或练习中的通用组件。效率 η<sub>ph</sub> = 0.75 考虑了各项损耗（积灰、温度、控制器、蓄电池、逆变器）。</p>
<p>峰值功率：<b>{PC}</b>。软件给出建议的系统电压（500 Wp 以下 12 V，2000 Wp 以下 24 V，以上 48 V）以及组件的串联和并联数量。离网系统中，方阵开路电压乘以 1.2（严寒）必须低于 120 V（UTE C 15-712-2）。</p>"""),
("蓄电池", f"""<p>选择电池技术（铅酸 AGM / GEL / OPzV 或磷酸铁锂 LiFePO₄）、电池型号、自给天数 J 和放电深度 D（铅酸 0.7，锂电 0.8）。</p>
<p>容量：<b>{CB}</b>。软件给出电池数量、串并联方式、实际自给天数以及电池组短路电流，用于校核保护电器的分断能力。</p>"""),
("控制器与逆变器", """<p>选择品牌：<b>Victron</b>（SmartSolar MPPT、Phoenix）或 <b>Studer</b>（VarioTrack、Xtender），最高 5 kVA，或通用型号（仅额定值）。</p>
<p>软件根据制造商数据手册选择满足要求的最小型号：充电电流、严寒时的最大光伏电压、蓄电池电压下的光伏功率；逆变器则依据需用功率和蓄电池电压。一台控制器不够时，会并联多台，每台连接各自的组串。</p>"""),
("电缆", f"""<p>输入每段线路的单程长度（组件 → 控制器、控制器 → 蓄电池、蓄电池 → 逆变器）以及允许的电压降。</p>
<p>截面：<b>{SC}</b>，铜的 ρ = 0.023 Ω·mm²/m，向上取标准截面。还需核对电缆的载流量。</p>"""),
("保护电器", """<p>设置：保护电器品牌（Legrand 或施耐德）、直流断路器品牌、I<sub>RM</sub>（组件最大串联熔断器额定值，见组件数据手册）、雷击密度 Ng、建筑类型、是否有避雷针，以及蓄电池负极的连接方式。</p>
<p>对于每种保护——组串熔断器式隔离开关（必须）、隔离开关、蓄电池保护、直流和交流浪涌保护器、30 mA A 型剩余电流保护、接地——软件给出选型规则、计算过程和制造商型号。提示信息会指出超出产品范围的情况。</p>"""),
("保护电器接线图", """<p>单线图自动绘制。熔断器式隔离开关：熔断器画在刀片上。断路器：接线端画叉，机械联动用虚线，受保护极上依次画热脱扣器（开口方框）和磁脱扣器（半圆）。直流的负极和交流的中性线始终断开但不保护，画在左侧。</p>
<p>黄绿保护导体将所有外露导电部分（包括组件边框）连接到接地排和接地极。选项<b>蓄电池负极接地</b>（Victron，<i>Wiring Unlimited</i> § 7.7）：只设一处连接，尽量靠近蓄电池。选项<b>浮地</b>：两极都设保护，并配绝缘监测器。</p>"""),
("技术资料", """<p>完整目录：组件、控制器、逆变器、蓄电池和保护电器，附技术参数和指向制造商数据手册的链接 ↗。</p>
<p>点击某一行即选用该设备：它会高亮显示并用于计算。灰色行表示不适合当前计算的系统。<i>Back to automatic choice</i> 按钮可取消选择。</p>"""),
("汇总、打印和文件", """<p>汇总页包括关键数据、系统框图、材料清单、接线图和详细计算过程。</p>
<p><b>Print / PDF</b> 打印汇总页；在打印机中选择“另存为 PDF”即可得到 PDF 文件。<b>Save</b> 生成 <code>.solarduo</code> 文件，可用 <b>Open</b> 重新载入；安装版中双击该文件也能打开。</p>"""),
("并网系统", """<p>在 Project &amp; site 中选择 <i>Grid-connected</i>。蓄电池、控制器与逆变器、保护电器这几个选项卡将被隐藏。</p>
<p>峰值功率根据年耗电量、需覆盖的比例（自发自用通常为 20% 至 50%）、辐照量、性能比 PR（0.75 至 0.85）以及朝向 / 倾角系数（最佳：正南，30°）计算。并网逆变器的额定功率取峰值功率的 0.8 至 1 倍。</p>"""),
("参考资料与局限", f"""<p>{REFS}；DualSun、晶科能源、Victron Energy、Studer Innotec、Legrand、施耐德电气、ABB 的数据手册。</p>
<p>Solar Duo 是用于教学的设计辅助工具。施工前请核对最新的数据手册和现行规范，并由合格的专业人员审核系统。报告错误：<a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> 或 <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>。</p>"""),
])

N["ru"] = dict(title="Руководство пользователя", sub="Расчёт фотоэлектрических установок — версия 1.0", toc="Содержание",
 site="Сайт Solar Duo", app="Онлайн-версия", dl="Скачать", print="Печать",
 note="Интерфейс программы доступен на французском, английском и испанском; на снимках — английская версия.", s=[
("Общие сведения", """<p>Solar Duo рассчитывает фотоэлектрическую установку по методике курса: энергобаланс, пиковая мощность, панели, аккумуляторы, контроллер заряда, инвертор, кабели и защита.</p>
<p>Два типа установок: <b>автономная</b> (с аккумуляторами) и <b>сетевая</b> (собственное потребление, без аккумуляторов). Каждый результат показывает формулу с подставленными значениями, чтобы расчёт можно было проверить. Интерфейс на французском, английском и испанском: кнопки FR / EN / ES вверху справа.</p>"""),
("Установка и обновление", f"""<ul><li><b>Windows</b>: {F_WIN} (установщик) или {F_ZIP} (портативная версия без установки). Если Windows показывает «Система Windows защитила ваш компьютер», нажмите <i>Подробнее</i> › <i>Выполнить в любом случае</i>.</li>
<li><b>macOS</b>: {F_MAC}. Распакуйте и перетащите Solar Duo в «Программы». При первом запуске: правый щелчок › <i>Открыть</i> (приложение не подписано Apple); иначе в Терминале: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (двойной щелчок или <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (сделать исполняемым и запустить) или архив <code>.tar.gz</code>.</li>
<li><b>Онлайн</b>, без установки: {URL}.</li></ul>
<p>При запуске программа проверяет наличие новой версии и сообщает о ней полосой в верхней части окна. Меню <i>Help › Check for updates</i>.</p>"""),
("Окно и проект", """<p>Вверху: <b>New</b> (новый), <b>Open</b> (открыть), <b>Save</b> (сохранить), <b>Print / PDF</b> и язык. Пронумерованные вкладки следуют порядку расчёта; кнопки <i>Previous</i> / <i>Next</i> внизу каждой вкладки переходят от шага к шагу.</p>
<p>На вкладке <b>Project &amp; site</b>: название проекта, автор, тип установки, место и период использования (весь год — худший месяц, — с апреля по сентябрь или среднегодовое значение). Значения инсоляции ориентировочные: для реального проекта проверьте их в PVGIS и введите свои. Список <b>Worked examples</b> загружает один из трёх решённых примеров.</p>"""),
("Энергобаланс", """<p>Добавьте приборы (из списка типовых или новой строкой): мощность, мощность в режиме ожидания, количество, часы работы в день (D) или в неделю (W, делится на 7), Ku, Ks и род тока (AC или DC). Режим ожидания учитывается на оставшуюся часть суток.</p>
<p>Программа рассчитывает энергию каждого прибора и суточную энергию E<sub>ch</sub>. Ku (коэффициент использования) и Ks (коэффициент одновременности) дают расчётную мощность, по которой выбираются инвертор, кабели и защита. <b>Таблицы Ku и Ks</b> открываются вверху вкладки.</p>"""),
("Панели", f"""<p>Выберите модель: DualSun FLASH (французский производитель), Jinko Tiger Neo или типовые модули из задач. КПД η<sub>ph</sub> = 0,75 учитывает потери (загрязнение, температура, контроллер, аккумулятор, инвертор).</p>
<p>Пиковая мощность: <b>{PC}</b>. Программа предлагает напряжение системы (12 В до 500 Вт, 24 В до 2000 Вт, выше — 48 В) и число модулей последовательно и параллельно. В автономной системе напряжение холостого хода массива, умноженное на 1,2 (сильный мороз), должно оставаться ниже 120 В (UTE C 15-712-2).</p>"""),
("Аккумуляторы", f"""<p>Выберите технологию (свинцовые AGM / GEL / OPzV или литий-железо-фосфатные LiFePO₄), аккумулятор, число дней автономности J и глубину разряда D (0,7 для свинцовых, 0,8 для литиевых).</p>
<p>Ёмкость: <b>{CB}</b>. Программа указывает число аккумуляторов, их последовательно-параллельное соединение, фактическую автономность и ток короткого замыкания батареи, по которому проверяется отключающая способность защиты.</p>"""),
("Контроллер и инвертор", """<p>Выберите марку: <b>Victron</b> (SmartSolar MPPT, Phoenix) или <b>Studer</b> (VarioTrack, Xtender), до 5 кВА, либо типовую модель (только номинал).</p>
<p>Программа выбирает наименьшую подходящую модель по паспортам производителей: ток заряда, максимальное напряжение ФЭ в сильный мороз, мощность ФЭ при напряжении аккумулятора; для инвертора — расчётную мощность и напряжение аккумулятора. Если одного контроллера недостаточно, ставится несколько параллельно, каждый со своей группой цепочек.</p>"""),
("Кабели", f"""<p>Укажите длину каждой линии в одну сторону (панели → контроллер, контроллер → аккумуляторы, аккумуляторы → инвертор) и допустимое падение напряжения.</p>
<p>Сечение: <b>{SC}</b>, ρ = 0,023 Ом·мм²/м (медь), округляется до ближайшего большего стандартного сечения. Проверьте также допустимый ток кабеля.</p>"""),
("Защита", """<p>Настройки: марка аппаратов защиты (Legrand или Schneider), марка автоматов постоянного тока, I<sub>RM</sub> (максимальный последовательный предохранитель, в паспорте модуля), плотность ударов молнии Ng, тип здания, молниеотвод и подключение минуса аккумулятора.</p>
<p>Для каждого аппарата — предохранители-разъединители цепочек (обязательны), выключатель-разъединитель, защита аккумулятора, УЗИП постоянного и переменного тока, УЗО 30 мА типа A, заземление — программа показывает правило выбора, расчёт и артикул производителя. Сообщения указывают на случаи вне ассортимента.</p>"""),
("Схема защиты", """<p>Однолинейная схема строится автоматически. Предохранители-разъединители: предохранитель на ноже. Автоматические выключатели: крестик на выводе, пунктирная механическая связь, тепловой расцепитель (открытый квадрат) и затем электромагнитный (дуга) на защищаемом полюсе. Минус постоянного тока и нейтраль переменного тока всегда отключаются, но не защищаются; они расположены слева.</p>
<p>Жёлто-зелёный проводник соединяет все открытые проводящие части, включая рамы панелей, с шиной и заземлителем. Вариант <b>минус аккумулятора на землю</b> (Victron, <i>Wiring Unlimited</i> § 7.7): одно соединение как можно ближе к аккумулятору. Вариант <b>изолированный</b>: защита обоих полюсов и контроль изоляции.</p>"""),
("Техническая документация", """<p>Весь каталог: модули, контроллеры, инверторы, аккумуляторы и аппараты защиты, с характеристиками и ссылкой ↗ на паспорт производителя.</p>
<p>Щелчок по строке выбирает это оборудование: оно подсвечивается и используется в расчётах. Серые строки не подходят для рассчитанной установки. Кнопка <i>Back to automatic choice</i> отменяет выбор.</p>"""),
("Сводка, печать и файлы", """<p>Сводка содержит основные показатели, структурную схему, спецификацию, схему защиты и подробный расчёт.</p>
<p><b>Print / PDF</b> печатает сводку; чтобы получить PDF, выберите принтер «Сохранить как PDF». <b>Save</b> создаёт файл <code>.solarduo</code>, который <b>Open</b> загружает снова; в установленном приложении файл открывается и двойным щелчком.</p>"""),
("Сетевая установка", """<p>Выберите <i>Grid-connected</i> на вкладке Project &amp; site. Вкладки аккумуляторов, контроллера и инвертора, а также защиты скрываются.</p>
<p>Пиковая мощность рассчитывается по годовому потреблению, покрываемой доле (при собственном потреблении обычно 20–50 %), инсоляции, коэффициенту производительности PR (0,75–0,85) и коэффициенту ориентации / наклона (оптимум: юг, 30°). Сетевой инвертор выбирается в пределах 0,8–1 от пиковой мощности.</p>"""),
("Источники и ограничения", f"""<p>{REFS} ; паспорта DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo — вспомогательное средство расчёта для обучения. Перед монтажом проверьте актуальные паспорта и действующие нормы и согласуйте установку с квалифицированным специалистом. Сообщить об ошибке: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> или <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["uk"] = dict(title="Посібник користувача", sub="Розрахунок фотоелектричних установок — версія 1.0", toc="Зміст",
 site="Сайт Solar Duo", app="Онлайн-версія", dl="Завантажити", print="Друк",
 note="Інтерфейс програми доступний французькою, англійською та іспанською; на знімках — англійська версія.", s=[
("Загальні відомості", """<p>Solar Duo розраховує фотоелектричну установку за методикою курсу: енергобаланс, пікова потужність, панелі, акумулятори, контролер заряду, інвертор, кабелі та захист.</p>
<p>Два типи установок: <b>автономна</b> (з акумуляторами) і <b>мережева</b> (власне споживання, без акумуляторів). Кожен результат показує формулу з підставленими значеннями, щоб розрахунок можна було перевірити. Інтерфейс французькою, англійською та іспанською: кнопки FR / EN / ES угорі праворуч.</p>"""),
("Встановлення та оновлення", f"""<ul><li><b>Windows</b>: {F_WIN} (інсталятор) або {F_ZIP} (портативна версія без встановлення). Якщо Windows показує «Windows захистила ваш ПК», натисніть <i>Докладніше</i> › <i>Однаково запустити</i>.</li>
<li><b>macOS</b>: {F_MAC}. Розпакуйте й перетягніть Solar Duo до «Програм». Під час першого запуску: правий клік › <i>Відкрити</i> (застосунок не підписаний Apple); інакше в Терміналі: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (подвійне клацання або <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (зробити виконуваним і запустити) або архів <code>.tar.gz</code>.</li>
<li><b>Онлайн</b>, без встановлення: {URL}.</li></ul>
<p>Під час запуску програма перевіряє, чи є нова версія, і повідомляє про неї смугою у верхній частині вікна. Меню <i>Help › Check for updates</i>.</p>"""),
("Вікно та проєкт", """<p>Угорі: <b>New</b> (новий), <b>Open</b> (відкрити), <b>Save</b> (зберегти), <b>Print / PDF</b> і мова. Пронумеровані вкладки йдуть за порядком розрахунку; кнопки <i>Previous</i> / <i>Next</i> унизу кожної вкладки переходять від кроку до кроку.</p>
<p>На вкладці <b>Project &amp; site</b>: назва проєкту, автор, тип установки, місце та період використання (увесь рік — найгірший місяць —, з квітня до вересня або середньорічне значення). Значення інсоляції орієнтовні: для реального проєкту перевірте їх у PVGIS і введіть власні. Список <b>Worked examples</b> завантажує один із трьох розв'язаних прикладів.</p>"""),
("Енергобаланс", """<p>Додайте прилади (зі списку типових або новим рядком): потужність, потужність у режимі очікування, кількість, години роботи на день (D) або на тиждень (W, ділиться на 7), Ku, Ks і рід струму (AC або DC). Режим очікування враховується на решту доби.</p>
<p>Програма розраховує енергію кожного приладу та добову енергію E<sub>ch</sub>. Ku (коефіцієнт використання) і Ks (коефіцієнт одночасності) дають розрахункову потужність, за якою вибирають інвертор, кабелі та захист. <b>Таблиці Ku і Ks</b> відкриваються вгорі вкладки.</p>"""),
("Панелі", f"""<p>Виберіть модель: DualSun FLASH (французький виробник), Jinko Tiger Neo або типові модулі із задач. ККД η<sub>ph</sub> = 0,75 враховує втрати (забруднення, температура, контролер, акумулятор, інвертор).</p>
<p>Пікова потужність: <b>{PC}</b>. Програма пропонує напругу системи (12 В до 500 Вт, 24 В до 2000 Вт, вище — 48 В) і кількість модулів послідовно та паралельно. В автономній системі напруга холостого ходу масиву, помножена на 1,2 (сильний мороз), має бути нижчою за 120 В (UTE C 15-712-2).</p>"""),
("Акумулятори", f"""<p>Виберіть технологію (свинцеві AGM / GEL / OPzV або літій-залізо-фосфатні LiFePO₄), акумулятор, кількість днів автономності J і глибину розряду D (0,7 для свинцевих, 0,8 для літієвих).</p>
<p>Ємність: <b>{CB}</b>. Програма вказує кількість акумуляторів, їх послідовно-паралельне з'єднання, фактичну автономність і струм короткого замикання батареї, за яким перевіряють комутаційну здатність захисту.</p>"""),
("Контролер та інвертор", """<p>Виберіть марку: <b>Victron</b> (SmartSolar MPPT, Phoenix) або <b>Studer</b> (VarioTrack, Xtender), до 5 кВА, чи типову модель (лише номінал).</p>
<p>Програма вибирає найменшу відповідну модель за паспортами виробників: струм заряду, максимальна напруга ФЕ в сильний мороз, потужність ФЕ за напруги акумулятора; для інвертора — розрахункову потужність і напругу акумулятора. Якщо одного контролера недостатньо, ставиться кілька паралельно, кожен зі своєю групою ланцюжків.</p>"""),
("Кабелі", f"""<p>Вкажіть довжину кожної лінії в один бік (панелі → контролер, контролер → акумулятори, акумулятори → інвертор) і допустимий спад напруги.</p>
<p>Переріз: <b>{SC}</b>, ρ = 0,023 Ом·мм²/м (мідь), округлюється до найближчого більшого стандартного перерізу. Перевірте також допустимий струм кабелю.</p>"""),
("Захист", """<p>Налаштування: марка апаратів захисту (Legrand або Schneider), марка автоматів постійного струму, I<sub>RM</sub> (максимальний послідовний запобіжник, у паспорті модуля), щільність ударів блискавки Ng, тип будівлі, блискавковідвід і під'єднання мінуса акумулятора.</p>
<p>Для кожного апарата — запобіжники-роз'єднувачі ланцюжків (обов'язкові), вимикач-роз'єднувач, захист акумулятора, ПЗІП постійного та змінного струму, ПЗВ 30 мА типу A, заземлення — програма показує правило вибору, розрахунок і артикул виробника. Повідомлення вказують на випадки поза асортиментом.</p>"""),
("Схема захисту", """<p>Однолінійна схема будується автоматично. Запобіжники-роз'єднувачі: запобіжник на ножі. Автоматичні вимикачі: хрестик на виводі, пунктирний механічний зв'язок, тепловий розчіплювач (відкритий квадрат), а потім електромагнітний (дуга) на захищеному полюсі. Мінус постійного струму та нейтраль змінного струму завжди вимикаються, але не захищаються; вони розташовані ліворуч.</p>
<p>Жовто-зелений провідник з'єднує всі відкриті провідні частини, разом із рамами панелей, із шиною та заземлювачем. Варіант <b>мінус акумулятора на землю</b> (Victron, <i>Wiring Unlimited</i> § 7.7): одне з'єднання якомога ближче до акумулятора. Варіант <b>ізольований</b>: захист обох полюсів і контроль ізоляції.</p>"""),
("Технічна документація", """<p>Увесь каталог: модулі, контролери, інвертори, акумулятори та апарати захисту, з характеристиками й посиланням ↗ на паспорт виробника.</p>
<p>Клацання по рядку вибирає це обладнання: воно підсвічується й використовується в розрахунках. Сірі рядки не підходять для розрахованої установки. Кнопка <i>Back to automatic choice</i> скасовує вибір.</p>"""),
("Підсумок, друк і файли", """<p>Підсумок містить основні показники, структурну схему, специфікацію, схему захисту та докладний розрахунок.</p>
<p><b>Print / PDF</b> друкує підсумок; щоб отримати PDF, виберіть принтер «Зберегти як PDF». <b>Save</b> створює файл <code>.solarduo</code>, який <b>Open</b> завантажує знову; у встановленому застосунку файл відкривається й подвійним клацанням.</p>"""),
("Мережева установка", """<p>Виберіть <i>Grid-connected</i> на вкладці Project &amp; site. Вкладки акумуляторів, контролера та інвертора, а також захисту приховуються.</p>
<p>Пікову потужність розраховують за річним споживанням, часткою, яку треба покрити (при власному споживанні зазвичай 20–50 %), інсоляцією, коефіцієнтом продуктивності PR (0,75–0,85) і коефіцієнтом орієнтації / нахилу (оптимум: південь, 30°). Мережевий інвертор вибирають у межах 0,8–1 від пікової потужності.</p>"""),
("Джерела та обмеження", f"""<p>{REFS} ; паспорти DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo — допоміжний засіб розрахунку для навчання. Перед монтажем перевірте актуальні паспорти та чинні норми й погодьте установку з кваліфікованим фахівцем. Повідомити про помилку: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> або <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["ar"] = dict(title="دليل الاستخدام", sub="حساب أبعاد المنظومات الكهروضوئية — الإصدار 1.0", toc="المحتويات",
 site="موقع Solar Duo", app="النسخة عبر الإنترنت", dl="تنزيل", print="طباعة",
 note="واجهة البرنامج متوفرة بالفرنسية والإنجليزية والإسبانية؛ والصور تعرض النسخة الإنجليزية.", s=[
("تقديم", """<p>يحسب Solar Duo أبعاد منظومة كهروضوئية وفق منهجية الدرس: الحصيلة الطاقية، القدرة القصوى، الألواح، البطاريات، منظم الشحن، العاكس، الكابلات والحمايات.</p>
<p>نوعان من المنظومات: <b>معزولة</b> (مستقلة، ببطاريات) و<b>متصلة بالشبكة</b> (استهلاك ذاتي، بلا بطارية). تعرض كل نتيجة معادلتها مع القيم، ليمكن التحقق من الحساب. الواجهة بالفرنسية والإنجليزية والإسبانية: أزرار FR / EN / ES أعلى اليمين.</p>"""),
("التثبيت والتحديث", f"""<ul><li><b>Windows</b>: {F_WIN} (برنامج تثبيت) أو {F_ZIP} (نسخة محمولة بلا تثبيت). إذا ظهرت رسالة «قام Windows بحماية الكمبيوتر»، انقر <i>مزيد من المعلومات</i> › <i>التشغيل على أي حال</i>.</li>
<li><b>macOS</b>: {F_MAC}. فك الضغط واسحب Solar Duo إلى التطبيقات. في المرة الأولى: نقر يمين › <i>فتح</i> (التطبيق غير موقَّع من Apple)؛ أو في الطرفية: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (نقرة مزدوجة، أو <code>sudo apt install ./solar-duo_amd64.deb</code>)، {F_APP} (اجعله قابلاً للتنفيذ ثم شغّله) أو الأرشيف <code>.tar.gz</code>.</li>
<li><b>عبر الإنترنت</b>، بلا تثبيت: {URL}.</li></ul>
<p>عند التشغيل يتحقق البرنامج من وجود إصدار جديد ويعلن عنه بشريط أعلى النافذة. القائمة <i>Help › Check for updates</i>.</p>"""),
("النافذة والمشروع", """<p>في الأعلى: <b>New</b> (جديد)، <b>Open</b> (فتح)، <b>Save</b> (حفظ)، <b>Print / PDF</b> واللغة. تتبع علامات التبويب المرقّمة خطوات الحساب؛ وينقل الزران <i>Previous</i> / <i>Next</i> أسفل كل علامة من خطوة إلى أخرى.</p>
<p>في <b>Project &amp; site</b>: اسم المشروع، المؤلف، نوع المنظومة، المكان وفترة الاستخدام (طوال السنة — أسوأ شهر —، من أبريل إلى سبتمبر، أو المتوسط السنوي). قيم الإشعاع الشمسي تقريبية: لمشروع حقيقي تحقق منها على PVGIS وأدخل قيمك. تحمّل القائمة <b>Worked examples</b> أحد الأمثلة الثلاثة المحلولة.</p>"""),
("الحصيلة الطاقية", """<p>أضف الأجهزة (من قائمة الأجهزة النموذجية أو سطراً جديداً): القدرة، قدرة الاستعداد، العدد، ساعات التشغيل في اليوم (D) أو في الأسبوع (W، تُقسم على 7)، Ku وKs ونوع التيار (AC أو DC). يُحتسب الاستعداد على بقية اليوم.</p>
<p>يحسب البرنامج طاقة كل جهاز والطاقة اليومية E<sub>ch</sub>. ويعطي Ku (معامل الاستعمال) وKs (معامل التزامن) القدرة المطلوبة، التي يُختار على أساسها العاكس والكابلات والحمايات. تُفتح <b>جداول Ku وKs</b> المرجعية أعلى علامة التبويب.</p>"""),
("الألواح", f"""<p>اختر الطراز: DualSun FLASH (صانع فرنسي)، Jinko Tiger Neo، أو الوحدات العامة في التمارين. المردود η<sub>ph</sub> = 0,75 يأخذ الضياعات في الحسبان (الاتساخ، الحرارة، المنظم، البطارية، العاكس).</p>
<p>القدرة القصوى: <b>{PC}</b>. يقترح البرنامج جهد المنظومة (12 فولت حتى 500 واط ذروة، 24 فولت حتى 2000 واط ذروة، و48 فولت فوق ذلك) وعدد الوحدات على التوالي والتوازي. في المنظومة المعزولة، يجب أن يبقى جهد الدارة المفتوحة للحقل مضروباً في 1,2 (البرد الشديد) أقل من 120 فولت (UTE C 15-712-2).</p>"""),
("البطاريات", f"""<p>اختر التقنية (رصاص AGM / GEL / OPzV أو ليثيوم فوسفات الحديد LiFePO₄)، البطارية، أيام الاستقلالية J وعمق التفريغ D (0,7 للرصاص و0,8 لليثيوم).</p>
<p>السعة: <b>{CB}</b>. يعطي البرنامج عدد البطاريات وطريقة توصيلها على التوالي / التوازي والاستقلالية الفعلية وتيار قصر الدارة للمجموعة، الذي يُستعمل للتحقق من قدرة القطع للحمايات.</p>"""),
("المنظم والعاكس", """<p>اختر العلامة: <b>Victron</b> (SmartSolar MPPT وPhoenix) أو <b>Studer</b> (VarioTrack وXtender) حتى 5 كيلوفولت أمبير، أو طرازاً عاماً (العيار فقط).</p>
<p>يختار البرنامج أصغر طراز مناسب وفق نشرات الصانعين: تيار الشحن، أقصى جهد كهروضوئي في البرد الشديد، القدرة الكهروضوئية عند جهد البطارية؛ وللعاكس: القدرة المطلوبة وجهد البطارية. إذا لم يكفِ منظم واحد، يضع عدة منظمات على التوازي، لكل منها مجموعة سلاسله.</p>"""),
("الكابلات", f"""<p>أدخل طول الذهاب لكل وصلة (الألواح ← المنظم، المنظم ← البطاريات، البطاريات ← العاكس) وهبوط الجهد المسموح.</p>
<p>المقطع: <b>{SC}</b>، مع ρ = 0,023 أوم·مم²/م (النحاس)، مقرّباً إلى المقطع القياسي الأعلى. تحقق أيضاً من التيار المسموح للكابل.</p>"""),
("الحمايات", """<p>الإعدادات: علامة الحمايات (Legrand أو Schneider)، علامة قواطع التيار المستمر، I<sub>RM</sub> (أقصى مصهر على التوالي، في نشرة الوحدة)، كثافة الصواعق Ng، نوع المبنى، مانعة الصواعق وتوصيل سالب البطارية.</p>
<p>لكل حماية — قواطع المصهرات للسلاسل (إلزامية)، قاطع العزل، حماية البطارية، مانعات الصواعق للتيار المستمر والمتناوب، قاطع تفاضلي 30 مللي أمبير من النوع A، التأريض — يعرض البرنامج قاعدة الاختيار والحساب ومرجع الصانع. وتنبّه الرسائل إلى الحالات الخارجة عن نطاق المنتجات.</p>"""),
("مخطط الحمايات", """<p>يُرسم المخطط الأحادي الخط تلقائياً. قواطع المصهرات: المصهر على السكين. القواطع الآلية: علامة × على الطرف، ربط ميكانيكي متقطع، مُطلِق حراري (مربع مفتوح) ثم مغناطيسي (قوس) على القطب المحمي. السالب في التيار المستمر والمحايد في المتناوب يُقطعان دائماً دون حماية، ويوضعان على اليسار.</p>
<p>يربط الموصل الأخضر/الأصفر جميع الأجزاء المعدنية، بما فيها إطارات الألواح، بقضيب التجميع وقطب التأريض. خيار <b>سالب البطارية إلى الأرض</b> (Victron، <i>Wiring Unlimited</i> § 7.7): وصلة واحدة، أقرب ما يمكن إلى البطارية. خيار <b>معزول</b>: حمايات على القطبين ومراقب للعزل.</p>"""),
("الوثائق التقنية", """<p>الكتالوج كاملاً: الوحدات والمنظمات والعواكس والبطاريات والحمايات، مع خصائصها ورابط ↗ إلى نشرة الصانع.</p>
<p>انقر على سطر لاختيار ذلك العتاد: يُبرَز ويُستعمل في الحسابات. الأسطر الرمادية لا تناسب المنظومة المحسوبة. يلغي الزر <i>Back to automatic choice</i> الاختيار.</p>"""),
("الخلاصة والطباعة والملفات", """<p>تجمع الخلاصة الأرقام الرئيسية والمخطط الإجمالي وقائمة العتاد والمخطط وتفاصيل الحسابات.</p>
<p>يطبع <b>Print / PDF</b> الخلاصة؛ اختر «حفظ بتنسيق PDF» كطابعة للحصول على ملف PDF. ينشئ <b>Save</b> ملفاً <code>.solarduo</code> يعيد <b>Open</b> تحميله؛ ومع التطبيق المثبَّت، تفتحه أيضاً نقرة مزدوجة على الملف.</p>"""),
("منظومة متصلة بالشبكة", """<p>اختر <i>Grid-connected</i> في Project &amp; site. تُخفى علامات تبويب البطاريات والمنظم والعاكس والحمايات.</p>
<p>تُحسب القدرة القصوى من الاستهلاك السنوي، والحصة المراد تغطيتها (غالباً 20 إلى 50 % في الاستهلاك الذاتي)، والإشعاع، ونسبة الأداء PR ‏(0,75 إلى 0,85)، ومعامل الاتجاه / الميل (الأمثل: الجنوب، 30°). يُختار عاكس الشبكة بين 0,8 و1 من القدرة القصوى.</p>"""),
("المراجع والحدود", f"""<p dir="ltr" style="text-align:right">{REFS} ; DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB</p>
<p>Solar Duo أداة مساعدة في حساب الأبعاد لأغراض التكوين. قبل أي تنفيذ، تحقق من النشرات التقنية المحدّثة ومن اللوائح السارية، واعرض المنظومة على مهني مؤهل. للإبلاغ عن خطأ: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> أو <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

N["sq"] = dict(title="Udhëzuesi i përdorimit", sub="Përmasimi i impianteve fotovoltaike — versioni 1.0", toc="Përmbajtja",
 site="Faqja e Solar Duo", app="Versioni në internet", dl="Shkarko", print="Shtyp",
 note="Ndërfaqja e programit është në frëngjisht, anglisht dhe spanjisht; pamjet tregojnë versionin anglisht.", s=[
("Prezantimi", """<p>Solar Duo përmason një impiant fotovoltaik sipas metodës së mësimit: bilanci energjetik, fuqia maksimale, panelet, bateritë, rregullatori i karikimit, invertori, kabllot dhe mbrojtjet.</p>
<p>Dy lloje impiantesh: <b>i izoluar</b> (autonom, me bateri) dhe <b>i lidhur me rrjetin</b> (vetëkonsum, pa bateri). Çdo rezultat tregon formulën me vlerat, që llogaritja të mund të kontrollohet. Ndërfaqja është në frëngjisht, anglisht dhe spanjisht: butonat FR / EN / ES lart djathtas.</p>"""),
("Instalimi dhe përditësimi", f"""<ul><li><b>Windows</b>: {F_WIN} (instalues) ose {F_ZIP} (portativ, pa instalim). Nëse Windows shfaq «Windows e mbrojti PC-në tënde», kliko <i>Më shumë informacion</i> › <i>Ekzekuto gjithsesi</i>.</li>
<li><b>macOS</b>: {F_MAC}. Shpaketo dhe tërhiq Solar Duo te Applications. Herën e parë: klik i djathtë › <i>Open</i> (aplikacioni nuk është i nënshkruar nga Apple); përndryshe, në Terminal: {XATTR}.</li>
<li><b>Linux</b>: {F_DEB} (klik i dyfishtë, ose <code>sudo apt install ./solar-duo_amd64.deb</code>), {F_APP} (bëje të ekzekutueshëm dhe nise) ose arkivi <code>.tar.gz</code>.</li>
<li><b>Në internet</b>, pa instaluar asgjë: {URL}.</li></ul>
<p>Në nisje, programi kontrollon nëse ka version të ri dhe e njofton me një shirit në krye të dritares. Menyja <i>Help › Check for updates</i>.</p>"""),
("Dritarja dhe projekti", """<p>Lart: <b>New</b> (i ri), <b>Open</b> (hap), <b>Save</b> (ruaj), <b>Print / PDF</b> dhe gjuha. Skedat e numëruara ndjekin hapat e llogaritjes; butonat <i>Previous</i> / <i>Next</i> poshtë çdo skede kalojnë nga një hap te tjetri.</p>
<p>Te <b>Project &amp; site</b>: emri i projektit, autori, lloji i impiantit, vendi dhe periudha e përdorimit (gjithë vitin — muaji më i keq —, nga prilli në shtator, ose mesatarja vjetore). Vlerat e rrezatimit diellor janë orientuese: për një projekt real, kontrollojini në PVGIS dhe vendosni tuajat. Lista <b>Worked examples</b> ngarkon një nga tre shembujt e zgjidhur.</p>"""),
("Bilanci energjetik", """<p>Shtoni pajisjet (nga lista e pajisjeve tipike ose rresht i ri): fuqia, fuqia në gatishmëri, sasia, orët e përdorimit në ditë (D) ose në javë (W, pjesëtuar me 7), Ku, Ks dhe lloji i rrymës (AC ose DC). Gatishmëria llogaritet për pjesën tjetër të ditës.</p>
<p>Programi llogarit energjinë e çdo pajisjeje dhe energjinë ditore E<sub>ch</sub>. Ku (faktori i përdorimit) dhe Ks (faktori i njëkohshmërisë) japin fuqinë e kërkuar, me të cilën zgjidhen invertori, kabllot dhe mbrojtjet. <b>Tabelat Ku dhe Ks</b> hapen në krye të skedës.</p>"""),
("Panelet", f"""<p>Zgjidhni modelin: DualSun FLASH (prodhues francez), Jinko Tiger Neo ose modulet e përgjithshme të ushtrimeve. Rendimenti η<sub>ph</sub> = 0,75 merr parasysh humbjet (ndotja, temperatura, rregullatori, bateria, invertori).</p>
<p>Fuqia maksimale: <b>{PC}</b>. Programi propozon tensionin e sistemit (12 V deri në 500 Wp, 24 V deri në 2000 Wp, mbi këtë 48 V) dhe numrin e moduleve në seri dhe në paralel. Në impiant të izoluar, tensioni pa ngarkesë i fushës shumëzuar me 1,2 (të ftohtë i madh) duhet të mbetet nën 120 V (UTE C 15-712-2).</p>"""),
("Bateritë", f"""<p>Zgjidhni teknologjinë (plumb AGM / GEL / OPzV ose litium LiFePO₄), baterinë, ditët e autonomisë J dhe thellësinë e shkarkimit D (0,7 për plumbin, 0,8 për litiumin).</p>
<p>Kapaciteti: <b>{CB}</b>. Programi jep numrin e baterive, lidhjen seri / paralel, autonominë reale dhe rrymën e lidhjes së shkurtër të grupit, me të cilën kontrollohet aftësia ndërprerëse e mbrojtjeve.</p>"""),
("Rregullatori dhe invertori", """<p>Zgjidhni markën: <b>Victron</b> (SmartSolar MPPT, Phoenix) ose <b>Studer</b> (VarioTrack, Xtender), deri në 5 kVA, ose një model të përgjithshëm (vetëm vlera nominale).</p>
<p>Programi zgjedh modelin më të vogël të përshtatshëm sipas fletëve të prodhuesve: rryma e karikimit, tensioni maksimal FV në të ftohtë të madh, fuqia FV në tensionin e baterisë; për invertorin, fuqia e kërkuar dhe tensioni i baterisë. Nëse një rregullator nuk mjafton, vendos disa në paralel, secili me grupin e vet të vargjeve.</p>"""),
("Kabllot", f"""<p>Vendosni gjatësinë e vajtjes të çdo lidhjeje (panelet → rregullatori, rregullatori → bateritë, bateritë → invertori) dhe rënien e lejuar të tensionit.</p>
<p>Seksioni: <b>{SC}</b>, me ρ = 0,023 Ω·mm²/m (bakër), i rrumbullakuar në seksionin standard më të madh. Kontrolloni edhe rrymën e lejuar të kabllos.</p>"""),
("Mbrojtjet", """<p>Cilësimet: marka e mbrojtjeve (Legrand ose Schneider), marka e ndërprerësve të rrymës së vazhduar, I<sub>RM</sub> (siguresa maksimale në seri, në fletën e modulit), dendësia e rrufeve Ng, lloji i ndërtesës, rrufepritësi dhe lidhja e − së baterisë.</p>
<p>Për çdo mbrojtje — mbajtëset e siguresave të vargjeve (të detyrueshme), ndërprerësi-seksionues, mbrojtja e baterisë, mbrojtësit e mbitensionit DC dhe AC, diferenciali 30 mA tipi A, tokëzimi — programi tregon rregullin e zgjedhjes, llogaritjen dhe kodin e prodhuesit. Mesazhet sinjalizojnë rastet jashtë gamës.</p>"""),
("Skema e mbrojtjeve", """<p>Skema njëvijëshe vizatohet automatikisht. Mbajtëset e siguresave: siguresa mbi thikë. Ndërprerësit automatikë: kryq te kapësja, lidhje mekanike me vija të ndërprera, lëshuesi termik (katror i hapur) dhe pastaj magnetik (hark) në polin e mbrojtur. − në rrymë të vazhduar dhe neutri në rrymë alternative ndërpriten gjithmonë, por nuk mbrohen; ndodhen majtas.</p>
<p>Përçuesi i verdhë-jeshil lidh të gjitha masat, përfshirë kornizat e paneleve, me shiritin dhe elektrodën e tokëzimit. Opsioni <b>− i baterisë në tokë</b> (Victron, <i>Wiring Unlimited</i> § 7.7): një lidhje e vetme, sa më afër baterisë. Opsioni <b>lundrues</b>: mbrojtje në të dy polaritetet dhe kontrollues izolimi.</p>"""),
("Dokumentacioni teknik", """<p>I gjithë katalogu: module, rregullatorë, invertorë, bateri dhe mbrojtje, me karakteristikat dhe lidhjen ↗ te fleta e prodhuesit.</p>
<p>Klikoni mbi një rresht për të zgjedhur atë pajisje: ajo theksohet dhe përdoret në llogaritje. Rreshtat gri nuk i përshtaten impiantit të llogaritur. Butoni <i>Back to automatic choice</i> anulon zgjedhjen.</p>"""),
("Përmbledhja, shtypja dhe skedarët", """<p>Përmbledhja mbledh shifrat kryesore, skemën e përgjithshme, listën e materialeve, skemën e mbrojtjeve dhe detajet e llogaritjeve.</p>
<p><b>Print / PDF</b> shtyp përmbledhjen; zgjidhni «Ruaj si PDF» si printer për të marrë një skedar PDF. <b>Save</b> krijon një skedar <code>.solarduo</code> që <b>Open</b> e ringarkon; me aplikacionin e instaluar, edhe një klik i dyfishtë mbi skedarin e hap.</p>"""),
("Impianti i lidhur me rrjetin", """<p>Zgjidhni <i>Grid-connected</i> te Project &amp; site. Skedat e baterive, të rregullatorit dhe invertorit dhe të mbrojtjeve fshihen.</p>
<p>Fuqia maksimale llogaritet nga konsumi vjetor, pjesa që duhet mbuluar (shpesh 20 deri në 50 % në vetëkonsum), rrezatimi, raporti i performancës PR (0,75 deri në 0,85) dhe faktori i orientimit / pjerrësisë (optimumi: jug, 30°). Invertori i rrjetit zgjidhet ndërmjet 0,8 dhe 1 herë fuqisë maksimale.</p>"""),
("Referencat dhe kufijtë", f"""<p>{REFS} ; fletët teknike DualSun, Jinko Solar, Victron Energy, Studer Innotec, Legrand, Schneider Electric, ABB.</p>
<p>Solar Duo është ndihmë për përmasimin në kuadër të formimit. Para çdo realizimi, kontrolloni fletët teknike të përditësuara dhe rregullat në fuqi, dhe kërkoni miratimin e impiantit nga një profesionist i kualifikuar. Raportoni një gabim: <a href="https://github.com/Deltapassion/Solar-Duo/issues">GitHub › Issues</a> ose <a href="mailto:deltapassion@gmx.com">deltapassion@gmx.com</a>.</p>"""),
])

if __name__ == "__main__":
    for l, d in N.items():
        assert len(d["s"]) == len(IMG), (l, len(d["s"]))
    out = Path(__file__).resolve().parent.parent / "docs" / "notice" / "notice-text.js"
    js = ("// Généré par tools/notice_i18n.py — ne pas modifier à la main\n"
          "window.NOTICE_IMG = " + json.dumps(IMG) + ";\n"
          "window.NOTICE = " + json.dumps(N, ensure_ascii=False) + ";\n")
    out.write_text(js, encoding="utf-8")
    print(out, len(js), sorted(N))
