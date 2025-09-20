# Appunti Python

## Interprete
Python è un linguaggio interpretato, quindi nessuna compilazione.

E' prodotto un byte code (estensione utilizzata `.pyc`) alla prima esecuzione, il quale viene eseguito dalla Python Virtual Machine. La compilazione del byte code è svolta solo alla prima esecuzione e rieseguita solo se ci sono modifiche ai file (il processo utilizza il timestamp dei file).

Il byte code permette di avere un'esecuzione più veloce degli script `.py`. Le implementazioni reali delle istruzioni possono essere in `c` come in `java`.

La `PVM` è il componente che realmente esegue gli script ed è l'ultimo step del'interprete di python.

## 2. Python Objects Type

Un programma python è composto come segue:
1. Programs are composed of modules.
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects.

`objects` sono intese `data structures`.

### Why use built-in type?
In python i più utili `objects type` sono intriseche al linguaggio, cosiché non sia necessario implementarle. Inoltre
- **Built-in objects are components of extensions.** For more complex tasks, you may need to provide your own objects using Python classes or C language interfaces. Objects implemented manually are often built on top of built-in types such as lists and dictionaries. For instance, a stack data structure may be implemented as a class that manages or customizes a built-in list.
- **Built-in objects are often more efficient than custom data structures.** Python’s built-in types employ already optimized data structure algorithms that are
implemented in C for speed.

### Python’s Core Data Types

| object type                  | esempio                                                                    |
|------------------------------|----------------------------------------------------------------------------|
| Numbers                      | 1234, 3.1415, 3+4j, Decimal, Fraction                                      |
| Strings                      | 'spam', "guido's", b'a\x01c'                                               |
| Lists                        | [1, [2, 'three'], 4]                                                       |
| Dictionaries                 | {'food': 'spam', 'taste': 'yum'}                                           |
| Tuples                       | (1, 'spam', 4, 'U')                                                        |
| Files                        | myfile = open('eggs', 'r')                                                 |
| Sets                         | set('abc'), {'a', 'b', 'c'}                                                |
| Other core types             | Booleans, types, None                                                      |
| Program unit types           | [Functions](#functions) , [modules](#modules), [classes](#classes-and-oop) |
| Implementation-related types |  Compiled code, stack tracebacks (Part IV, Part VII)                       |

As we’ll see in later, program units such as functions, modules, and
classes are objects in Python too—they are created with statements and expressions
such as def, class, import, and lambda and may be passed around scripts freely, stored
within other objects, and so on. Python also provides a set of implementation-related
types such as compiled code objects, which are generally of interest to tool builders
more than application developers; these are also discussed in later parts.

I tipi definiti dalla tabella sono `core data types` perché sono cablati in Python. Ad esempio:
```python
>>> 'spam'
```
è letteralmente un'espressione che genera e ritorna un nuovo `string object`. In modo simile, un'espressione contenuta nelle paretesi quadrate produce una lista, una nelle tonde un dizionario e così via.

Una volta creato un `object`, su questo è possibile effettuare operazioni riguardati quel tipo (ad esempio è possibile applicare solo operazioni definite su una stringa per una stringa e operazioni definite su una lista per una lista). 

Inoltre, Python è `dynamically typed` (modifica il tipo senza richiedere dichiarazioni) ed anche `strongly typed` (è possibile applicare solo operazioni su un `object` relative al suo tipo).

### Numbers
Le operazioni sui numeri sono le solite, solo `**` è per l'esponenziale
```python
>>> 2**4 # = pow(2,4)
16
```
Attenzione alla precisione macchina:
```python
>>> 3.1415 * 2        # repr: as code
6.2830000000000004
>>> print(3.1415 * 2) # str: user-friendly
6.283
```
### Strings
Le stringhe sono considerate come sequenza, sono vettori. Sono collezioni ordinate di strighe formate da un singolo carattere.

```python
>>> S = 'Spam'
>>> S[0]
'S'
```

Gli indici di un vettore possono essere negativi, in tal caso il vettore sarà considerato dalla fine perché un indice negato è semplicemente aggiunto alla lunghezza del vettore (in questo caso della stringa):
```python
>>> S[-1] # = S[len(S)-1]
'm'
```
Inoltre, è possibile selezionare un intervallo di valori in un vettore (aka slicing)

```python
>>> S[0:2]
'Spa' #slice
>>> S[1:] # Everything past the first (1:len(S))
'pam'
>>> S # S itself hasn't changed
'Spam'
>>> S[0:3] # Everything but the last
'Spa'
>>> S[:3] # Same as S[0:3]
'Spa'
>>> S[:-1] # Everything but the last again, but simpler (0:-1)
'Spa'
>>> S[:] # All of S as a top-level copy (0:len(S))
'Spam'
```

Inoltre, come per tutti i vettori, è possibile la concatenzazione (per ogni tipo cambia la forma):
```python
>>> S + 'xyz'
'Spamxyz'
>>> S # S is unchanged
'Spam'
>>> S * 8 # Repetition
'SpamSpamSpamSpamSpamSpamSpamSpam'
```

Le operazioni viste valgono per qualsiasi sequenza in Python, come liste e tuple.

#### Type-Specific Method

Ogni sequenza ha delle operazioni di base, le stringhe (come le altre sequenze speifiche come di numeri) hanno operazioni aggiuntive, disponibili come `methods`. Ad esempio 
```python
>>> S.find('Pa') # Find the offset of a substring
1
```

#### Help

`dir(S)` fornisce tutti i `methods` associati ad una sequenza (vettore).

### Lists
La `list objects` è la più generale sequenxa in Python. Sono collezione posizionalmente ordinate, vettori, di `arbitraly typed objects` e non hanno una lunghezza fissata. 

```python
>>> L = [123, 'spam', 1.23]
>>> L[0] # Indexing by position
123
>>> L[:-1] [123, 'spam']
# Slicing a list returns a new list
>>> L + [4, 5, 6] 
# Concatenation makes a new list too
[123, 'spam', 1.23, 4, 5, 6]
```

#### Type-Specific Operations
Per aggiungere ed eliminare un elemento sono utilizate `append` e `pop` (le quali aggiungono e eliminano l'elemento alla fine della lista): 
```python
>>> L.append('NI') # Growing: add object at end of list
>>> L
[123, 'spam', 1.23, 'NI']
L.pop(2) # Shrinking: delete an item in the middle
>>> 1.23
```

#### Bounds Checking
Gli indici delle liste devono essere compresi tra 0 e `len(list)-1`.

#### Nesting
I `Python’s core data types` supportano la concatenazione arbitraria (per esempio, è possibile avere una lista che contiene dizionari, che contiene un'altra lista e così via). Un'applicazione immediata è quella delle matrici:

```python
>>> M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
[4, 5, 6], # Code can span lines if bracketed
[7, 8, 9]]

>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> M[1] # Get row 2
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
>>> col2 = [row[1] for row in M]
>>> col2
[2, 5, 8]

>>> M[:][1]
[4, 5, 6]
```
Altri esempi:
```python
>>> [row[1] + 1 for row in M] [3, 6, 9]
# Add 1 to each item in column 2

>>> [row[1] for row in M if row[1] % 2 == 0] # Filter out odd items
[2, 8]

>>> diag = [M[i][i] for i in [0, 1, 2]] # Collect a diagonal from matrix
>>> diag
[1, 5, 9]

>>> doubles = [c * 2 for c in 'spam'] # Repeat characters in a string
>>> doubles
['ss', 'pp', 'aa', 'mm']
```
 

## Statments and syntax
