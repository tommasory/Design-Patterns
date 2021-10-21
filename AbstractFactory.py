from abc import ABC, abstractmethod

class Browser(ABC):
    """
    Creates "Abstract Product A"
    """

    # Interface - Create Search Toolbar
    @abstractmethod
    def create_search_toolbar(self):
        pass

    # Interface - Create Browser Window
    @abstractmethod
    def create_browser_window(self):
        pass

class Messenger(ABC):
    """
    Creates "Abstract Product B"
    """

    @abstractmethod
    # Interface - Create Messenger Window
    def create_messenger_window(self):
        pass

"""
Estos actúan como clases base para las siguientes clases concretas, es decir, variantes de producto de los productos abstractos: vainilla y seguro:
"""

class VanillaBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Interface - Create Search Toolbar
    def create_search_toolbar(self):
        print("Search Toolbar Created")

    # Interface - Create Browser Window]
    def create_browser_window(self):
        print("Browser Window Created")


class VanillaMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Interface - Create Messenger Window
    def create_messenger_window(self):
        print("Messenger Window Created")

class SecureBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Abstract Method of the Browser base class
    def create_search_toolbar(self):
        print("Secure Browser - Search Toolbar Created")

    # Abstract Method of the Browser base class
    def create_browser_window(self):
        print("Secure Browser - Browser Window Created")

    def create_incognito_mode(self):
        print("Secure Browser - Incognito Mode Created")


class SecureMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Abstract Method of the Messenger base class
    def create_messenger_window(self):
        print("Secure Messenger - Messenger Window Created")

    def create_privacy_filter(self):
        print("Secure Messenger - Privacy Filter Created")

    def disappearing_messages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")

"""
Puede notar que, además de los métodos abstractos, también se agregan características adicionales a los productos concretos para hacerlos funcionales en su propio contexto.

Estamos casi alli. Creemos ahora la propia fábrica abstracta y las correspondientes fábricas de hormigón como:
"""

class AbstractFactory(ABC):
    """
    The Abstract Factory
    """

    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass

class VanillaProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()

class SecureProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()

"""
En el código anterior, dado que AbstractFactory actúa como una clase base, los métodos abstractos se instancian tal como se menciona en la clase base.

Agreguemos un método main () para que veamos nuestro ejemplo en acción:
"""

def main():
    for factory in (VanillaProductsFactory(), SecureProductsFactory()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()
        product_a.create_browser_window()
        product_a.create_search_toolbar()
        product_b.create_messenger_window()

if __name__ == "__main__":
    main()

