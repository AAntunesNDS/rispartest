import sys
from service import ServiceBank

if __name__ == "__main__":
    print('### Atualizando saldo das contas ###\n')
    response = ServiceBank(str(sys.argv[1]), str(sys.argv[2]))
    response.run_service()
    print(response.__str__())
    print('\nCSV atualizado e encontrado em: data/contas_update.csv')