from pathlib import Path
import shutil, os, stat

# Define a pasta onde os arquivos estão e a pasta que vai receber as cópias.
caminho_origem = Path(r'C:\Users\Mateus\Downloads')
caminho_destino = Path(r'C:\OrganizadorTeste')

# Relaciona cada extensão com o nome da pasta correspondente.
extensao = {".zip" : "Compactados", ".pdf" : "PDFs", ".txt" : "Arquivos de Texo", ".png" : "Imagens"}

# Cria uma lista com as pastas das extensões e adiciona uma pasta para outros tipos.
pastas = list(extensao.values())
pastas.append("Outros")

# Cria as pastas de destino caso elas ainda não existam.
for nova_pasta in pastas:
    caminho_completo = caminho_destino / nova_pasta
    caminho_completo.mkdir(exist_ok=True)

# Percorre tudo o que existe dentro da pasta de origem.
for arquivo in caminho_origem.iterdir():
    # Lê os atributos do arquivo para descobrir se ele está oculto ou é do sistema.
    info_arquivo = os.stat(arquivo)
    atributos = getattr(info_arquivo, "st_file_attributes", 0)

    # Verifica se o arquivo tem o atributo de oculto ou de arquivo do sistema.
    eh_oculto_ou_sistema = bool(atributos & stat.FILE_ATTRIBUTE_HIDDEN or atributos & stat.FILE_ATTRIBUTE_SYSTEM)

    # Só organiza arquivos normais; pastas e arquivos ocultos são ignorados.
    if arquivo.is_file() and not eh_oculto_ou_sistema:
        # Escolhe a pasta pela extensão ou usa "Outros" quando não houver correspondência.
        pasta_arquivo = extensao.get(arquivo.suffix, "Outros")

        # Monta o caminho final mantendo o nome original do arquivo.
        destino = caminho_destino / pasta_arquivo / arquivo.name

        # Exibe o arquivo atual e copia ele para a pasta escolhida.
        print("Processando:", arquivo)
        shutil.copy(arquivo, destino)



        
