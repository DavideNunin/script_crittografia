# Cryptography Educational Scripts

Questo repository contiene script educativi in Python per comprendere il funzionamento di alcune primitive crittografiche fondamentali.

## 📚 Contenuto

Il modulo `crypto_lib.py` implementa diverse operazioni crittografiche organizzate in classi tematiche:

### `NumberTheory`
Operazioni di teoria dei numeri:
- Test di primalità
- Fattorizzazione in numeri primi
- Funzione φ di Eulero
- Algoritmo esteso di Euclide
- Calcolo dei divisori

### `Groups`
Aritmetica modulare e teoria dei gruppi:
- Esponenziazione veloce (normale e modulare)
- Calcolo dell'inverso moltiplicativo (3 metodi: brute force, φ di Eulero, Euclide esteso)
- Ricerca di generatori per gruppi moltiplicativi

### `RSA`
Operazioni specifiche per RSA:
- Fattorizzazione tramite trial division

### `Montgomery`
Aritmetica di Montgomery per calcoli modulari efficienti:
- Generazione parametri
- Riduzione di Montgomery
- Moltiplicazione di Montgomery

## 🚀 Utilizzo

```python
from crypto_lib import NumberTheory, Groups, RSA, Montgomery

# Test di primalità
print(NumberTheory.isprime(17))  # True

# Esponenziazione modulare
result = Groups.fast_exp_mod(3, 5, 7)  # 3^5 mod 7

# Funzione φ di Eulero
phi_10 = NumberTheory.phi(10)  # 4

# Inverso moltiplicativo
inv = Groups.mult_inv_euclid(3, 11)  # 4

# Generatore di gruppo
gen = Groups.find_generator(11)
```

## ⚠️ Nota importante

**Questi script sono esclusivamente a scopo educativo e didattico.** Non sono ottimizzati per la produzione e non dovrebbero essere utilizzati in applicazioni reali che richiedono sicurezza crittografica.

Per applicazioni in produzione, utilizzare librerie crittografiche consolidate come:
- `cryptography`
- `PyCryptodome`
- `NaCl/libsodium`

## 📝 Requisiti

- Python 3.x
- Nessuna dipendenza esterna (solo libreria standard)

## 🎓 Scopo educativo

Questo repository è pensato per:
- Altri studenti di crittografia che vogliono comprendere gli algoritmi fondamentali
- Mio personale esercizio
