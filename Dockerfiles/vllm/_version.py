__all__ = ["__version__", "__version_tuple__", "version", "version_tuple"]

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Tuple
    from typing import Union

    VERSION_TUPLE = Tuple[Union[int, str], ...]
else:
    VERSION_TUPLE = object

version: str
__version__: str
__version_tuple__: VERSION_TUPLE
version_tuple: VERSION_TUPLE

__version__ = version = '0.7.3.dev0+cu124'
__version_tuple__ = version_tuple = (0, 7, 3, 'dev0', 'cu124')
