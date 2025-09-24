from sqlalchemy import Column, Integer, String, CHAR, Enum as SqlEnum, Date, Numeric, Computed
from ..database import Base
import enum

class Parcelado(enum.Enum):
    SIM = "SIM"
    NAO = "NAO"

class Operacao(enum.Enum):
    OGV = "OGV"
    IGV = "IGV"

class EP(Base):
    __tablename__ = "eps"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(CHAR(11), nullable=False)
    nome = Column(String(255), nullable=False)
    pais_origem = Column(String(255), nullable=False)
    pais_destino = Column(String(255), nullable=False)
    id_operacao = Column(Integer, nullable=False)
    parcelado = Column(SqlEnum(Parcelado, name="parcelado_enum"), nullable=False)
    data_vencimento = Column(Date, nullable=False)
    qtd_parcelas_total = Column(Integer, nullable=False)
    qtd_parcelas_pendentes = Column(
        Integer,
        Computed("qtd_parcelas_total - 1", persisted=True)  # STORED no MySQL
    )
    valor_total = Column(Numeric(10, 2), nullable=False)
    desconto_oferecido = Column(Numeric(10, 2), nullable=False)
    valor_com_desconto = Column(Numeric(10, 2), nullable=False)
