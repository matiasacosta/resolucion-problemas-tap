## Problema I – Indecisos
### Autor: Pablo Zimmermann - Universidad Nacional de Rosario

Hoy es un dı́a importante en Nlogonia: se vota una ley clave para las nlogonas y los
legisladores están debatiendo arduamente. Conscientes de la importancia de las leyes para
defender los derechos de los nlogones menos privilegiados, muchas nlogonas están atentas
a este resultado. Inés, que espera esa ley desde hace muchos años, sigue atentamente las
noticias.

En Nlogonia las leyes se aprueban por mayorı́a simple (tiene que haber más votos por el
sı́ que por el no). En este paı́s, los legisladores siguen patrones curiosos para votar. Hay
algunos que votan en base a lo que prometieron, otros se basan en encuestas, otros que
ilusamente creen que siguiendo su opinión personal representan a quienes les votaron, e
incluso algunos que por desgracia responden a intereses de algún órgano de poder. Para
complicar los análisis, en muchos casos hay una combinación de estos factores.

Faltando cinco horas para la votación, gracias a Nlotter (red social en Nlogonia), se sabe
la opinión de cada legislador. ¡Sin embargo algunos aún están indecisos! Y posiblemente
sean esos votos los que determinen el resultado final de la ley.

Inés está muy ansiosa. ¿Podrı́an ayudarla a saber si ya es seguro que la ley se aprueba o
no, a pesar de los indecisos, o si el resultado depende de ellos?

#### Entrada
La entrada consiste en dos lı́neas. La primera lı́nea contiene un entero (1 ≤ N ≤ 1000)
que representa la cantidad de legisladores. La segunda lı́nea contiene una cadena de
caracteres L de longitud N que representan las posturas públicas de los legisladores de
Nlogonia. Cada carácter puede ser una ‘P’ que significa que ese legislador ya está seguro
de votar positivo, una ‘N’ que representa un voto negativo, o una ‘I’ que simboliza que
ese legislador está indeciso y todavı́a no definió su voto.

#### Salida
Imprimir en la salida una lı́nea conteniendo una cadena que representa la posibilidad de
que salga la ley. La cadena debe ser “SI” si ya es seguro que la ley se aprueba, “NO” si ya
es seguro que la ley no se aprueba, o “INDECISOS” si todavı́a depende de los indecisos.

| Entrada de ejemplo | Salida para la entrada de ejemplo |
|--------------------|-----------------------------------|
| 5                  | SI                                |
| PPIPN              |                                   |

| Entrada de ejemplo | Salida para la entrada de ejemplo |
|--------------------|-----------------------------------|
| 3                  | NO                                |
| NNI                |                                   |

| Entrada de ejemplo | Salida para la entrada de ejemplo |
|--------------------|-----------------------------------|
| 4                  | INDECISOS                         |
| PNII               |                                   |