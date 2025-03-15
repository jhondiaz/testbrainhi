
class DependencyContainer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._dependencies = {}
        return cls._instance

    def register(self, interface, implementation, *args, **kwargs):
        instance = implementation(*args, **kwargs)
        self._dependencies[interface] = instance

    def resolve(self, interface):
        instance = self._dependencies.get(interface)
        if not instance:
            raise ValueError(f"No se encontró implementación para la interfaz '{interface.__name__}'.")
        return instance

    def clear(self):
        self._dependencies.clear()

