from abc import ABC


class TokenProvider(ABC):
    def __init__(self):
        pass

    def get_token(self) -> dict:
        """
         Decription:

        Returns:

        Args:

        Raises:

        """
        return dict()

    def get_token_by_login(self) -> dict:

        """
         Decription:

        Returns:

        Args:

        Raises:

        """
        return dict()

    def get_token_by_email(self) -> dict:

        """
         Decription:

        Returns:

        Args:

        Raises:

        """
        return dict()

    def validate_token(self) -> None:

        """
         Decription:

        Returns:

        Args:

        Raises:

        """
        return
