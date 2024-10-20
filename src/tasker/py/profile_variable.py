from dataclasses import dataclass


@dataclass
class ProfileVariable:
    config_type: str = 't'

    config_on_imported: bool = False
    structure_variable: bool = False
    immutable: bool = False
    
    variable_name: str = '%aaa'
    value: str = ''
    display: str = ''
    prompt: str = ''

    same_value: bool = True
    exported_value: str = ''
