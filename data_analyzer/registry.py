class Registry:
    def __init__(self):
        self.operations = {}
    
    def register(self, operation_name):
        def decorator(cls):
            self.operations[operation_name] = cls()
            return cls
        return decorator

    def get_operation(self, operation_name):
        if operation_name not in self.operations:
            raise ValueError(f"Operation '{operation_name}' is not registered.")
        return self.operations[operation_name]

operation_registry = Registry()
