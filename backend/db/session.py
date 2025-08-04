from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker


class Session:
    __engine = None
    __session = None

    @classmethod
    def _initialize(cls):
        try:
            if cls.__engine is None:
                cls.__engine = create_engine(
                    "sqlite:///banco.db",
                    poolclass=QueuePool,
                    pool_size=5,
                    max_overflow=10,
                    pool_pre_ping=True,
                    echo=False,  # Opcional: mostra logs SQL
                    )
                cls.__session = sessionmaker(bind=cls.__engine)
                
                # Base.metadata.create_all(cls.__engine) # Essa linha cria as tabelas automaticamente. Comentado pois agora é feito pela biblioteca alembic
                
        except Exception as e:
            print(e)

    @classmethod
    def get_session(cls):
        cls._initialize()
        return cls.__session()
    