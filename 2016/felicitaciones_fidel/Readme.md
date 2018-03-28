## Problema F – ¡Felicitaciones, Fidel!
### Autor: Leopoldo Taravilse - Universidad de Buenos Aires

Fidel ha finalizado una fructífera etapa de su formación en la facultad, obteniendo su
doctorado en física. Esto es fundamentalmente fruto de la firmeza a la hora de formalizar
los fabulosos resultados de su fantástica investigación.
Fidel ha fomentado siempre la felicidad entre sus amigos y familiares, por lo que hemos
decidido firmarle una felicitación a nuestro doctor favorito. Habiendo finalizado la carta
de felicitación, solo resta incorporar la fervorosa firma de los F firmantes. Para esto,
hemos comprado dos fibrones, uno de color azul Francia, y el otro de color fucsia, con los
que cada firmante escribirá su nombre.
Es nuestra intención hacer foco en el título de doctor que acaba de obtener Fidel, y por
lo tanto queremos que en nuestras firmas se vea camuflada muchas veces la abreviación
de doctor (“DR”). Para esto, firmaremos utilizando ambos colores, y escribiremos algunas
letras en azul y otras en fucsia, de modo tal que si Fidel lee sólo las letras de color fucsia
pueda leer la sigla “DR”.
Nuestro objetivo es que, al leer únicamente las letras escritas en fucsia, Fidel sólo lea las
letras ‘D’ y ‘R’ de manera alternada. Por lo tanto, la primera letra de color fucsia debe
ser una ‘D’, y para cada letra ‘D’ que está escrita en fucsia, la próxima letra de ese color
deberá ser una ‘R’. Análogamente, para cada letra ‘R’ de color fucsia la siguiente letra de
ese color deberá ser una ‘D’, siendo entonces una ‘R’ la última letra de color fucsia.
Queremos escribir las letras en fucsia de modo tal que Fidel lea las letras ‘D’ y ‘R’ en ese
color la mayor cantidad de veces posible. Para cumplir nuestro objetivo, podemos elegir
en qué orden escribir nuestros nombres, y qué letras escribir de cada color. Como hay
muchas formas de hacer esto, les pedimos ayuda para que nos digan cuál es la mayor
cantidad de veces que podemos escribir las siglas “DR” de color fucsia si respetamos las
reglas dadas en el párrafo anterior.

###Entrada
La primera línea contiene un entero F, representando el número de firmantes (1 ≤ F ≤
1000). Cada una de las siguientes F líneas contiene el nombre de uno de los amigos de
Fidel. El nombre de cada amigo está compuesto por no más de 100 caracteres de la ‘A’ a
la ‘Z’.

##Salida
Imprimir en la salida una línea conteniendo un entero que representa la máxima cantidad
de veces que puede aparecer la sigla “DR” en fucsia al firmar nuestra carta de felicitación,
si escribimos las letras ‘D’ y ‘R’ alternadamente como se describe en el enunciado

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 10                     | 4                                        |
| RAMIRO                 |                                          |
| AUGUSTO                |                                          |
| JOAQUIN                |                                          |
| JACINTO                |                                          |
| NICOLAS                |                                          |
| ALEJANDRO              |                                          |
| DIJKSTRA               |                                          |
| KAJITA                 |                                          |
| MCDONALD               |                                          |
| SCHRODINGER            |                                          |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 4                      | 4                                        |
| DDD                    |                                          |
| RRR                    |                                          |
| DRDR                   |                                          |
| RDRD                   |                                          |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 12                     | 5                                        |
| MELANIE                |                                          |
| DAMIAN                 |                                          |
| RAMIRO                 |                                          |
| AUGUSTO                |                                          |
| JOAQUIN                |                                          |
| JACINTO                |                                          |
| NICOLAS                |                                          |
| ALEJANDRO              |                                          |
| DIJKSTRA               |                                          |
| KAJITA                 |                                          |
| MCDONALD               |                                          |
| SCHRODINGER            |                                          |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 4                      | 0                                        |
| ABCEFG                 |                                          |
| HIJKLM                 |                                          |
| NOPQST                 |                                          |
| UVWQYZ                 |                                          |