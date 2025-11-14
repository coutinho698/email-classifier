def generate_response(label):
    if label is None:
        return "Recebemos sua mensagem e estamos analisando. Em breve retornaremos."

    label = str(label).strip().lower()

    if label == "produtivo":
        return (
            "Olá,\n\n"
            "Obrigado pelo seu contato. Recebemos a sua solicitação e ela já foi encaminhada para análise.\n"
            "Caso tenha número de protocolo, contrato ou ticket, por favor responda este e-mail informando esses dados "
            "para agilizar o atendimento.\n\n"
            "Atenciosamente,\n"
            "Equipe de Atendimento"
        )
    elif label == "improdutivo":
        return (
            "Olá,\n\n"
            "Muito obrigado pela sua mensagem! 😊\n"
            "Agradecemos o contato e ficamos à disposição sempre que precisar.\n\n"
            "Atenciosamente,\n"
            "Equipe de Atendimento"
        )
    else:
        return (
            "Olá,\n\n"
            "Recebemos a sua mensagem e estamos analisando internamente. "
            "Se necessário, entraremos em contato com você em breve.\n\n"
            "Atenciosamente,\n"
            "Equipe de Atendimento"
        )
