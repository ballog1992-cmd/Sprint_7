class DataRequestCode:

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class DataRequestBody:

    OK_TRUE = {"ok": True}

    
    CREATE_COURIER_DATA = "Недостаточно данных для создания учетной записи"
    CREATE_DUPLICATE_LOGIN = "Этот логин уже используется"
    
    
    LOGIN_COURIER_DATA = "Недостаточно данных для входа"
    LOGIN_NOT_FOUND = "Учетная запись не найдена"
    
    
    DELETE_COURIER_ID = "Недостаточно данных для удаления курьера"
    DELETE_NOT_FOUND = "Курьера с таким id нет"