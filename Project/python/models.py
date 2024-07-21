from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Produto(Base):
    __tablename__ = "Produto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    preco = Column(Float())

    def create_session():
        CONN = "sqlite:///projeto2.db"

        engine = create_engine(CONN, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
        
Base.metadata.create_all(engine)
