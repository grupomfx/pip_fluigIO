from pip_fluigio.__fluig_services_base.interfaces.card import Item


class CardProperties:
    @classmethod
    def set_values(cls, fields: dict):

        list_items = []
        for key, value in fields.items():
            list_items.append(Item(field=key, value=value))

        return list_items
