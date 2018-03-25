## Problema A – Audición
### Autor: Pablo Zimmermann - Universidad Nacional de Rosario

Eddard Stark: — Tú te casarás con un gran señor y reinarás su castillo.
Y tus hijos serán caballeros y príncipes y señores.
Arya Stark: — No. Esa no soy yo.

A pesar de que ahora, en un contexto de lucha por la igualdad de género, se recibe con
agrado la actitud de Arya, en los tiempos de la abuela Amalia las mujeres no tenían
muchas posibilidades de elegir qué querían hacer de sus vidas.
La abuela Amalia llegó a recibirse de profesora de piano, pero de adulta tuvo que dejar
sus estudios para ocuparse de los quehaceres del hogar. Más de sesenta a ̃nos despu ́es
su nieto tecladista descubrió que ella, a pesar de no haber tocado el piano en todo ese
tiempo, tenía la capacidad de reconocer una nota con solo oírla. Sin embargo se percató
de que su oído escuchaba las notas más agudas de lo que en realidad eran.
En nuestro sistema tonal, un semitono es la diferencia mínima que puede haber entre
una nota y otra. Una escala cromática es un conjunto ordenado de 12 notas, separadas
entre sí por un semitono. Para este problema consideramos arbitrariamente las notas de
la escala cromática que comienza en la nota “DO”. Las notas de esta escala, de más grave
a más aguda, se llaman: “DO”, “DO#”, “RE”, “RE#”, “MI”, “FA”, “FA#”, “SOL”,
“SOL#”, “LA”, “LA#” y “SI”. Esta escala se repite de manera cíclica, es decir, luego
de cada nota “SI” se encuentra un nuevo “DO” más agudo a un semitono de distancia,
y antes de cada “DO” hay un “SI” más grave, tambi ́en a un semitono de distancia.
Cada vez que Amalia escucha una nota y dice cuál cree que es, su nieto sabe que está
corrida S semitonos hacia las notas más agudas con respecto a lo que en realidad suena.
Por ejemplo, si S = 2 y Amalia dice que escucha un “LA”, la nota que en realidad suena
es dos semitonos más grave que la que dice escuchar, o sea un “SOL”.
Dada la nota que Amalia dice escuchar, escriban un programa que le ayude a su nieto a
saber cuál es la nota real correspondiente.

#### Entrada
La entrada consiste en una  ́unica línea que contiene un entero S y una cadena N. El entero
S representa el corrimiento de semitonos hacia las notas más agudas que escucha Amalia
(1 ≤ S ≤ 3). La cadena N es una de las 12 notas de la escala cromática mencionada
anteriormente: “DO”, “DO#”, “RE”, “RE#”, “MI”, “FA”, “FA#”, “SOL”, “SOL#”,
“LA”, “LA#” y “SI”, y representa la nota que Amalia dice escuchar.

#### Salida
Imprimir en la salida una línea conteniendo una cadena que representa la nota real que
suena sin el corrimiento de semitonos.

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 2 LA                   | SOL                                      |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 1 MI                   | RE#                                      |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 1 DO                   | SI                                       |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 3 SOL#                 | FA                                       |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 3 DO#                  | LA#                                      |
