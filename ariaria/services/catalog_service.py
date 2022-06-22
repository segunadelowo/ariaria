from ariaria.services.search_service import SearchService


class CatalogService(SearchService):
      def __init__(self):
        self.__product_names = {}
        self.__product_categories = {}

      def search_products_by_name(self, name):
          return self.product_names.get(name)

      def search_products_by_category(self, category):
          return self.product_categories.get(category)