# Vigenère-Cipher-and-Turning-Grille-Fleissner-Grille-
Implementimi i algoritmeve të enkriptimit dhe dekriptimit Vigenère Cipher dhe Turning Grille (Fleissner Grille) në Python.

## Pershkrimi
Ky projekt implementon algoritmet kriptografike Vigenere dhe Turning Grille. Mer teksin nga useri dhe e enkripton/dekripton.

## Qëllimi
Ky eshte nje projekt universitar, qellimi i ketij projekti eshte te demonstroj se si algoritmet e ndryshme funksionojne ne praktike. 

## Struktura e Projektit
Projekti ka nje strukture te thjeshte. <br>
**Folderi algorithms** - permban algoritmet per enkriptim/dekriprim dhe kontrollin, i cili kontrollon se cili algoritem duhet te ekzekutohet.<br>
**Folderi core** - kjo pjese, permban inputet e userit, validimin e tyre, kontrollon dhe nje ui ku useri jep te dhenat.<br>


## Si Funksionon
Ne ui.py eshte thirrur funskioni start(), ky funsion gjendet ne core_control.py. Ai perdor file-at inputs.py dhe validation.py per ti mar te dhenar dhe validuar. Me ane te input.py meren te dhenat dhe validation.py validohen te dhenat.<br>
Te dhenat pas inputit dhe validimit ruhen ne disa variabla ne funksionin start(). Ky funksion pastaj thirr njerin nga funksionet ne algorithm_control.py. Keto funksione pastaj percaktojne se cilat nga funksionet e enkriptimit/dekriptimit duhet te ekzekutohen. <br>
Rezultatet e enkriptimit/dekriptimit pastaj kthehen ne funksionin start() dhe printohen per userin.


## Perdorimi
Per ekzekutimin e projekt pas hapjes se folderit, shkruajme komanden  **py -m core/ui**. Aty do te pyetesh per enc/dec (enkriptim/dekriptim), pastaj jep llojin e algoritmit V ose t (Vigenere ose Turning Grille) dhe ne fund jep te dhenat si teksti, key etj.

## 🧱 Project Structure

```text
project/
├── algorithms/                   → algoritmet e enkriptimit dhe dekriptimit
│   ├── algorithm_control.py      → koordinon thirrjen e algoritmeve
│   ├── turning_grille_encrypt.py → enkriptimi me Turning Grille
│   ├── turning_grille_decrypt.py → dekriptimi me Turning Grille
│   ├── vigenere_encrypt.py       → enkriptimi me Vigenère
│   └── vigenere_decrypt.py       → dekriptimi me Vigenère
│
├── core/                         → logjika kryesore e programit
│   ├── core_control.py           → kontrollon rrjedhën kryesore të programit
│   ├── inputs.py                 → merr input nga përdoruesi
│   ├── validation.py             → validon inputet
│   └── ui.py                     → pika hyrëse / ndërfaqja e thjeshtë në terminal
│
├── .gitignore                    → përjashton file të panevojshëm nga Git
└── README.md                     → dokumentimi i projektit
```

## Permbledhje e Moduleve


###  Moduli Core

### `core/ui.py`
**Entry point i programit**

- Nis ekzekutimin e aplikacionit
- Thërret funksionin kryesor nga `core_control.py`
- Shërben si ndërfaqe e thjeshtë në terminal (CLI)


### `core/core_control.py`
**Kontrolluesi kryesor (truri i aplikacionit)**

- Menaxhon rrjedhën e plotë të programit
- Thërret funksionet nga `inputs.py` për input
- Validon inputet përmes `validation.py`
- Vendos:
  - encrypt / decrypt
  - cili algoritëm do përdoret
- Thërret algoritmet përkatëse nga `algorithms/`
- Kthen dhe shfaq rezultatin final


### `core/inputs.py`
**Menaxhimi i inputit**

- Merr input nga përdoruesi:
  - plaintext / ciphertext
  - key
  - zgjedhjen e algoritmit
  - mënyrën (enc/dec)
- Ndihmon që input logjika të jetë e ndarë nga logjika e programit



### `core/validation.py`
**Validimi i inputeve**

- Kontrollon nëse inputet janë të sakta para përdorimit
- Validon:
  - mënyrën (`enc` / `dec`)
  - algoritmin (`V`, `T`, `B`)
  - key
  - tekstin
- Parandalon error-e gjatë ekzekutimit të algoritmeve

---

###  Moduli i Algoritmeve

### `algorithms/algorithm_control.py`
**Ndërmjetës mes core dhe algoritmeve**

- Merr vendimin se cili algoritëm duhet të ekzekutohet
- Thërret funksionin e duhur:
  - Vigenère
  - Turning Grille
- Ul kompleksitetin në `core_control.py`
- Shmang shumë `if/else` në logjikën kryesore


### `algorithms/vigenere_encrypt.py`
**Vigenère Encryption**

- Merr plaintext dhe key
- Aplikon formulën e Vigenère Cipher
- Kthen ciphertext


