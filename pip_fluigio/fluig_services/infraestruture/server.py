from typing import Optional

from zeep.client import Client, Settings  # type:ignore


class ClientFluig:
    def __init__(
        self,
        wsdl_url: str,
        client_soap: Optional[Client] = None,
        settings: Optional[Settings] = None,
    ) -> None:
        self._URL_WSDL = wsdl_url
        self._client_soap = client_soap
        self._settings = settings or Settings(strict=False)  # type:ignore

    @property
    def soap_intance(self) -> Client:
        if self._client_soap is None:
            self._client_soap = Client(wsdl=self._URL_WSDL, settings=self._settings)
        return self._client_soap

    def get_element_in_xml(self, element: str):
        client = self.soap_intance
        return client.get_type(element)
