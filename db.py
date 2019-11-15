from sqlalchemy import Column, Integer, create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///bomber_data.db', connect_args={'check_same_thread': False})

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    spam_balance = Column(Float)
    tg_id = Column(Integer)
    payment_comment = Column(Integer)

    def __repr__(self):
        return 'Client telegram_id:{} spam balance:{} spam_on:{}'.format(self.tg_id, self.spam_balance, self.spam_on)

    def decrease_money(self, money, session):
        if self.spam_balance >= money:
            self.spam_balance -= money
            self.spam_balance = round(self.spam_balance, 2)
            print(self.spam_balance)
            session.commit()


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
