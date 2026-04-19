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



