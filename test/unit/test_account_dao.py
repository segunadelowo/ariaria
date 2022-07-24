from enum import IntEnum
import pytest
from ariaria.domain.models.account import Account
from ariaria.dao.account_dao import AccountDao
from ariaria.utils.enums import AccountStatus



def test_repository_can_save_an_account(session):
    acct = Account(1,'testuser','vghvhgvghvgh','test_name1','test_email.com','09090909','989 khjhhkkh kkh yyuyuyuu', AccountStatus.UNKNOWN.value)

    repo = AccountDao(session)
    repo.add(acct)
    session.commit()

    rows = session.execute(
        'SELECT id, email, phone FROM "accounts"'
    )
    assert list(rows) == [(1, "test_email.com", '09090909')]