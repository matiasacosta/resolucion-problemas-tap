## Problema C – Correlatividades
### Autor: Mariano Crosetti - Universidad Nacional de Rosario

Terminar una carrera universitaria no s´olo es cuesti´on de estudiar y aprender. Para hacerse con el preciado t´ıtulo universitario, cada alumno tiene que demostrar lo que ha
aprendido, y para ello debe aprobar N materias. A menudo es necesario adem´as respetar
innumerables y deliberadamente caprichosos laberintos reglamentarios.
En el Instituto Con Pocas Correlatividades (ICPC) rigen antiguas normas que impiden
a los alumnos aprobar ciertas materias no habiendo aprobado antes algunas otras. Estas
´ultimas son llamadas \correlativas" de las primeras. Cada materia puede tener cero o
m´as materias correlativas, pero no existen correlatividades c´ıclicas, de modo que siempre
es posible terminar una carrera.
Gabina es una alumna de Ciencias de la Contentura, y afortunadamente sus profesores
son personas extremadamente comprensivas. Por ello, le permiten a Gabina aprobar materias sin tener sus correlativas aprobadas. El inconveniente es que el sistema inform´atico
del ICPC s´olo puede registrar las materias como aprobadas respetando el r´egimen de
correlatividades. De este modo, una materia estar´a registrada si y s´olo si est´a aprobada
y tiene todas sus materias correlativas registradas.
Ver su progreso mantiene a Gabina motivada, y le ayuda a continuar con sus estudios. Es
por esto que cada vez que aprueba una materia, chequea despu´es en el sistema inform´atico
la cantidad de materias que figuran registradas. A veces encuentra que esta cantidad
no ha variado, puesto que no pose´ıa registradas todas las correlativas de la materia
recientemente aprobada. Otras veces, recibe la grata sorpresa de que la cantidad de
materias registradas ha aumentado. En ocasiones, el aumento puede incluso ser en m´as de
uno, lo cual ocurre cuando la materia que aprob´o estaba en condiciones de ser registrada,
y al serlo destrab´o el registro de una serie de materias aprobadas con anterioridad, que
ahora est´an en condiciones de ser a su vez registradas por el sistema.
Gabina ya tiene planeado el orden en que aprobar´a todas las materias de su carrera.
Desea ahora determinar la cantidad de materias que figurar´an registradas en el sistema
luego de aprobar cada una de ellas. Su tarea es escribir un programa que ayude a Gabina
a predecir esto, para que ella pueda terminar felizmente la carrera de Ciencias de la
Contentura.
#### Entrada
La primera l´ınea contiene dos enteros N y M, que representan la cantidad de materias
de la carrera y la cantidad de relaciones de correlatividad entre pares de materias, respectivamente (1 ≤ N; M ≤ 5× 104). Las materias est´an identificadas por los n´umeros del
1 al N. Cada una de las siguientes M l´ıneas contiene dos enteros A y B (1 ≤ A; B ≤ N
con A 6= B) indicando que la materia A es correlativa de B. Esto significa que la materia A debe estar registrada como aprobada antes de poder registrar la materia B como
aprobada. No hay en la entrada relaciones de correlatividad repetidas ni correlatividades
c´ıclicas. La ´ultima l´ınea contiene N n´umeros P1, P2, . . . , PN que representan las materias
en el orden en el que Gabina las aprobar´a (1 ≤ Pi ≤ N para i = 1; : : : ; N, con Pi 6= Pj
para i 6= j)
#### Salida
Imprimir N l´ıneas con un n´umero cada una. El n´umero en la i-´esima l´ınea representa la
cantidad de materias registradas en el sistema inmediatamente despu´es de que Gabina
apruebe cada una de las materias de la carrera en el orden dado en la entrada.

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 3 2                    | 1                                        |
| 1 2                    | 2                                        |
| 2 3                    | 3                                        |
| 1 2 3                  |                                          |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 3 2                    | 0                                        |
| 1 2                    | 0                                        |
| 2 3                    | 3                                        |
| 3 2 1                  |                                          |

| Entrada de Ejemplo     | Salida para la entrada de ejemplo        |
| -----------------------|------------------------------------------|
| 4 4                    | 0                                        |
| 1 2                    | 0                                        |
| 2 3                    | 2                                        |
| 4 3                    | 4                                        |
| 1 4                    |                                          |
| 2 3 1 4                |                                          |
