import openai

# Configurações do OpenAI API
openai.api_key = 'ADICIONE A CHAVE AQUI'
engine = "gpt-4o"  # Modelo GPT-4

# Função para ler documentos .docx e converter para texto
def ler_documento(docx_file):
    texto = '''CavData: Liderando o Futuro da Análise de Dados

Fundada em 2023, a CavData é uma empresa que se destaca no cenário tecnológico como uma líder inovadora em análise de dados e inteligência artificial. Com sede em uma metrópole vibrante, nossa equipe diversificada e altamente qualificada está empenhada em fornecer soluções personalizadas e de ponta para uma ampla gama de setores, desde finanças até saúde e varejo.

Nossa missão é simples: capacitar empresas e organizações a tomarem decisões mais informadas e estratégicas por meio da análise inteligente de dados. Acreditamos que os dados são o ativo mais valioso de qualquer empresa e, quando aproveitados corretamente, têm o poder de transformar completamente a maneira como os negócios são conduzidos.

Na CavData, adotamos uma abordagem holística para a análise de dados, combinando técnicas avançadas de ciência de dados e aprendizado de máquina com uma compreensão profunda das necessidades exclusivas de cada cliente. Nossa equipe de especialistas em dados trabalha em estreita colaboração com os clientes para entender seus desafios e objetivos específicos, desenvolvendo soluções personalizadas que impulsionam o crescimento, a eficiência e a inovação.

Oferecemos uma ampla gama de serviços, incluindo análise preditiva, modelagem estatística, mineração de dados, visualização de dados e muito mais. Além disso, nossa plataforma proprietária de inteligência artificial, CavAI, permite que os clientes automatizem processos complexos, identifiquem padrões ocultos nos dados e prevejam tendências futuras com precisão sem precedentes.

Na CavData, estamos comprometidos não apenas em fornecer soluções tecnológicas de ponta, mas também em oferecer um serviço excepcional ao cliente. Acreditamos em construir relacionamentos sólidos e de longo prazo com nossos clientes, baseados na confiança, transparência e resultados tangíveis.

À medida que continuamos a avançar rumo ao futuro da análise de dados, na CavData, estamos prontos para enfrentar os desafios mais complexos e empolgantes que o mundo dos negócios tem a oferecer. Junte-se a nós nesta jornada emocionante enquanto transformamos dados em insights e insights em impacto tangível. CavData: liderando o futuro da análise de dados, um byte de cada vez.
A CavData possui mais de 1 milhão de faturamento anual'''
    return texto

# Função para interagir com o modelo GPT-4 e obter uma resposta
def obter_resposta(pergunta, contexto, max_tokens=50):
    resposta = openai.ChatCompletion.create(
        model=engine,
        messages=[
            {"role": "user", "content": pergunta},
            {"role": "system", "content": contexto}
        ],
        max_tokens=max_tokens
    )
    return resposta.choices[0].message['content']

# Exemplo de uso
def main():
    # Ler documentos .docx e converter para texto
    contexto = ler_documento(None)  # Nenhuma necessidade de arquivo neste exemplo

    # Loop contínuo até que a mensagem digitada seja "SAIR"
    while True:
        # Pergunta do usuário
        pergunta = input("Faça uma pergunta (Digite SAIR para encerrar o chat): ")

        # Verificar se a mensagem é "SAIR"
        if pergunta.upper() == "SAIR":
            print("Chat encerrado.")
            break

        # Obter resposta usando o modelo GPT-4
        resposta = obter_resposta(pergunta, contexto)

        # Exibir resposta
        print("Resposta do bot:", resposta)

if __name__ == "__main__":
    main()
