
from ariaria.domain.models.account import Account
from ariaria.dao.abstract_dao import AbstractDao


class AccountDao(AbstractDao):
    def __init__(self, session):
        self.session = session

    def add(self, account):
        self.session.add(account)
        

    def update(self, account):
        pass
    
    def delete(self, account):
        pass

    def get(self, reference):
        return self.session.query(Account).filter_by(id=reference).one()

    def list(self):
        return self.session.query(Account).all()

    def find(self, search_params):
        pass