import Pyro4

@Pyro4.expose
class FileServer(object):
    def __init__(self):
        self.files = {}  # Dicionário para armazenar os arquivos disponíveis
        self.interests = {}  # Dicionário para armazenar os registros de interesse

    def upload_file(self, filename, filedata):
        self.files[filename] = filedata
        print(f"File '{filename}' uploaded successfully.")

    def get_file_info(self):
        return list(self.files.keys())  # Retorna uma lista com os nomes dos arquivos disponíveis

    def download_file(self, filename):
        if filename in self.files:
            return self.files[filename]  # Retorna o conteúdo do arquivo
        else:
            return None  # Arquivo não encontrado

    def register_interest(self, filename, client_reference, validity_period):
        if filename not in self.interests:
            self.interests[filename] = []
        self.interests[filename].append((client_reference, validity_period))
        print(f"Interest registered for file '{filename}' from client '{client_reference}' "
              f"valid for {validity_period} seconds.")

    def cancel_interest(self, filename, client_reference):
        if filename in self.interests:
            self.interests[filename] = [(ref, period) for ref, period in self.interests[filename]
                                        if ref != client_reference]
            print(f"Interest canceled for file '{filename}' from client '{client_reference}'.")
        else:
            print(f"No interests found for file '{filename}'.")

# Código para inicializar o servidor
daemon = Pyro4.Daemon()
uri = daemon.register(FileServer)

print("Ready. Object uri =", uri)
daemon.requestLoop()