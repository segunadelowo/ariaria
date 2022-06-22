class Item:
      def __init__(self, id, quantity, price):
        self.__product_id = id
        self.__quantity = quantity
        self.__price = price

      def update_quantity(self, quantity):
        None