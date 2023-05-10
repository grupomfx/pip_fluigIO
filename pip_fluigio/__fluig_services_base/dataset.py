from abc import ABC
from typing import List


class DatasetProvider(ABC):
    def __init__(self):
        pass

    def get_dataset(self) -> List[dict]:

        """
        Description: Method is abstract webservice soap fluig is get dataset

        Returns: list()

        Raises: None

        """

        return list()

    def disable_dataset(self) -> None:

        """
        Description: Method is abstract webservice soap fluig is disabled dataset

        Returns: None

        Raises: None

        """

        return

    def get_available_datasets(self) -> List[dict]:

        """
        Description: Method is abstract webservice soap fluig return is dataset available by form

        Returns: list()

        Raises: None

        """

        return list()

    def get_all_available_dataset(self) -> List[dict]:

        """
        Description: Method is abstract webservice soap fluig return is dataset available by form

        Returns: list()

        Raises: None

        """

        return list()
