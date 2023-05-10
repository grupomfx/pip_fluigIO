from pip_fluigio.__fluig_services_base.interfaces.dataset import DatasetQueryParams


class DatasetPropertiers:
    @classmethod
    def set_constraints(cls, field_name: str, value: str, type: str):
        return DatasetQueryParams(field_name=field_name, value=value, type=type)

    @classmethod
    def set_order(cls, sort_field: list):
        return list(sort_field)

    @classmethod
    def set_filter(cls, filters: list):
        return list(filters)
