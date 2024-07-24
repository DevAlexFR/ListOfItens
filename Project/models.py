from sqlalchemy import create_engine, Column, Integer, String, Float
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
    quantidade = Column(Float())

    @staticmethod # Define como estático! Porque ele não depende de nenhuma instância específica da classe para ser chamado e executado.
    def create_session() -> sessionmaker:
        """ Função de criação de sessão.

        Returns
        -------
        sessionmaker
            Retorna uma sessão de com o banco de dados relacional SQLite.
        """
        engine = create_engine(CONN, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

Base.metadata.create_all(engine)
