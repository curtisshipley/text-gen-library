import sys
import logging
import pkgutil
import importlib
from .module_factory import ModelFactory

moduleFactory = ModelFactory()
managerLogger = logging.getLogger("module_manager")


def _get_module_factory():
    return moduleFactory

def _import_modules():
    import modules
    managerLogger.info('Importing modules')
    for importer, package_name, _ in pkgutil.iter_modules(modules.__path__):
        full_package_name = '%s.%s' % (modules.__name__, package_name)
        if full_package_name not in sys.modules:
            module = importlib.import_module(full_package_name)
            module.register_model(moduleFactory)

_import_modules()

