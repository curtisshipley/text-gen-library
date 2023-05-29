import logging
logging.basicConfig(level=logging.DEBUG)

from modules_management.module_manager import _get_module_factory
from modules_management.module_manager import _import_modules 


mod = _get_module_factory().create_model('ModelA')
mod.setup()
mod.generate("A", "B")
