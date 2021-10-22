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

# Structural patterns
In Software Engineering, Structural Design Patterns are Design Patterns that ease the design by identifying a simple way to realize relationships between entities.

* **Adapter**
Match interfaces of different classes
* **Bridge**
Separates an object's interface from its implementation
* **Composite**
A tree structure of simple and composite objects
* **Decorator**
Add responsibilities to objects dynamically
* **Facade**
A single class that represents an entire subsystem
* **Flyweight**
A fine-grained instance used for efficient sharing
* **Private Class Data**
Restricts accessor/mutator access
* **Proxy**
An object representing another object


## Patrones de diseño - Facade
Lo que hace es que por medio de una fachada los usuarios pueden usar los servicios de manera mas facil sin saber la complejida que hay detras de estos. 

Facade es un patrón de diseño estructural que proporciona una interfaz simplificada (pero limitada) a un sistema complejo de clases, bibliotecas o _frameworks_.

**Ejemplos de uso**: El patrón Facade se utiliza habitualmente en aplicaciones escritas en Python. Es de especial utilidad al trabajar con bibliotecas y API complejas.

**Identificación:** El patrón Facade se puede reconocer en una clase con una interfaz simple, pero que delega la mayor parte del trabajo a otras clases. Normalmente, las fachadas gestionan todo el ciclo de vida de los objetos que utilizan.

## Decorador (Decorator)
Lo que este patron ofrece es que podamos agregar funcionalidades a un objeto existente sin alterar su estructura, que no haya necidad de alterar el codigo de la clase base.

## Proxy
**Intención**
El patrón de diseño de proxy incluye un nuevo objeto, que se denomina "Proxy" en lugar de un objeto existente que se denomina "Sujeto real". El objeto proxy creado del sujeto real debe estar en la misma interfaz de tal manera que el cliente no debería tener la menor idea de que se usa un proxy en lugar del objeto real. Las solicitudes generadas por el cliente al proxy se pasan a través del sujeto real.


# Behavioral patterns
In software engineering, behavioral design patterns are design patterns that identify common communication patterns between objects and realize these patterns. By doing so, these patterns increase flexibility in carrying out this communication.

* **Chain of responsibility**
A way of passing a request between a chain of objects
* **Command**
Encapsulate a command request as an object
* **Interpreter**
A way to include language elements in a program
* **Iterator**
Sequentially access the elements of a collection
* **Mediator**
Defines simplified communication between classes
* **Memento**
Capture and restore an object's internal state
* **Null Object**
Designed to act as a default value of an object
* **Observer**
A way of notifying change to a number of classes
* **State**
Alter an object's behavior when its state changes
* **Strategy**
Encapsulates an algorithm inside a class
* **Template method**
Defer the exact steps of an algorithm to a subclass
* **Visitor**
Defines a new operation to a class without change

## Command
* Promueve la encapsulación de la petición de una operación, bajo un metodo.

* El patrón de diseño de comandos es un patrón de diseño de comportamiento en el que una solicitud se puede convertir en acción.

**¿Dónde usar un patrón de diseño de comandos?**

Cuando necesitamos
* Hacer / deshacer acción.
* Cuando desee pasar el método como argumento o cuando desee llamar a una función de devolución de llamada. 
* Cuando queremos registrar o rastrear comandos.

**¿Por qué utilizar un patrón de diseño de comandos?**

Command Design Pattern es un patrón de diseño basado en solicitudes. Una solicitud ayudará a elegir qué comando debe ejecutarse sin saber qué método de objeto llamar. En este tipo de comando de caso, el patrón de diseño juega un papel clave, lo que facilita el uso de ICommand. El patrón de diseño de comandos en realidad desacopla el administrador de comandos y la lógica de ejecución de comandos, es decir, la implementación real.

**Jugadores en este patrón ICommand:** 

* ICommand: su interfaz que realizará la acción deshacer la acción.
* ConcreateCommand: el que implementa ICommand.
* Invoker - Aquel que lleva a cabo la acción.
* Receiver: One who receives action from invoker and performs action.