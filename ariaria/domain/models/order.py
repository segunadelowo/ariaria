import datetime

from ariaria.util.enums import OrderStatus


class Order:
      def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = 0
        self.__status = status
        self.__order_date = datetime.date.today()
        self.__order_log = []

      def send_for_shipment(self):
        None

      def make_payment(self, payment):
        None

      def add_order_log(self, order_log):
        None