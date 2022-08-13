
from typing import Iterable
from dataclasses import dataclass

@dataclass
class Account:
      id: int
      user_name: str 
      password: str
      name: str 
      email: str
      phone: str 
      shipping_address: str
      status: int
      credit_cards: Iterable
      bank_accounts: Iterable
     