# Vigenère-Cipher-and-Turning-Grille-Fleissner-Grille-
Implementimi i algoritmeve të enkriptimit dhe dekriptimit Vigenère Cipher dhe Turning Grille (Fleissner Grille) në Python.

## Pershkrimi
Ky projekt implementon algoritmet kriptografike Vigenere dhe Turning Grille. Mer teksin nga useri dhe e enkripton/dekripton.

## Qëllimi
Ky eshte nje projekt universitar, qellimi i ketij projekti eshte te demonstroj se si algoritmet e ndryshme funksionojne ne praktike. 

## Struktura e Projektit
Projekti ka nje strukture te thjeshte. 
**Folderi algorithms** - permban algoritmet per enkriptim/dekriprim dhe kontrollin, i cili kontrollon se cili algoritem duhet te ekzekutohet.
**Folderi core** - kjo pjese, permban inputet e userit, validimin e tyre, kontrollon dhe nje ui ku useri jep te dhenat.


## Si Funksionon
Ne ui.py eshte thirrur funskioni start(), ky funsion gjendet ne core_control.py. Ai perdor file-at inputs.py dhe validation.py per ti mar te dhenar dhe validuar. Me ane te input.py meren te dhenat dhe validation.py validohen te dhenat.
Te dhenat pas inputit dhe validimit ruhen ne disa variabla ne funksionin start(). Ky funksion pastaj thirr njerin nga funksionet ne algorithm_control.py. Keto funksione pastaj percaktojne se cilat nga funksionet e enkriptimit/dekriptimit duhet te ekzekutohen. 
Rezultatet e enkriptimit/dekriptimit pastaj kthehen ne funksionin start() dhe printohen per userin.


## Perdorimi
Per ekzekutimin e projekt pas hapjes se folderit, shkruajme komanden  **py -m core/ui**. Aty do te pyetesh per enc/dec (enkriptim/dekriptim), pastaj jep llojin e algoritmit V ose t (Vigenere ose Turning Grille) dhe ne fund jep te dhenat si teksti, key etj.

## Shembull
### Enkriptimi
Le te themi se kemi perdorur modin "enc" dhe algoritmin "v". 
Hapi 1:
Japim tekstin dhe key.
Text: HELLO
Key: KEY

Hapi 2:
Funksioni start shikon te dhenat dhe i dergon tek funksioni use_vigenere()

Hapi 3: 
Funksioni use_vigenere() shikon te dhenat (nese eshte enc apo dec) dhe therret funksionin vigenere_encryption()

Hapi 4:
Ne vigenere_encrypt() key behet i gjate sa teksti, key-t i shtohen ne fund shkronjat e tij nga fillimi deri sa te behet i gjat sa texti.
Tani kemi:
Text: HELLO
Key: KEYKE

Hapi 5:
Text dhe key kthehen ne ASCII dhe ju hiqet vlera ord('A') apo 65.
Text: 
H → 72 - 65 = 7
E → 69 - 65 = 4
L → 76 - 65 = 11
L → 76 - 65 = 11
O → 79 - 65 = 14

Key: 
K → 75 - 65 = 10
E → 69 - 65 = 4
Y → 89 - 65 = 24 
K → 75 - 65 = 10
E → 69 - 65 = 4

Hapi 6:
Mblidhen Key dhe Text shkrinje per shkronje dhe aplikojme mod 26
7 + 10 = 17 mod 26 = 17
4 + 4 = 8 mod 26 = 8
11 + 24 = 35 mod 26 = 9
11 + 10 = 21 mod 26 = 21
14 + 4 = 18 mod 26 = 18

Hapi 7: 
Keto shifra i mbledhim me ord('A') ose me 65 dhe i kthejme ne shkronja permes utf-8.
82 → R
73 → I
74 → J
86 → V
83 → S
Ciphertext: RIJVS

### Dekriptimi
Le te themi se kemi perdorur modin "dec" dhe algoritmin "v". 
Hapi 1:
Japim tekstin dhe key.
Text: RIJVS
Key: KEY

Hapi 2:
Funksioni start shikon te dhenat dhe i dergon tek funksioni use_vigenere()

Hapi 3: 
Funksioni use_vigenere() shikon te dhenat (nese eshte enc apo dec) dhe therret funksionin vigenere_decryption()

Hapi 4:
Ne vigenere_decrypt() key behet i gjate sa teksti, key-t i shtohen ne fund shkronjat e tij nga fillimi deri sa te behet i gjat sa texti.
Tani kemi:
Text: RIJVS
Key: KEYKE

Hapi 5:
Text dhe key kthehen ne ASCII dhe ju hiqet vlera ord('A') apo 65.
Text: 
R → 82 - 65 = 17
I → 73 - 65 = 8
J → 74 - 65 = 9
V → 86 - 65 = 21
S → 83 - 65 = 18

Key: 
K → 75 - 65 = 10
E → 69 - 65 = 4
Y → 89 - 65 = 24 
K → 75 - 65 = 10
E → 69 - 65 = 4

Hapi 6:
Text i zbresim key shkrinje per shkronje dhe aplikojme mod 26
17 - 10 = 7 mod 26 = 7
8 - 4 = 4 mod 26 = 4
9 - 24 = -15 mod 26 = 11
21 - 10 = 11 mod 26 = 11
18 - 4 = 14 mod 26 = 14

Hapi 7: 
Keto shifra i mbledhim me ord('A') ose me 65 dhe i kthejme ne shkronja permes utf-8.
7 + 65 = 72 → H
4 + 65 = 69 → E
11 + 65 = 76 → L
11 + 65 = 76 → L
14 + 65 = 79 → O
Plaintext: HELLO



