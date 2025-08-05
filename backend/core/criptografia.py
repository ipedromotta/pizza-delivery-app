import bcrypt


class Criptografia:

    @staticmethod
    def criptografar(senha: str) -> str | bool:
        try:
            senha_bytes = senha.encode()
            salt = bcrypt.gensalt()
            hash_senha = bcrypt.hashpw(senha_bytes, salt)
            return hash_senha.decode()
        except Exception as e:
            return False

    @staticmethod
    def verificar_senha(senha: str, hash_senha: str) -> bool:
        try:
            return bcrypt.checkpw(senha.encode(), hash_senha.encode())
        except Exception as e:
            return False
