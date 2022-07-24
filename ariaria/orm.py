from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship

import ariaria.domain.models
from ariaria.domain.models.account import Account


metadata = MetaData()

accounts = Table(
    "accounts",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_name", String(50)),
    Column("password", String(50), nullable=False),
    Column("name", String(50)),
    Column("email", String(50)),
    Column("phone", String(50)),
    Column("shipping_address", String(100)),
    Column("status", Integer, nullable=False),
)



def start_mappers():
    #lines_mapper = mapper(model.OrderLine, order_lines)
    mapper(
        Account,
        accounts,

    )