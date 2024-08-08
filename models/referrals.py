from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Referral(Base):
    __tablename__ = 'referrals'

    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer, ForeignKey('users.telegram_id'))
    referred_id = Column(Integer, ForeignKey('users.telegram_id'))

    referrer = relationship("User", foreign_keys=[referrer_id], back_populates="referrals_given")
    referred = relationship("User", foreign_keys=[referred_id], back_populates="referrals_received")

    def __init__(self, referrer_id, referred_id):
        self.referrer_id = referrer_id
        self.referred_id = referred_id