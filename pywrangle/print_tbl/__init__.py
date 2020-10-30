# Import TableInfo class. Methods for: .init_tbl(), .add_entry(), .add_entres(), and .print_tbl()
try:
    from .script_objects import Any, Iterator, Table, Union, UserDefinedClass, Dict, Tuple
    from .tblinfo_aux import Aux_TblInfo
    from .table_class import TableInfo
    

except ModuleNotFoundError:
    from ..tableinfo.script_objects import Any, Iterator, Table, Union, UserDefinedClass
    from ..tableinfo.tblinfo_aux import Aux_TblInfo
    from ..tableinfo.table_class import TableInfo
 