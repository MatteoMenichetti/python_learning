# Appunti Python

## Interprete
Python è un linguaggio interpretato, quindi nessuna compilazione.

E' prodotto un byte code (estensione utilizzata `.pyc`) alla prima esecuzione, il quale viene eseguito dalla Python Virtual Machine. La compilazione del byte code è svolta solo alla prima esecuzione e rieseguita solo se ci sono modifiche ai file (il processo utilizza il timestamp dei file).

Il byte code permette di avere un'esecuzione più veloce degli script `.py`. Le implementazioni reali delle istruzioni possono essere in `c` come in `java`.

La `PVM` è il componente che realmente esegue gli script ed è l'ultimo step del'interprete di python.

## 2. Python Objects Type

### Why use built-in type?
In python i più utili `objects type` sono intriseche al linguaggio, cosiché non sia necessario implementarle. Inoltre
- **Built-in objects are components of extensions.** For more complex tasks, you may need to provide your own objects using Python classes or C language interfaces. Objects implemented manually are often built on top of built-in types such as lists and dictionaries. For instance, a stack data structure may be implemented as a class that manages or customizes a built-in list.
- **Built-in objects are often more efficient than custom data structures.** Python’s built-in types employ already optimized data structure algorithms that are
implemented in C for speed.

### Python’s Core Data Types

