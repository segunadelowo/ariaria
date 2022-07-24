class Product:
      def __init__(self, id, name, description, price, category, seller_account):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__available_item_count = 0
        self.__seller = seller_account