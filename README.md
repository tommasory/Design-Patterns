# Design-Patterns
In software engineering, a design pattern is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations.

# Creational patterns
In software engineering, creational design patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by somehow controlling this object creation.

Example of Abstract Factory

* **Abstract Factory**
Creates an instance of several families of classes
* **Builder**
Separates object construction from its representation
* **Factory Method**
Creates an instance of several derived classes
* **Object Pool**
Avoid expensive acquisition and release of resources by recycling objects that are no longer in use
* **Prototype**
A fully initialized instance to be copied or cloned
* **Singleton**
A class of which only a single instance can exist

## Patrón Factory
El patrón Factory hace parte de los patrones de creación. Te explico, dentro de los patrones de diseño existen tres categorías:

1. Patrones de creación.
2. Patrones de comportamiento.
3. Patrones estructurales.

Si quieres profundizar un poco en estas categorías, puedes leer más información al respecto.

Como su nombre lo indica, la idea de este patrón es tener una fábrica que cree objetos de distinto tipo, esto es suprémamente útil cuando no se sabe con antelación que objeto crear, por lo tanto se crearán en tiempo de ejecución. La factoría hace uso de parámetros para determinar qué objeto debe crear, nosotros (obviamente) debemos de proporcionarle tales parámetros.

### ¡Manos a la fábrica!
Qué mejor que un buen ejemplo para interiorizar lo anteriormente explicado, haremos una factoría que cree personas.

**Ingredientes:**
1. Una super-clase llamada **Persona**.
2. Dos clases que llevarán por nombre Masculino y Femenino, estas heredan de Persona.
3. Una clase Factoria, que nos representará la factoría como tal.
4. Un pequeño fichero, al que llamaremos main desde donde se iniciará la aplicación.
5. Sal y pimienta al gusto :)

**Preparación**:
En la siguiente imagen podrás ver los ficheros que he creado, todos en el mismo nivel.

## Fábrica abstracta

La fábrica abstracta se utiliza en el tejido de vehículos. El mismo dispositivo mecánico se utiliza para estampar partes de diferentes modelos de vehículos (puertas, paneles, cubiertas de carrocería, guardabarros y varios espejos). El modelo que agrega diferentes dispositivos mecánicos es configurable y se puede cambiar fácilmente en cualquier momento. enEste enlacePodemos ver un ejemplo de una fábrica abstracta para la fabricación de vehículos.

El ejemplo que se muestra a continuación se puede utilizar como referencia para la implementación de fábrica abstracta:

## Patrones de diseño - Prototype

Especificar los tipos de objetos para crear usando una instancia prototípica,
y cree nuevos objetos copiando este prototipo.
* Copia de objetos con los mismos valores