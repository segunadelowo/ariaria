import datetime


class Shipment:
      def __init__(self, shipment_number, shipment_method):
        self.__shipment_number = shipment_number
        self.__shipment_date = datetime.date.today()
        self.__estimated_arrival = datetime.date.today()
        self.__shipment_method = shipment_method
        self.__shipmentLogs = []

      def add_shipment_log(self, shipment_log):
       None
