from zeep.helpers import serialize_object
from zeep.xsd.valueobjects import CompoundValue


def convert_zeep_object(obj):
    if isinstance(obj, CompoundValue):
        obj = serialize_object(obj)

    if isinstance(obj, list):
        return [convert_zeep_object(sub) for sub in obj]

    if isinstance(obj, dict):
        return {k: convert_zeep_object(v) for k, v in obj.items()}

    return obj
