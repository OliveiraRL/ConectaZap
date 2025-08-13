from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem
from utils.formatters import formatar_mensagem


def main():
    pessoas = buscar_contatos()

    if not pessoas:
        print("Nenhuma pessoa encontrada.")
        return

    for pessoa in pessoas:
        nome = pessoa.get("name")
        telefone = pessoa.get("telephone")

        if not telefone:
            print(f"⚠️ Contato {nome} sem telefone. Pulando...")
            continue

        mensagem = formatar_mensagem(nome)
        status, resposta = enviar_mensagem(telefone, mensagem)

        if status == 200:
            print(f"✅ Mensagem enviada para {nome}")
        else:
            print(f"❌ Erro ao enviar para {nome}: {resposta}")


if __name__ == "__main__":
    main()

