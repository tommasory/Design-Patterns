# Design-Patterns
In software engineering, a design pattern is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations.


# ¿Qué es el Patrón Factory?
El patrón Factory hace parte de los patrones de creación. Te explico, dentro de los patrones de diseño existen tres categorías:

1. Patrones de creación.
2. Patrones de comportamiento.
3. Patrones estructurales.

Si quieres profundizar un poco en estas categorías, puedes leer más información al respecto.

Como su nombre lo indica, la idea de este patrón es tener una fábrica que cree objetos de distinto tipo, esto es suprémamente útil cuando no se sabe con antelación que objeto crear, por lo tanto se crearán en tiempo de ejecución. La factoría hace uso de parámetros para determinar qué objeto debe crear, nosotros (obviamente) debemos de proporcionarle tales parámetros.

## ¡Manos a la fábrica!
Qué mejor que un buen ejemplo para interiorizar lo anteriormente explicado, haremos una factoría que cree personas.

**Ingredientes:**
1. Una super-clase llamada **Persona**.
2. Dos clases que llevarán por nombre Masculino y Femenino, estas heredan de Persona.
3. Una clase Factoria, que nos representará la factoría como tal.
4. Un pequeño fichero, al que llamaremos main desde donde se iniciará la aplicación.
5. Sal y pimienta al gusto :)

**Preparación**:
En la siguiente imagen podrás ver los ficheros que he creado, todos en el mismo nivel.

