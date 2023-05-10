from typing import Optional

from pip_fluigio.__fluig_services_base.card import CardProvider
from pip_fluigio.__fluig_services_base.interfaces.card import CardData, Item
from pip_fluigio.fluig_services.infraestruture.server import ClientFluig
from pip_fluigio.utils.logger import Logger


class Card(CardProvider):
    def __init__(self, wsdl_url: str, client: Optional[ClientFluig] = None) -> None:
        self._client = client or ClientFluig(wsdl_url=wsdl_url)
        self._logger = Logger()

    def update_card_data(
        self,
        *,
        company_id: str,
        user_name: str,
        password: str,
        card_id: str,
        items: list[Item],
    ):

        try:

            self._logger.attribute.info(
                f"Start update card value by cardid - {card_id}"
            )

            return self._client.soap_intance.service.updateCardData(
                company_id, user_name, password, card_id, CardData(item=items).dict()
            )

        except Exception as error:
            self._logger.attribute.error(error)
