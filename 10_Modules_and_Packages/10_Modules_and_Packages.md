## Modules and Packages

Python projects should be structured in the following way, making sure that every directory defines an **init**.py file:

pytest_debug_project/
**init**.py
common/
**init**.py
archivo_1.py
archivo_2.py
common2/
**init**.py
archivo_3.py
tests/
conftest.py
test_archivo_1.py
test_archivo_2.py
test_archivo_3.py
main.py

The init file is used to execute initial code from a package when is imported, for example:

```
import common2
```

This would import all the code located in the **init**.py file inside the common2 package

So if the content of this **init**.py is:

```
from . import archivo_1
from . import archivo_2
```

Both imports will be placed with the same statement

In python3 it is not needed to specicified theses **init** files, works even if dont exist

## Import of everything

When you want to import all the functions and constantes o a python module, you just need to write:

```
from module import *
```

If you want to specify concrete functions to be imported with this statemen, just use the **all** variable inside the module:

```
__all__ = [function1, function2]
```

## Relative imports

To import functions of an external module inside the same package:

```
#pytest_debug_project/common/archivo_1.py
from .archivo_2 import function_2
```

To import functions outside that subpackage:

```
#pytest_debug_project/common/archivo_1.py
from ..common_2. archivo_3 import funcion_3
```

Inside packages, imports involving modules in the same package can either use fully specigied absolite names or a relative imports uding the syntax shown:

```
#pytest_debug_project/common/archivo_1.py
from pytest_debug_project.common import archivo_2           # Correct
from . import archivo_2                             # Correct
import archivo_2                                    # Error
```

It is more recommended to use relative imports, as it gives more freedom in case you are willing to change the project structure in the future. With absolute imports, if you are planning to change a name, you will have to update every single file involving that import

When using relative imports, the from ... import ... is the way to go.

It is important to have in mind that relative imports only work when working inside a package at the root level.

If you want to execute in a separate way a submodule then you need to use the -m notation when running the script:

```
python3 pytest_debug_project/common/archivo_1.py        # Error
python3 -m pytest_debug_project.common.archivo_1        # Correct
```
