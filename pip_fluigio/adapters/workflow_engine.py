from pip_fluigio.__fluig_services_base.interfaces.workflow_engine import (
    Attachment, Colleagues, Item, ItemAttachments)


class WorkflowProperties:
    @classmethod
    def set_colleagues(cls, colleagues: list[str]):

        list_colleagues = []
        for colleague in colleagues:
            list_colleagues.append(Colleagues(item=colleague))

        return list_colleagues

    @classmethod
    def set_items(cls, data: dict):
        list_items = []
        for key, value in data.items():
            list_items.append(Item(key=key, value=value))

        return list_items

    @classmethod
    def set_attachments(
        cls,
        file_name: str,
        file_size: str,
        file_content: str,
        description: str,
        document_type: str,
        company_id: str,
        process_instance_id: int,
    ):

        attach = Attachment(
            attach="true",
            editing="true",
            fileName=file_name,
            fileSize=file_size,
            filecontent=file_content,
            principal="true",
        )

        return ItemAttachments(
            attachmentSequence=22,
            attachments=attach,
            colleagueId="",
            colleagueName="",
            companyId=company_id,
            deleted="false",
            description=description,
            documentType=document_type,
            newAttach="true",
            processInstanceId=process_instance_id,
            size=file_size,
        )
