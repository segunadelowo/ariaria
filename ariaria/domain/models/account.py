from ariaria.utils.enums import AccountStatus

class Account:
      def __init__(self,id, user_name, password, name, email, phone, shipping_address, status=AccountStatus.UNKNOWN):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.shipping_address = shipping_address
        self.status = status
        self.credit_cards = []
        self.bank_accounts = []