from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String)
    chat_id = Column(Integer)
    balance = Column(Float)
    referral_code = Column(String)

    referrals_given = relationship("Referral", foreign_keys='Referral.referrer_id', back_populates="referrer")

    # Отношение к модели Referral для получения всех реферралов, перешедших по ссылке данного пользователя
    referrals_received = relationship("Referral", foreign_keys='Referral.referred_id', back_populates="referred")

    def __init__(self, telegram_id, username='', chat_id=0, balance=0, referral_code=''):
        self.telegram_id = telegram_id
        self.balance = balance
        self.username = username
        self.referral_code = referral_code
        self.chat_id = chat_id
