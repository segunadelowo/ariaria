import datetime

from ariaria.util.enums import ShipmentStatus


class ShipmentLog:
      def __init__(self, shipment_number, status=ShipmentStatus.PENDING):
        self.__shipment_number = shipment_number
        self.__status = status
        self.__creation_date = datetime.date.today()