| object type                  | esempio                                                                      |
|------------------------------|------------------------------------------------------------------------------|
| Numbers                      | 1234, 3.1415, 3+4j, Decimal, Fraction                                        |
| Strings                      | 'spam', "guido's", b'a\x01c'                                                 |
| Lists                        | [1, [2, 'three'], 4]                                                         |
| Dictionaries                 | {'food': 'spam', 'taste': 'yum'}                                             |
| Tuples                       | (1, 'spam', 4, 'U')                                                          |
| Files                        | myfile = open('eggs', 'r')                                                   |
| Sets                         | set('abc'), {'a', 'b', 'c'}                                                  |
| Other core types             | Booleans, types, None                                                        |
| Program unit types           | [Functions](#4-functions) , [modules](#modules), [classes](#classes-and-oop) |
| Implementation-related types | Compiled code, stack tracebacks (Part IV, Part VII)                          |

As we’ll see in later, program units such as functions, modules, and
classes are objects in Python too—they are created with statements and expressions
such as def, class, import, and lambda and may be passed around scripts freely, stored
within other objects, and so on. Python also provides a set of implementation-related
types such as compiled code objects, which are generally of interest to tool builders
more than application developers; these are also discussed in later parts.

I tipi definiti dalla tabella sono `core data types` perché sono cablati in Python. Ad esempio:
```python
 'spam'
```
è letteralmente un'espressione che genera e ritorna un nuovo `string object`. In modo simile, un'espressione contenuta nelle paretesi quadrate produce una lista, una nelle tonde un dizionario e così via.

Una volta creato un `object`, su questo è possibile effettuare operazioni riguardati quel tipo (ad esempio è possibile applicare solo operazioni definite su una stringa per una stringa e operazioni definite su una lista per una lista). 

Inoltre, Python è `dynamically typed` (modifica il tipo senza richiedere dichiarazioni) ed anche `strongly typed` (è possibile applicare solo operazioni su un `object` relative al suo tipo).

### Numbers
Le operazioni sui numeri sono le solite, solo `**` è per l'esponenziale
```python
 2**4 # = pow(2,4)
16
```
Attenzione alla precisione macchina:
```python
 3.1415 * 2        # repr: as code
6.2830000000000004
 print(3.1415 * 2) # str: user-friendly
6.283
```
### Strings
Le stringhe sono considerate come sequenza, sono vettori. Sono collezioni ordinate di strighe formate da un singolo carattere.

```python
S = 'Spam'
S[0]
'S'
```

Gli indici di un vettore possono essere negativi, in tal caso il vettore sarà considerato dalla fine perché un indice negato è semplicemente aggiunto alla lunghezza del vettore (in questo caso della stringa):
```python
S[-1] # = S[len(S)-1]
'm'
```
Inoltre, è possibile selezionare un intervallo di valori in un vettore (aka slicing)

```python
S[0:2]
'Spa' #slice
S[1:] # Everything past the first (1:len(S))
'pam'
S # S itself hasn't changed
'Spam'
S[0:3] # Everything but the last
'Spa'
S[:3] # Same as S[0:3]
'Spa'
S[:-1] # Everything but the last again, but simpler (0:-1)
'Spa'
S[:] # All of S as a top-level copy (0:len(S))
'Spam'
```

Inoltre, come per tutti i vettori, è possibile la concatenzazione (per ogni tipo cambia la forma):
```python
S + 'xyz'
'Spamxyz'
S # S is unchanged
'Spam'
S * 8 # Repetition
'SpamSpamSpamSpamSpamSpamSpamSpam'
```

Le operazioni viste valgono per qualsiasi sequenza in Python, come liste e tuple.

#### Type-Specific Method

Ogni sequenza ha delle operazioni di base, le stringhe (come le altre sequenze speifiche come di numeri) hanno operazioni aggiuntive, disponibili come `methods`. Ad esempio 
```python
S.find('Pa') # Find the offset of a substring
1
```

#### Help

`dir(S)` fornisce tutti i `methods` associati ad una sequenza (vettore).

### Lists
La `list objects` è la più generale sequenxa in Python. Sono collezione posizionalmente ordinate, vettori, di `arbitraly typed objects` e non hanno una lunghezza fissata. 

```python
L = [123, 'spam', 1.23]
L[0] # Indexing by position
123
L[:-1] [123, 'spam']
# Slicing a list returns a new list
L + [4, 5, 6] 
# Concatenation makes a new list too
[123, 'spam', 1.23, 4, 5, 6]
```

#### Type-Specific Operations
Per aggiungere ed eliminare un elemento sono utilizate `append` e `pop` (le quali aggiungono e eliminano l'elemento alla fine della lista): 
```python
L.append('NI') # Growing: add object at end of list
L
[123, 'spam', 1.23, 'NI']
L.pop(2) # Shrinking: delete an item in the middle
1.23
```

#### Bounds Checking
Gli indici delle liste devono essere compresi tra 0 e `len(list)-1`.

#### Nesting
I `Python’s core data types` supportano la concatenazione arbitraria (per esempio, è possibile avere una lista che contiene dizionari, che contiene un'altra lista e così via). Un'applicazione immediata è quella delle matrici:

```python
M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
[4, 5, 6], # Code can span lines if bracketed
[7, 8, 9]]

M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

M[1] # Get row 2
[4, 5, 6]

>>>M[1][2] 
6
```
This matrix structure works for small-scale tasks, but for more serious number crunching you will probably
want to use one of the numeric extensions to Python, such as the open source NumPy system. Such tools can
store and process large matrixes much more efficiently than our nested list structure. NumPy has been said
to turn Python into the equivalent of a free and more powerful version of the Matlab system. 

#### Comprehensions
In aggiunta alle `sequence operations` and `list methods`, Python include operazioni avanzate conosciute come 
`list comprehension expression`, le quali sono utili per processare strutture come matrici.

Le `list comprehension expression` sono definite fra le parentesi quadre e composte da un espressione e un `looping construct` (eventualmente con l'aggiunta di clausole `if`) che fornisce una variabile (nel caso delle matrici `row` perché sono salvate per righe). Il risultato sono nuove liste che possono essere utilizzate per iterare su ogni `iterable objects`.

Supposto di dover estrarre la seconda colonna di una matrice, è più facile estrarla con una `list compression`:

```python
col2 = [row[1] for row in M]
col2
[2, 5, 8]

M[:][1]
[4, 5, 6]
```
Altri esempi:
```python
[row[1] + 1 for row in M] [3, 6, 9]
# Add 1 to each item in column 2

[row[1] for row in M if row[1] % 2 == 0] # Filter out odd items
[2, 8]

diag = [M[i][i] for i in range(len(M))] # Collect a diagonal from matrix
diag
[1, 5, 9]

doubles = [c * 2 for c in 'spam'] # Repeat characters in a string
doubles
['ss', 'pp', 'aa', 'mm']
```
 Le `list comprehensions` sono una feature opzionale, ma spesso forniscono un sostanziale vantaggio nella velocità di processamento

### Dictionaries
**I dizionari non sono del tutto delle seguenze**, sono conosciuti come `mappings`, ovvero sono anche collezioni di oggetti, dove questi sono immagazzinati per chiave invece che per posizione. 
Infatti, per i mappings non ha senso un ordinamento in base alla posizione della chiave (left-right order), semplicemente mappano le chiavi associate ai valori.

I dizionari sono gli unici `mapping type` nel `Python's core objects set` e sono mutabili: è possibile cambiare di posto agli elementi e farle crescere.

#### Mapping operation
Un dizionario ha la struttura
```python
D = {key : value , key_1 : value_2, ... , key_n : value_n}
```

La dichiarazione può avvenire nei seguenti modi

```python
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
```
oppure
```python
D = {}
D['name'] = 'Bob' # Create keys by assignment
D['job'] = 'dev'
D['age'] = 40
```

dove sono possibili operazioni sui singoli valori:
```Python
D['name']
'Bob'

D['age'] += 1
```

#### Nesting 
È possbile utilizzare tutti i tipi definiti precedentemente come `value`, per rappresentare informazioni complesse. Ad esempio:
```python
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'job': ['dev', 'mgr'],
'age': 40.5}
```
Nella prima riga sono presenti tre chiavi, alla chiave `'name'` è associato un `value` dizionario (`nesting dictionary`). Il valore associato alla chiave `'job'` è  una `list` (`nesting list`).

A tali valori è possibile accedere secondo il metodo associato alla struttura:
```python
rec['name']     #nesting dictionary
{'first': 'Bob', 'last': 'Smith'}

rec['name']['last']
'Smith'

rec['job'][1]
'mgr'

rec['job'].append('janiator') #aggiunta di un elemento alla lista associata alla chiave

rec
{'age': 40.5, 'job': ['dev', 'mgr', 'janitor'], 'name': {'last': 'Smith',
'first': 'Bob'}}
```

In Python è implementato il garbage collector: a differenza di linguaggi di programmazione di basso livello, la pulizia della memoria legata agli `object's space` è svolta in automatico **appena** (**IMMEDIATAMENTE**) è perso l'ultimo riferimento all'oggeto (per esempio assegnando un nuovo valore). Ad esempio

#### Sorting Key
Dato che i dizionari non sono sequenze come le liste, per avere le chiavi ordinate è necessario creare una lista ed ordinarle:
```python
D = {'a': 1, 'b': 2, 'c': 3}

ks = list(D.keys).sort()

ks = sorted(D)

```

**IMPORTANTE: CON CHIAVI DI DIVERSO TIPO (es. stringhe e int) NON È POSSIBILE IL CONFRONTO QUINDI L'ORDINAMENTO**.


#### Missing Key
Se ricercata una chiave che non è nel dizionario (es. `D['f']`) errore. Per evitarlo
```python
value = D.get('x', 0) # Index but with a default

value = D['x'] if 'x' in D else 0 
```

### Tuple
Una tupla è una sequenza immutabile, non modificabile, quindi è utile in tutti i contesti dove è necessaria una sequenza (tipo una lista) ma con la sicurezza di non poter essere modificata. Infatti non sono definite operazioni modificano tuple (ad esempio `pop()` e `append()`).

È definita tra parentesi tonde.

Pertano, rimangono valide le operazioni che si possono svolgere sulle `list`.

```python
T = (1, 2, 3, 4) # A 4-item tuple

T + (5, 6) # Concatenation
(1, 2, 3, 4, 5, 6) 

T[0] # Indexing, slicing, and more
1

T.index(4) # Tuple methods: 4 appears at offset 3
3

T.count(4) 1 # 4 appears once

T[0] = 2 # Tuples are immutable
...error text omitted...

T = ('spam', 3.0, [11, 22, 33])

T[1]
3.0

T[2][1]
22

T.append(4)
AttributeError: 'tuple' object has no attribute 'append'
```

### Other core types

#### set
Non sono `mapping` ne `sequences`, sono collezioni non ordinate di elementi unici e `immutable objects`.

Sono costruiti richiamando la function built-in `set` ed hanno tutte le operazioni degli insiemi matematici.

```python
X = set('spam') # Make a set out of a sequence in 2.6 and 3.0
Y = {'h', 'a', 'm'} # Make a set with new 3.0 set literals

X, Y
({'a', 'p', 's', 'm'}, {'a', 'h', 'm'})

X & Y # Intersection (valida anche X.intersection(Y))
{'a', 'm'} 

X | Y # Union (valida anche X.union(Y))
{'a', 'p', 's', 'h', 'm'}  

X – Y # Difference
{'p', 's'}

X^Y # Symmetric difference (valida anche X.symmetric_difference(Y))

>>> {x ** 2 for x in [1, 2, 3, 4]} # Set comprehensions in 3.0
{16, 1, 4, 9}
```

### And Everything Else
In Python tutto è un oggetto, ma solo solo ciò che è stato visto in [Python’s Core Data Types](#python’s-core-data-types) è un `Python's core type set`.
Altri tipi sono anche essi oggetti ma relativi all'esecuzione del programma (ad esempio `function`, `modules`, `classes` e `compiled code`).

### Dynamic Typing Interlude
Capitolo che tratta di `dynamic typing` e `polymorphism`.

In Python i tipi sono determinati a runtime automaticamente.

Ciclo di una variabile:
1) Creazione
   - la variabile è creata solo quando gli è assegnato un valore
2) Tipo
   - una variabile non ha un informazione riguardo al suo tipo, è generica e questa è un riferimento ad un oggetto in un partiacolare momento
3) Uso
   - la variabile è sostituita con l'oggetto al quale fa riferimento quando appare in un'espressione

### Shared References
Nel caso di assegnazioni di valori di `raw types` (come interi) le variabili non hanno `shallow copy` del valore.

Nel caso di assegnazioni di `lists` o costrutti che non sono `raw types` è possibile avere una `shallow copy` (assegnando il riferimento), ovvero come avviene in `c` o `java`:  
```python
L1  = [2,3,4]
L2 = L1 #copia il riferimento e non fa un deep copy.

L2[1] = 1

L1
[2,1,4]
```

Per fare una `deep copy`:
```python
L1 = [2, 3, 4]
L2 = L1[:]
```

Ciò si riperquote anche sul confronto:
```python
L = [1, 2, 3]
M = [1, 2, 3]   # M and L reference different objects
L == M # Same values
True
L is M # Different objects
False
```

**NOTA: per i `raw types` `==` e `is` si equivalgono**.

## 3 Statments and syntax

Un programma python è composto come segue:
1. Programs are composed of modules.
2. Modules contain statements.
3. `Statements` contain `expressions`.
4. Expressions create and process objects.

Con `statments` e `expressions` sono intese rispettivamente la logica di una operazione ed il processamento di `objects` dello `statments`.

Alcuni esempi di `statments` sono le assegnazioni di valori, i `def` e `class` per definire funzioni e metodi e classi , i cicli, `import`. **(Vedere pagina 313)**.

### Syntax
Tutti i `compound statements` (cicli, condizioni, definizioni classi e metodi) sono della forma
```
Header line:
    Nested statement block
```
### Assigment Statments

Alcune cose da ricordare:
- **Assignments create object references.** Come descritto in [Dynamic Typing Interlude](#dynamic-typing-interlude), l'assegnazione assegna il riferimento all'`objects` al nome o alla `data structure` perché le variabili sono più puntatori che `data storage areas`.
- **Names are created when first assigned.** Le variabili sono create alla prima assegnazione (nessun bisogno di predichiarle). Una volta assegnato, un nome è sostituiro dal valore a cui si riferisce. Alcune `data structure slots` sono create quando assegnate.
- **Some operations perform assignments implicitly.** Alcune operazioni assegnano implicitamente variabili, ad esempio `for x in [0, 1, 2]`.

#### Advaced sequence assigment patterns
```python
string = 'SPAM'
a, b, c, d = string # Same number on both sides
a, d
('S', 'M')
a, b, c = string 
...error text omitted...
ValueError: too many values to unpack
```
```pyhon
a, b, c = string[0], string[1], string[2:] # Index and slice
a, b, c
('S', 'P', 'AM')

a, b, c = list(string[:2]) + [string[2:]] # Slice and concatenate
a, b, c
('S', 'P', 'AM')
```
```python
seq = [1, 2, 3, 4]

a, *b = seq 

a, b
(1, [2, 3, 4])
```

```python
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ... # Simple tuple assignment

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ... # Nested tuple assignment
```

#### Variable Name Rules
La forma delle variabili consigliata è `(underscore or letter)+(any number of letters, digit or underscores)` (nessun carattere speciale).

### break, continue, pass
- `break`, esce dal ciclo;
- `continue`, salta all'inizio del ciclo (loop's header line);
- `pass`, non fa niente
### Itereators and Compresion, Part 1
Un `iterable object` è una generalizzazione del concetto di sequenza, in quanto un `object` è  considerato `iterable` se è `stored` come sequenza oppure un `object` che produce un risultato alla volta nel contesto dei un `iteration tool` (come un `for`), comprendendo le `virtual sequence`.

`iterable` e `iterator` spesso si riferiscono, rispettivamente, ad un `object` che supporta `iter` e ad un `object` restituito da un `iter` che supporta `next(I)`. Oppure i due termini possono essere intercabili in riferimento ad un `object` che supporta iterazioini in generale. 

#### Iteration Protocol: File Iterators
Un `file object` ha un metodo `readline` che ogni volta che viene invocato restiusce una stringa contentente una riga ed una riga vuota alla fine del file.

```python
f = open('file.extesion') # Read a 4-line script file in this directory
f.readline() # readline loads one line on each call
'riga 1'

f.readline()
'riga 2'

f.readline() # Returns empty string at end-of-file
''
```
oppure invocando `__next__` su `f` (`f.__next__()`) si ha lo stesso effetto ma con un'ececezione `StopIteration` alla fine del file.

Inoltre, è presente una function (stesso effetto dell'ultimo esempio) `next` che invoca automaticamente la chiama `__next__` di un `object`.

```python
f = open('file.extesion') # Read a 4-line script file in this directory

next(f) # readline loads one line on each call
'riga 1'

next(f)
'riga 2'

f.readline() # Returns empty string at end-of-file
''
```

#### List compressions
Operazioni come 
```python
L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] += 10
```

può non essere un'operazione ottimale in Python. È possibile produrre quasi lo stesso risultato attraverso

```python
L = [x + 10 for x in L]

#codice equivalente:
res=[]
for x in L:
    res.append(x+10)
L = res
```
In questo modo l'operazione necessita di meno righe di codice ed è sostanzialmente più veloce, con l'unico inconveniente che resituisce un nuova `list object` (e in alcuni casi può essere importante mantere il riferimento all'originale lista).

Una `list comprehension` inizia con un'espressione arbitraria (`x+10`), seguita da un `for` che itera su un `iterable object` (`for x in L`).

##### List comprehension su file

Se è necessario leggere tutte le stringhe di un file è possibile quanto segue:
```python
f = open('script1.py')

lines = f.readlines()

lines
['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n']
```
se è nessario che non siano presenti caratteri `\n`, allora
```python
lines = [line.rstrip() for line in open('script1.py')]
```

Un altro modo fare quanto descritto:
```python
lines = list(map(str.strip, open('script1.py').readlines()))
```

Un ulteriore esempio è
```python
lines = [line.rstrip() for line in open('script1.py') if line[0] == 'p']

lines
['print(sys.path)', 'print(2 ** 33)']
```

Le `list comprehensions` possono essere più complesse, se necessario, includendo `for` annidiati con eventuali clausole `if` associate. Ad esempio:
```python
[x + y for x in 'abc' for y in 'lmn']
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
```

Nel capitolo [Iteration and Comprehensions, Part 2](#itereators-and-compresion-part-2) sarà discusso delle `list comprehensions` nel contesto della programmazione funzionale.

##### Altre iterazioni possibili

```python
>>> list(open('script1.py'))
['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n']

>>> tuple(open('script1.py'))
('import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n')

>>> '&&'.join(open('script1.py'))
'import sys\n&&print(sys.path)\n&&x = 2\n&&print(2 ** 33)\n'

>>> set(open('script1.py'))
{'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n', 'import sys\n'}

>>> {line for line in open('script1.py')}
{'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n', 'import sys\n'}
```

## 4 Function