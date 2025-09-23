from sqlalchemy.orm import Session
from ..schemas import UserCreate
from ..utils import gerar_salt, hash_senha
from .user_service import UserService
from .area_service import AreaService
from .cargo_service import CargoService
from .contato_service import ContatoService
from .credencial_service import CredencialService
from .perfil_service import PerfilService


class CentralService:
    def __init__(self, db: Session):
        self.user_service = UserService(db)
        self.area_service = AreaService(db)
        self.cargo_service = CargoService(db)
        self.contato_service = ContatoService(db)
        self.credencial_service = CredencialService(db)
        self.perfil_service = PerfilService(db)
        self.db = db

    # -----------------------
    # CRUD COMPLETO
    # -----------------------
    def cadastrar_usuario_completo(self, user_create: UserCreate):
        # Criar usuário básico
        usuario = self.user_service.criar_usuario(user_create)

        # Validar entidades relacionadas
        area = self.area_service.buscar_por_sigla(user_create.area)
        cargo = self.cargo_service.buscar_por_sigla(user_create.cargo)
        if not area or not cargo:
            raise ValueError("Área ou cargo inválidos")

        # Adicionar dados relacionados
        self.contato_service.criar_contato(usuario.id, user_create.email)

        self.credencial_service.criar_credencial(usuario.id, user_create.login, user_create.senha)

        self.perfil_service.criar_perfil(usuario.id, area.id, cargo.id)

        self.db.commit()
        self.db.refresh(usuario)

        return {
            "mensagem":"Cadastro Realizado com Sucesso\nAguarde Aprovação de um superior",
            "usuario": usuario
        }

    def listar_usuarios_completo(self):
        """
        Lista todos os usuários com dados relacionados.
        """
        usuarios = self.user_service.listar_usuarios()
        return usuarios

    def deletar_usuario_completo(self, user_id: int):
        """
        Deleta usuário e seus relacionamentos.
        """
        # Deletar entidades relacionadas primeiro
        self.contato_service.deletar_por_user_id(user_id)
        self.credencial_service.deletar_por_user_id(user_id)
        self.perfil_service.deletar_por_user_id(user_id)

        # Deletar usuário
        usuario = self.user_service.deletar_usuario(user_id)
        self.db.commit()
        return usuario

    def atualizar_usuario_completo(self, user_id: int, user_update: UserCreate):
        """
        Atualiza dados do usuário e relacionados.
        """
        # Atualizar dados básicos do usuário
        usuario = self.user_service.atualizar_usuario(user_id, user_update)

        # Atualizar contato
        self.contato_service.atualizar_contato(user_id, user_update.email)

        # Atualizar credencial
        salt = gerar_salt()
        senha_hash = hash_senha(user_update.senha, salt)
        self.credencial_service.atualizar_credencial(user_id, user_update.login, senha_hash, salt)

        # Atualizar perfil (área e cargo)
        area = self.area_service.buscar_por_sigla(user_update.area)
        cargo = self.cargo_service.buscar_por_sigla(user_update.cargo)
        if not area or not cargo:
            raise ValueError("Área ou cargo inválidos")

        self.perfil_service.atualizar_perfil(user_id, area.id, cargo.id)

        self.db.commit()
        self.db.refresh(usuario)
        return usuario
