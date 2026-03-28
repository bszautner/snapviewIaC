# SnapView – Felhőalapú Fotókezelő Rendszer
## Fejlesztői Összefoglaló

---

## 1. Projekt célkitűzése és funkcionális követelmények

A projekt során egy olyan skálázható webes alkalmazást hoztam létre, amely képes nagy mennyiségű vizuális adat (fénykép) tárolására és rendszerezésére. A fejlesztés során a modern felhasználói élményt (UX) ötvöztem a felhőalapú infrastruktúra (PaaS) biztonságával.  

**GitHub Repository:** [bszautner/snapviewIaC](https://github.com/bszautner/snapviewIaC)

### Főbb funkcionális követelmények:

- **Képek metaadatokkal:** Minden képhez kötelező nevet (max. 40 karakter) rendeltem, a feltöltési dátumot pedig automatikusan rögzítem.
- **Dinamikus listázás:** Lehetőséget biztosítottam a képek név és dátum szerinti rendezésére.
- **Biztonság:** A CRUD műveleteket (feltöltés/törlés) kizárólag hitelesített felhasználók számára tettem elérhetővé.
- **Objektumtárolás:** A képeket nem a lokális szerveren, hanem felhőalapú tárolóban helyeztem el a skálázhatóság érdekében.

### Alkalmazott technológiák

| Réteg       | Technológia                   | Indoklás                                                                 |
|-------------|-------------------------------|--------------------------------------------------------------------------|
| Backend     | Python / Django               | A gyors prototípus-készítés és a beépített biztonsági funkciók miatt választottam. |
| Frontend    | HTML5, CSS3, JS               | A modern megjelenést (Inter font) és az interaktív Drag & Drop funkciót ezzel valósítottam meg. |
| Adatbázis   | Render Database for PostgreSQL | A relációs adatok (felhasználók, metaadatok) stabil, felhőalapú tárolására ezt alkalmaztam. |
| Fájltárolás | Cloudinary           | Költséghatékony és végtelenül skálázható megoldásként integráltam.      |
| Deployment  | GitHub Actions                | Teljesen automatizált CI/CD folyamatot alakítottam ki az Render. |

---

## 2. Felhasználói felület (UI/UX) bemutatása

Az alkalmazásnál törekedtem a letisztult megjelenésre, ezért modern kék-szürke színpalettát használtam.

### 2.1 A Főoldal és a Galéria

A főoldalt (`base.html`) reszponzív grid hálózattal terveztem meg. A képek kártya alapú elrendezésben jelennek meg, ahol feltüntettem a feltöltő nevét és a dátumot is.

- **Rendezés:** A jobb felső sarokban elhelyezett gombokkal a felhasználó választhat a rendezési elvek között. Ezt a backend oldalon a QuerySet-ek `order_by()` metódusával kezeltem le.

*1. ábra: Kezdőlap - Galéria nézet*

### 2.2 Feltöltési felület (Drag & Drop)

A feltöltést (`photo_upload.html`) JavaScript segítségével tettem interaktívvá. Olyan felületet hoztam létre, ahol a felhasználók egyszerűen behúzhatják a fájlokat, amiről azonnali vizuális visszajelzést kapnak.

### 2.3 Részletes nézet és Törlés

A képre kattintva a `photo_detail.html` oldal töltődik be, ahol a kép közvetlenül az Azure Blob Storage-ból érkezik. Implementáltam egy ellenőrzést: ha a bejelentkezett felhasználó a kép tulajdonosa, megjelenik a törlés gomb, amely egy megerősítő oldalra (`photo_confirm_delete.html`) irányít a véletlen adatvesztés elkerülése érdekében.

---

## 3. Felhő-architektúra részletezése 

A teljes alkalmazást az Render felhőben üzemeltetem.

### 3.1 Render Service (PaaS)

A Python-kódom a Render PaaS környezeten fut, amely a HTTP-kérések kiszolgálásáért felel. A `settings.py`-ban használt érzékeny adatokat (adatbázis URL, kulcsok) tárolom.

### 3.2 Cloudinary (Storage)

A médiafájlok kezeléséhez az Cloudinary Storage-ot használtam. A `django-storages` könyvtár segítségével úgy konfiguráltam a rendszert, hogy a feltöltött fájlok automatikusan az Cloudinary tárolóba kerüljenek.

### 3.3 Render database for PostgreSQL

Az első fázisban még SQLite-ot használtam, de a végleges verzióban már (jelenleg is ez van már üzembe helyezve) egy dedikált PostgreSQL szervert állítottam be. Ez biztosítja az adatok perzisztenciáját és a többfelhasználós környezet stabilitását.

*2. ábra: Az alkalmazás felhő-architektúrája*

---

## 4. CI/CD: Automatizált közzététel (GitHub Actions)

Létrehoztam egy `.github/workflows/main.yml` fájlt, amely minden `develop` branch-re történő push esetén automatikusan elindítja a folyamatot:

1. **Build:** Ellenőrzöm a Python függőségeket.
2. **Deploy:** Sikeres build után a kódom automatikusan frissül az Render-en.
3. **Post-deploy:** Automatikusan lefuttatom az adatbázis-migrációkat, így a séma mindig naprakész marad.

