import hashlib
import os
import base64

def gerar_salt() -> str:
    return base64.urlsafe_b64encode(os.urandom(24)).decode()

def hash_senha(senha: str, salt: str) -> str:
    return hashlib.sha256(f"{senha}{salt}".encode()).hexdigest()

def verificar_senha(senha: str, salt: str, hash_armazenado: str) -> bool:
    return hash_senha(senha, salt) == hash_armazenado
