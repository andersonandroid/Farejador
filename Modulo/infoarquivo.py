import pathlib
from datetime import datetime
import hashlib

def Getsha256File(arquivo):
    try:
        hashsha = hashlib.sha256()
        with open(arquivo, "rb") as f:
            for a in iter(lambda: f.read(4096), b""):
                hashsha.update(a)
        return hashsha.hexdigest()

    except Exception as e:
        print("Erro: %s" % (e))
        return ""
    except:
        print("Erro desconhecido")
        return ""

def InfoArquivo(arquivo):

    try:

        infoarquivo = arquivo.stat()
        ultimo_acesso = infoarquivo.st_atime
        ultima_alteracao = infoarquivo.st_mtime
        data_criacao = infoarquivo.st_ctime
        infoacesso = datetime.fromtimestamp(ultimo_acesso)
        infoalteracao = datetime.fromtimestamp(ultima_alteracao)
        infocriacao = datetime.fromtimestamp(data_criacao)

    except Exception as e:
        print("Erro" % (e))

    return infoacesso, infoalteracao, infocriacao

if __name__ == "__main__":
    