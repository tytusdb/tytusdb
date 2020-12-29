![Help Builder Web Site](./Logo.png)
# Justificacion
## ¿Porqué usamos una gramática Ascendente?

El análisis ascendente (bottom-up) tiene la primera
característica a favor, es que tiene una facilidad de
lectura y escritura para los desarrolladores de la
gramática haciendola entendible para el lenguaje
humano común.

Además que la herramienta (<b>PLY</b>) 
usada para este proyecto acepta de forma natural
gramáticas ascedendentes, si se quisiera utilizar
una descendente se tendría que implementar una pila 
y simular la ejecución descendente incrementando
el tiempo de ejecución dependiendo de la cantidad
de producciones que se pudiera tener, afectando la
eficiencia del analizador y retardando el resultado.

Si se necesita utilizar una gramática descendente
se recomienda utilizar otras herramientas optimizadas
para sacar el máximo provecho de su analizador 
para no afectar el rendimiento y 
funcionamiento de la aplicación.




  