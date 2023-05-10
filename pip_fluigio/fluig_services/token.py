from typing import Optional

from pip_fluigio.__fluig_services_base.token import TokenProvider
from pip_fluigio.fluig_services.infraestruture.server import ClientFluig
from pip_fluigio.utils.logger import Logger


class Token(TokenProvider):
    def __init__(self, *, wsdl_url: str, client: Optional[ClientFluig] = None) -> None:

        self._client = client or ClientFluig(wsdl_url=wsdl_url)
        self._logger = Logger()

    def get_token(self, *, login: str, password: str):

        try:

            self._logger.attribute.info("Request token with webservice")

            response = self._client.soap_intance.service.getToken(password, login)

            if response:
                return response

            else:
                return

        except Exception as error:
            self._logger.attribute.error(error)

    def get_token_by_login(self, *, company_id: str, user_id: str, password: str, login: str):

        try:

            self._logger.attribute.info("Request login with webservice")

            response = self._client.soap_intance.service.getTokenByLogin(company_id, user_id, password, login)

            if response:
                return response

            else:
                return

        except Exception as error:
            self._logger.attribute.error(error)

    def get_token_by_email(self, *, company_id: str, password: str, email: str):

        try:

            self._logger.attribute.info("Request login by email with webservice")

            response = self._client.soap_intance.service.getTokenEmail(
                company_id,
                email,
                password,
            )

            if response:
                return response

            else:
                return

        except Exception as error:
            self._logger.attribute.error(error)

    def validate_token(self, *, token: str):

        try:

            self._logger.attribute.info("Validate Login with webservice")

            response = self._client.soap_intance.service.validateToken(token)

            if response:
                item = {}
                item.update({"user": response, "token": token, "validate": True})
                return item

            else:
                return

        except Exception as error:
            self._logger.attribute.error(error)
