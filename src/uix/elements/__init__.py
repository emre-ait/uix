import sys
import os
from types import ModuleType
import importlib
__modules = []
__all__ = __modules
print("Imported: __init__")
for __file in os.listdir(os.path.dirname(__file__)):
    if __file.endswith(".py") and __file.startswith("_") and __file != "__init__.py":
        module_name = __file[1:-3]
        __modules.append(module_name)


def __getattr__(name):
    if name in __modules:
        module = importlib.import_module(f"uix.elements._{name}")
        attr = getattr(module, name)
        return attr
    raise AttributeError(f"module {__name__} has no attribute {name}")
    

def __dir__():
    """Just show what we want to show."""
    print("Imported: __dir__")
    result = list(__modules)
    result.extend(
        (
            "__file__",
            "__doc__",
            "__all__",
            "__docformat__",
            "__name__",
            "__path__",
            "__package__",
            "__version__",
        )
    )
    return result