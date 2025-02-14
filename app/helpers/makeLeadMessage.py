from datetime import datetime
from app.services import getLeadById, getUserById, getContactById, getCompanyById
from app.helpers import arrFind, arrGet
from app.config import CRM_BASE_URL


async def makeLeadMessage(leadId: int):
    lead = await getLeadById(leadId)
    user = await getUserById(lead["responsible_user_id"])

    custom_fields = lead.get("custom_fields_values", []) or []
    # contacts = lead.get("_embedded", {}).get("contacts", []) or []
    # companies = lead.get("_embedded", {}).get("companies", []) or []

    # contacts = [await getContactById(contact["id"]) for contact in contacts]
    # companies = [await getCompanyById(company["id"]) for company in companies]

    new_value = _getValue(custom_fields, "Новый")
    source_value = _getValue(custom_fields, "Источник")
    calls_value = _getValue(custom_fields, "С какого кол-ва звонков продано")
    product_value = _getValue(custom_fields, "Продукт")
    name_value = _getValue(custom_fields, "Ф.И.О")
    industry_value = _getValue(custom_fields, "Отрасль")
    region_value = _getValue(custom_fields, "Регион")
    phone_value = _getValue(custom_fields, "Телефон")
    plan_value = _getValue(custom_fields, "Тариф")
    contractNum_value = _getValue(custom_fields, "Договор №")
    contractDate_value = _getValue(custom_fields, "Дата договора")
    contractAmount_value = _getValue(custom_fields, "Сумма по договору")
    paymentDate_value = _getValue(custom_fields, "Дата оплаты")
    paymentAmount_value = _getValue(custom_fields, "Сумма платежа")
    debit_value = _getValue(custom_fields, "Дебиторка")
    paymentType_value = _getValue(custom_fields, "Вид платежа")
    # cancelReason_value = _getValue(custom_fields, "Причина отказа")

    contractDate = contractDate_value and datetime.fromtimestamp(contractDate_value).strftime("%d.%m.%Y")
    paymentDate = paymentDate_value and datetime.fromtimestamp(paymentDate_value).strftime("%d.%m.%Y")

    leadTime = datetime.now().strftime("%d.%m.%Y %H:%M")
    text = f"<b>Время</b>: {leadTime}\n\n"

    leadLink = CRM_BASE_URL + f"leads/detail/{lead['id']}"
    text += f'<b>Сделка</b>: <a href="{leadLink}">{lead["name"]}</a>\n\n'

    text += f"<b>Отв-ный</b>: {user['name'] or ''}\n"
    text += f"<b>Бюджет</b>: {lead['price'] or ''}\n"

    text += f"<b>Новый</b>: \n" if new_value is None else f"<b>Новый</b>: {'Да' if new_value else 'Нет'}\n"
    text += f"<b>Источник</b>: {source_value or ''}\n"
    text += f"<b>Кол-во звонков продано</b>: {calls_value or ''}\n"
    text += f"<b>Продукт</b>: {product_value or ''}\n"
    text += f"<b>Ф.И.О</b>: {name_value or ''}\n"
    text += f"<b>Отрасль</b>: {industry_value or ''}\n"
    text += f"<b>Регион</b>: {region_value or ''}\n"
    text += f"<b>Телефон</b>: {phone_value or ''}\n"
    text += f"<b>Тариф</b>: {plan_value or ''}\n"
    text += f"<b>Договор №</b>: {contractNum_value or ''}\n"
    text += f"<b>Дата договора</b>: {contractDate or ''}\n"
    text += f"<b>Сумма по договору</b>: {contractAmount_value or ''}\n"
    text += f"<b>Дата оплаты</b>: {paymentDate or ''}\n"
    text += f"<b>Сумма платежа</b>: {paymentAmount_value or ''}\n"
    text += f"<b>Дебиторка</b>: {debit_value or ''}\n"
    text += f"<b>Вид платежа</b>: {paymentType_value or ''}\n"
    # text += f"<b>Причина отказа</b>: {cancelReason_value or ''}\n\n"

    # for contact in contacts:
    #     custom_fields = contact.get("custom_fields_values", []) or []

    #     phone_value = _getValue(custom_fields, "Телефон")
    #     email_value = _getValue(custom_fields, "Email")
    #     position_value = _getValue(custom_fields, "Должность")

    #     contactLink = CRM_BASE_URL + f"contacts/detail/{contact['id']}"
    #     text += f'<b>Контакт</b>: <a href="{contactLink}">{contact['name']}</a>\n\n'

    #     text += f"<b>Телефон</b>: {phone_value or ''}\n"
    #     text += f"<b>Email</b>: {email_value or ''}\n"
    #     text += f"<b>Должность</b>: {position_value or ''}\n\n"

    # for company in companies:
    #     custom_fields = company.get("custom_fields_values", []) or []

    #     phone_value = _getValue(custom_fields, "Телефон")
    #     email_value = _getValue(custom_fields, "Email")
    #     web_value = _getValue(custom_fields, "Web")
    #     address_value = _getValue(custom_fields, "Адрес")

    #     companyLink = CRM_BASE_URL + f"companies/detail/{company['id']}"
    #     text += f'<b>Компания</b>: <a href="{companyLink}">{company['name']}</a>\n\n'

    #     text += f"<b>Телефон</b>: {phone_value or ''}\n"
    #     text += f"<b>Email</b>: {email_value or ''}\n"
    #     text += f"<b>Web</b>: {web_value or ''}\n"
    #     text += f"<b>Адрес</b>: {address_value or ''}\n\n"

    return text.strip()


def _getValue(custom_fields: list, field_name: str):
    field = arrFind(custom_fields, lambda field: field["field_name"] == field_name, {})
    return arrGet(field.get("values", []) or [], 0, {}).get("value")
