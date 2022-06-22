import datetime
from ariaria.util.enums import OrderStatus


class OrderLog:
      def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = order_number
        self.__creation_date = datetime.date.today()
        self.__status = status