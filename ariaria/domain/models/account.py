from util.enums import AccountStatus

class Account:
      def __init__(self, id,user_name, password, name, email, phone, shipping_address, status=AccountStatus.UNKNOWN):
        self.__id = 0
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__shipping_address = shipping_address
        self.__status = status.ACTIVE
        self.__credit_cards = []
        self.__bank_accounts = []