class DataOrdersCode:

    SUCCESSFUL_ORDER_CREATION_CODE = 201
    SUCCESSFUL_CANCEL_ORDER = 200
    
    SUCCESSFUL_LIST_ORDERS = 200



class DataOrdersBody:

    OK_TRUE = {"ok": True}

    ORDER_BODY_TEMPLATE = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }


def non_existent_courier_body():
    return {
        "login": "Uchiha",
        "password": "Haringan",
        "firstName": "Saske"
    }