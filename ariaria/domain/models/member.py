from ariaria.domain.models.customer import Customer


class Member(Customer):
      def __init__(self, account):
        self.__account = account

      def place_order(self, order):
        None