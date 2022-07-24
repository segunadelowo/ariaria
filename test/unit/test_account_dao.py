from enum import IntEnum
import pytest
from ariaria.domain.models.account import Account
from ariaria.dao.account_dao import AccountDao
from ariaria.utils.enums import AccountStatus



def test_raccountdao_can_save_an_account(session):
    acct = Account(1,'testuser','vghvhgvghvgh','test_name1','test_email.com','09090909','989 khjhhkkh kkh yyuyuyuu', AccountStatus.UNKNOWN.value)

    repo = AccountDao(session)
    repo.add(acct)
    session.commit()

    rows = session.execute(
        'SELECT id, email, phone FROM "accounts"'
    )
    assert list(rows) == [(1, "test_email.com", '09090909')]


def test_accountdao_can_get_account(session):
   
    session.execute(
        "INSERT INTO accounts (id, 'user_name', 'password', 'name', 'email', 'phone', 'shipping_address', 'status')"
        " VALUES (1,'testuser','vghvhgvghvgh','test_name1','test_email.com','09090909','989 khjhhkkh kkh yyuyuyuu', 6)"
    )

    repo = AccountDao(session)
    acct  = repo.get(1)

    assert acct.user_name == 'testuser'