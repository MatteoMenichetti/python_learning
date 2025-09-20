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

[Statments and syntax](#statments-and-syntax)


## Statments and syntax

ciao

queato