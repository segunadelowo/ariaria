import pytest
from ariaria.domain.models.account import Account
from ariaria.repositories.abstract_repository import AbstractRepository
from ariaria.util.enums import AccountStatus



class AccountRepository(AbstractRepository):
    def __init__(self, accounts):
        self._accounts = set(accounts)

    def add(self, account):
        self._accounts.add(account)

    def get(self, reference):
        return next(b for b in self._accounts if b.id == reference)

    def list(self):
        return list(self._accounts)


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_add_account():
    repo, session = AccountRepository([]), FakeSession()
    repo.add(Account(1,'testuser','vghvhgvghvgh','test_name1','test_email.com','09090909','989 khjhhkkh kkh yyuyuyuu',AccountStatus.UNKNOWN))
    #services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, repo, session)
    assert repo.get(1) is not None
    assert session.committed