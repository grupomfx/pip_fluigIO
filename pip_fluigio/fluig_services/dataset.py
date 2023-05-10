from typing import List, Optional

from pip_fluigio.__fluig_services_base.dataset import DatasetProvider
from pip_fluigio.__fluig_services_base.interfaces.dataset import (
    DatasetQuery,
    DatasetQueryParams,
    StructConstraint,
    StructField,
    StructOrder,
)
from pip_fluigio.fluig_services.infraestruture.server import ClientFluig
from pip_fluigio.utils.commomns import convert_zeep_object
from pip_fluigio.utils.logger import Logger


class Dataset(DatasetProvider):
    def __init__(self, wsdl_url: str, client: Optional[ClientFluig] = None) -> None:
        self._client = client or ClientFluig(wsdl_url=wsdl_url)
        self._logger = Logger()

    def __constraints(self, constraints: List[StructConstraint]):
        constraint_array_element = self._client.get_element_in_xml(element="ns0:searchConstraintDtoArray")
        constraint_element = self._client.get_element_in_xml(element="ns0:searchConstraintDto")
        items = []
        for value in constraints:
            items.append(
                constraint_element(  # type:ignore
                    value.constraint_type,
                    value.field_name,
                    value.init_value,
                    value.final_value,
                    value.like_search,
                )
            )
        return constraint_array_element(items)  # type:ignore

    def get_dataset(
        self,
        *,
        company_id: str,
        user_name: str,
        password: str,
        dataset_name: str,
        constraints: list[DatasetQueryParams],
        fields: Optional[list] = None,
        order: Optional[list] = None,
    ) -> Optional[List[dict]]:

        try:
            self._logger.attribute.info("Start request dataset")

            list_fields = []
            list_order = []
            list_constraints = []

            if constraints:

                for constraint_item in constraints:
                    list_constraints.append(
                        StructConstraint(
                            constraint_type=constraint_item.type,
                            field_name=constraint_item.field_name,
                            init_value=constraint_item.value,
                            final_value=constraint_item.value,
                        )
                    )

            if fields:
                for item in fields:
                    list_fields.append(StructField(item=item))

            if order:
                for item in order:
                    list_order.append(StructOrder(item=item))

            dataset = DatasetQuery(
                company_id=company_id,
                user_name=user_name,
                password=password,
                dataset_name=dataset_name,
                constraints=list_constraints,
                fields=list_fields,
                order=list_order,
            )

            query_result = self._client.soap_intance.service.getDataset(
                dataset.company_id,
                dataset.user_name,
                dataset.password,
                dataset.dataset_name,
                dataset.fields,
                self.__constraints(constraints=dataset.constraints),
                dataset.order,
            )

            if query_result:

                response = convert_zeep_object(query_result)

                serialize_result = []

                for value in response["values"]:  # type:ignore
                    items = {}
                    for k, v in zip(response["columns"], value["value"]):  # type:ignore
                        items.update({k: v})

                    serialize_result.append(items)

                self._logger.attribute.info("Finish request dataset success")
                return serialize_result

            else:
                self._logger.attribute.warning("Response Dataset is empty")
                return []

        except Exception as error:
            self._logger.attribute.error(error)

    def get_all_available_dataset(self, *, company_id: str, user_name: str, password: str) -> Optional[List[dict]]:

        try:
            self._logger.attribute.info("Request all Datasets Available")

            query = self._client.soap_intance.service.findAllFormulariesDatasets(
                company_id,
                user_name,
                password,
            )

            response = convert_zeep_object(query)
            serialize_result = []

            if response:

                for value in response:  # type:ignore

                    serialize_result.append(value)

                return serialize_result

            else:
                return []

        except Exception as error:
            self._logger.attribute.error(error)

    def get_available_datasets(self, *, company_id: str, user_name: str, password: str) -> Optional[List[dict]]:

        try:

            self._logger.attribute.info("Request dataset built in available")

            query = self._client.soap_intance.service.getAvailableDatasets(
                company_id,
                user_name,
                password,
            )

            response = convert_zeep_object(query)

            if response:

                serialize_result = []

                for value in response:  # type:ignore
                    items = {}  # type:ignore
                    items.update({"dataset_name": value})

                    serialize_result.append(items)

                return serialize_result

            else:
                return []

        except Exception as error:
            self._logger.attribute.error(error)

    def disable_dataset(self, *, company_id: str, user_name: str, password: str, dataset_name: str) -> None:

        self._logger.attribute.info(f"Disable dataset {dataset_name}")

        return self._client.soap_intance.service.deleteDataset(
            company_id,
            user_name,
            password,
            dataset_name,
        )