### `algorithms/vigenere_decrypt.py`
**Vigenère Decryption**

- Merr ciphertext dhe key
- Kryen procesin e kundërt të enkriptimit
- Kthen plaintext


### `algorithms/turning_grille_encrypt.py`
**Turning Grille Encryption**

- Merr plaintext, size dhe holes
- Vendos karakteret sipas rrotullimeve të grilës
- Gjeneron ciphertext


### `algorithms/turning_grille_decrypt.py`
**Turning Grille Decryption**

- Merr ciphertext, size dhe holes
- Lexon tekstin sipas hapjeve të grilës
- Rikthen plaintext


## Shembull
### Enkriptimi
Le te themi se kemi perdorur modin "enc" dhe algoritmin "v". 

`Hapi 1:`<br>

Japim tekstin dhe key.<br>
Text: HELLO <br>
Key: KEY <br>

`Hapi 2:` <br>

Funksioni start shikon te dhenat dhe i dergon tek funksioni use_vigenere()v<br>

`Hapi 3:`<br>

Funksioni use_vigenere() shikon te dhenat (nese eshte enc apo dec) dhe therret funksionin vigenere_encryption() <br>

`Hapi 4:` <br>

Ne vigenere_encrypt() key behet i gjate sa teksti, key-t i shtohen ne fund shkronjat e tij nga fillimi deri sa te behet i gjat sa texti. <br>
Tani kemi: <br>
Text: HELLO <br>
Key: KEYKE <br>

`Hapi 5:` <br>

Text dhe key kthehen ne ASCII dhe ju hiqet vlera ord('A') apo 65. <br>
Text: <br>
H → 72 - 65 = 7 <br>
E → 69 - 65 = 4 <br>
L → 76 - 65 = 11 <br>
L → 76 - 65 = 11 <br>
O → 79 - 65 = 14 <br>

Key: <br>
K → 75 - 65 = 10 <br>
E → 69 - 65 = 4 <br>
Y → 89 - 65 = 24 <br>
K → 75 - 65 = 10 <br>
E → 69 - 65 = 4 <br>

`Hapi 6:` <br>

Mblidhen Key dhe Text shkronje per shkronje dhe aplikojme mod 26 <br>
7 + 10 = 17 mod 26 = 17 <br>
4 + 4 = 8 mod 26 = 8 <br>
11 + 24 = 35 mod 26 = 9 <br>
11 + 10 = 21 mod 26 = 21 <br>
14 + 4 = 18 mod 26 = 18 <br>

`Hapi 7:` <br>

Keto shifra i mbledhim me ord('A') ose me 65 dhe i kthejme ne shkronja permes utf-8. <br>
82 → R <br>
73 → I <br>
74 → J <br>
86 → V <br>
83 → S <br>
Ciphertext: RIJVS <br>

 
### Dekriptimi
Le te themi se kemi perdorur modin "dec" dhe algoritmin "v". <br>

`Hapi 1:` <br>

Japim tekstin dhe key.<br>
Text: RIJVS<br>
Key: KEY<br>

`Hapi 2:` <br>

Funksioni start shikon te dhenat dhe i dergon tek funksioni use_vigenere()<br>

`Hapi 3:` <br>

Funksioni use_vigenere() shikon te dhenat (nese eshte enc apo dec) dhe therret funksionin vigenere_decryption()<br>

`Hapi 4:`<br>

Ne vigenere_decrypt() key behet i gjate sa teksti, key-t i shtohen ne fund shkronjat e tij nga fillimi deri sa te behet i gjat sa texti.<br>
Tani kemi:<br>
Text: RIJVS<br>
Key: KEYKE<br>

`Hapi 5:`<br>

Text dhe key kthehen ne ASCII dhe ju hiqet vlera ord('A') apo 65.<br>
Text: <br>
R → 82 - 65 = 17<br>
I → 73 - 65 = 8<br>
J → 74 - 65 = 9<br>
V → 86 - 65 = 21<br>
S → 83 - 65 = 18<br>
<br>
Key: <br>
K → 75 - 65 = 10 <br>
E → 69 - 65 = 4 <br>
Y → 89 - 65 = 24 <br>
K → 75 - 65 = 10<br>
E → 69 - 65 = 4<br>
<br>
`Hapi 6:`<br>

Text i zbresim Key shkronje per shkronje dhe aplikojme mod 26<br>
17 - 10 = 7 mod 26 = 7<br>
8 - 4 = 4 mod 26 = 4<br>
9 - 24 = -15 mod 26 = 11<br>
21 - 10 = 11 mod 26 = 11<br>
18 - 4 = 14 mod 26 = 14<br>

`Hapi 7:` <br>

Keto shifra i mbledhim me ord('A') ose me 65 dhe i kthejme ne shkronja permes utf-8.<br>
7 + 65 = 72 → H<br>
4 + 65 = 69 → E<br>
11 + 65 = 76 → L<br>
11 + 65 = 76 → L<br>
14 + 65 = 79 → O<br>
Plaintext: HELLO<br>



