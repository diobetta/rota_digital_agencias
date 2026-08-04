# Importando recursos do Flask
# Flask: cria a aplicação web
# render_template: chama os arquivos HTML da pasta templates
# request recebe: dados enviados por formulário
# session: guarda dados temporários enquanto o usuário navega
# redirect e url_for: ajudam a mudar de uma rota para outra

from flask import Flask, render_template, request, session, redirect, url_for

# Criando a aplicação Flask
app = Flask(__name__)

# Chave usada pelo Flask para trabalhar com session

app.secret_key = "rota_digital_agencias"

# Modelagem simples de dados em Python 
# Lista de perguntas do diagnóstico
# Perguntas = Lista que guarda todas as perguntas
# Cada pergunta possui:
# - id: identificação da pergunta
# - area: área avaliada
# - texto: pergunta exibida ao usuário
# - criterios: explicação qualitativa para cada resposta

# A pontuação não aparece para o usuário durante o questionário
perguntas = [
    {
        "id": "q1",
        "area": "Atendimento / Vendas",
        "texto": "A agência registra por qual canal cada cliente chegou?",
        "criterios": {
            "nao": "A agência não registra origem do cliente ou depende apenas da memória da equipe.",
            "parcialmente": "A origem é percebida informalmente, mas não existe registro padronizado ou consulta fácil.",
            "sim": "A origem do cliente é registrada de forma organizada, como WhatsApp, Instagram, indicação, site, telefone ou outro canal."
        }
    },
    {
        "id": "q2",
        "area": "Atendimento / Vendas",
        "texto": "Existe um roteiro mínimo de perguntas para entender o perfil da viagem antes de montar a proposta?",
        "criterios": {
            "nao": "Cada atendimento acontece de um jeito e as informações são coletadas sem padrão.",
            "parcialmente": "Alguns atendentes fazem perguntas parecidas, mas não existe roteiro definido ou registrado.",
            "sim": "Existe um conjunto mínimo de perguntas sobre destino, datas, orçamento, perfil, passageiros, preferências e restrições."
        }
    },
    {
        "id": "q3",
        "area": "Atendimento / Vendas",
        "texto": "Os atendimentos são organizados por status, como novo contato, em cotação, proposta enviada, aguardando retorno, fechado ou perdido?",
        "criterios": {
            "nao": "A agência não sabe claramente em que etapa cada cliente está.",
            "parcialmente": "Alguns clientes são acompanhados manualmente, mas sem status padronizado.",
            "sim": "Os atendimentos possuem status definidos e são acompanhados em planilha, sistema, CRM ou ferramenta equivalente."
        }
    },
    {
        "id": "q4",
        "area": "Atendimento / Vendas",
        "texto": "Existe uma rotina de follow-up para clientes que receberam proposta e ainda não responderam?",
        "criterios": {
            "nao": "A agência envia proposta e espera o cliente retornar espontaneamente.",
            "parcialmente": "O follow-up acontece em alguns casos, mas depende da lembrança de cada pessoa.",
            "sim": "Existe prazo, rotina ou controle para retomar contato com clientes que ainda não responderam."
        }
    },
    {
        "id": "q5",
        "area": "Atendimento / Vendas",
        "texto": "O histórico do cliente fica registrado em algum lugar acessível?",
        "criterios": {
            "nao": "O histórico fica perdido em conversas, memória individual ou anotações soltas.",
            "parcialmente": "Existem registros, mas incompletos, espalhados ou difíceis de consultar.",
            "sim": "O histórico do cliente pode ser consultado de forma organizada por outras pessoas da equipe."
        }
    },
    {
        "id": "q6",
        "area": "Comercial",
        "texto": "A agência possui uma lista organizada de fornecedores, parceiros, operadoras, hotéis, receptivos ou prestadores usados com frequência?",
        "criterios": {
            "nao": "Os fornecedores são lembrados informalmente ou ficam espalhados em conversas e contatos pessoais.",
            "parcialmente": "Existe alguma lista, mas ela é incompleta, desatualizada ou não é usada por todos.",
            "sim": "Existe uma base organizada de fornecedores, com contatos e informações mínimas para consulta."
        }
    },
    {
        "id": "q7",
        "area": "Comercial",
        "texto": "As condições comerciais dos fornecedores ficam registradas, como comissão, prazo, regras, contatos e condições de cancelamento?",
        "criterios": {
            "nao": "As condições são consultadas caso a caso e dependem de troca de mensagens ou memória.",
            "parcialmente": "Algumas condições ficam registradas, mas sem padrão ou atualização frequente.",
            "sim": "As condições comerciais ficam registradas de forma consultável e atualizada."
        }
    },
    {
        "id": "q8",
        "area": "Comercial",
        "texto": "Existe um processo para atualizar produtos, pacotes, tarifários ou ofertas antes de repassar informações para atendimento/vendas?",
        "criterios": {
            "nao": "Produtos e preços são repassados sem conferência clara ou processo definido.",
            "parcialmente": "A atualização acontece, mas de forma manual, irregular ou concentrada em uma pessoa.",
            "sim": "Existe rotina para revisar e atualizar ofertas antes de serem usadas no atendimento ou em propostas."
        }
    },
    {
        "id": "q9",
        "area": "Comercial",
        "texto": "As informações negociadas pelo comercial chegam de forma clara para quem vende e para quem opera a viagem?",
        "criterios": {
            "nao": "Vendas e operação descobrem condições comerciais apenas quando precisam resolver um caso.",
            "parcialmente": "Algumas informações são repassadas, mas ainda há ruído, atraso ou falta de padrão.",
            "sim": "As condições negociadas são comunicadas de forma organizada para vendas e operação."
        }
    },
    {
        "id": "q10",
        "area": "Comercial",
        "texto": "A agência registra problemas recorrentes com fornecedores, como atrasos, divergências, baixa qualidade ou falhas de comunicação?",
        "criterios": {
            "nao": "Problemas com fornecedores são tratados caso a caso e não ficam registrados.",
            "parcialmente": "Alguns problemas são lembrados ou anotados, mas sem histórico organizado.",
            "sim": "A agência registra ocorrências recorrentes e usa essa informação para avaliar fornecedores."
        }
    },
    {
        "id": "q11",
        "area": "Operação",
        "texto": "Após a venda, existe um checklist para acompanhar o que precisa ser confirmado antes da viagem?",
        "criterios": {
            "nao": "Cada viagem é conduzida conforme a experiência de quem está operando.",
            "parcialmente": "Existe algum controle, mas incompleto, informal ou diferente para cada pessoa.",
            "sim": "Existe checklist mínimo para reservas, documentos, vouchers, confirmações, prazos e pendências."
        }
    },
    {
        "id": "q12",
        "area": "Operação",
        "texto": "A agência acompanha o status de reservas, confirmações, documentos, vouchers e pendências em algum lugar organizado?",
        "criterios": {
            "nao": "O controle fica espalhado em mensagens, e-mails ou memória individual.",
            "parcialmente": "Há registros, mas eles não cobrem todas as viagens ou não são atualizados com regularidade.",
            "sim": "A agência possui controle organizado e atualizado das principais pendências operacionais."
        }
    },
    {
        "id": "q13",
        "area": "Operação",
        "texto": "Existe conferência das informações principais antes do envio ao cliente, como nomes, datas, horários, serviços, contatos, valores e regras?",
        "criterios": {
            "nao": "A conferência depende da atenção individual e não possui etapa definida.",
            "parcialmente": "Algumas informações são conferidas, mas sem checklist ou padrão claro.",
            "sim": "Existe uma conferência mínima antes do envio de vouchers, propostas, confirmações ou orientações ao cliente."
        }
    },
    {
        "id": "q14",
        "area": "Operação",
        "texto": "A comunicação com fornecedores durante a operação fica registrada de forma acessível para a equipe?",
        "criterios": {
            "nao": "A comunicação fica presa no celular, e-mail ou WhatsApp de uma pessoa.",
            "parcialmente": "Parte da comunicação é registrada, mas nem sempre fica acessível para continuidade do atendimento.",
            "sim": "Informações relevantes com fornecedores ficam registradas e podem ser consultadas pela equipe."
        }
    },
    {
        "id": "q15",
        "area": "Operação",
        "texto": "Existe algum fluxo definido para lidar com problemas durante a viagem, como hotel, transfer, passeio, voo, atraso ou emergência?",
        "criterios": {
            "nao": "Problemas durante a viagem são resolvidos no improviso.",
            "parcialmente": "A equipe sabe quem acionar em alguns casos, mas não existe fluxo claro.",
            "sim": "Existe orientação mínima sobre prioridade, responsáveis e próximos passos em caso de problema em viagem."
        }
    },
    {
        "id": "q16",
        "area": "Dados",
        "texto": "A agência registra quantos contatos ou pedidos de orçamento recebe em determinado período?",
        "criterios": {
            "nao": "A agência não sabe o volume de demanda recebido.",
            "parcialmente": "Existe uma noção aproximada, mas sem registro confiável ou recorrente.",
            "sim": "A agência registra volume de contatos, pedidos de orçamento ou oportunidades em determinado período."
        }
    },
    {
        "id": "q17",
        "area": "Dados",
        "texto": "A agência acompanha quantas propostas foram enviadas, fechadas ou perdidas?",
        "criterios": {
            "nao": "A agência não acompanha conversão de propostas.",
            "parcialmente": "Algumas propostas são acompanhadas, mas sem rotina ou consolidação.",
            "sim": "A agência registra propostas enviadas, fechadas e perdidas, permitindo leitura de conversão."
        }
    },
    {
        "id": "q18",
        "area": "Dados",
        "texto": "A agência registra os principais motivos de perda de venda?",
        "criterios": {
            "nao": "A agência não registra por que as vendas são perdidas.",
            "parcialmente": "Alguns motivos são comentados ou anotados, mas não são consolidados.",
            "sim": "A agência registra motivos de perda de venda para analisar padrões e melhorar o processo."
        }
    },
    {
        "id": "q19",
        "area": "Dados",
        "texto": "A agência sabe quais destinos, produtos ou tipos de viagem são mais procurados pelos clientes?",
        "criterios": {
            "nao": "A agência decide com base apenas em percepção ou memória.",
            "parcialmente": "Existe percepção dos produtos mais procurados, mas sem registro organizado.",
            "sim": "A agência registra e consegue identificar destinos, produtos ou tipos de viagem mais demandados."
        }
    },
    {
        "id": "q20",
        "area": "Dados",
        "texto": "A agência registra problemas recorrentes por etapa do processo, como atendimento, comercial, fornecedor, documentação, reserva, operação ou pós-venda?",
        "criterios": {
            "nao": "Problemas recorrentes são tratados como casos isolados.",
            "parcialmente": "A agência percebe alguns problemas, mas não registra por etapa ou frequência.",
            "sim": "A agência registra problemas recorrentes e consegue identificar onde eles acontecem."
        }
    }
]

# Pontuação interna das respostas: quantitativa
# Essa pontuação não aparece para o usuário durante o questionário
# Dicionário para converter as respostas
pontuacao_respostas = {
    "nao": 0,
    "parcialmente": 1,
    "sim": 2
}

# Ordem de desempate para identificar gargalo principal
# Se duas áreas tiverem a mesma menor pontuação, o sistema segue esta ordem
ordem_desempate = [
    "Atendimento / Vendas",
    "Operação",
    "Comercial",
    "Dados"
]

# Diagnósticos específicos por área
# Cada área tem textos próprios para cada faixa de pontuação
# Dicionário aninhado
diagnosticos_por_area = {
    "Atendimento / Vendas": {
        "baixo": "Atendimento e vendas pouco estruturados. A agência provavelmente depende de memória, conversas soltas e ação individual.",
        "medio": "Atendimento e vendas em estruturação. Há práticas úteis, mas ainda sem padronização suficiente.",
        "bom": "Atendimento e vendas organizados. A agência já possui controle razoável, mas pode melhorar consistência e acompanhamento.",
        "alto": "Atendimento e vendas bem estruturados. Existe boa base para acompanhamento comercial, histórico e conversão."
    },
    "Comercial": {
        "baixo": "Comercial pouco estruturado. Fornecedores, condições e produtos provavelmente estão dispersos ou dependem de poucas pessoas.",
        "medio": "Comercial em estruturação. A agência possui algumas informações comerciais, mas ainda sem base confiável e atualizada.",
        "bom": "Comercial organizado. Há base de fornecedores e condições, mas ainda pode haver falha de atualização ou alinhamento.",
        "alto": "Comercial bem estruturado. A agência possui boa organização de fornecedores, condições e comunicação com as demais áreas."
    },
    "Operação": {
        "baixo": "Operação pouco estruturada. A entrega da viagem depende muito de improviso, memória e conferência manual.",
        "medio": "Operação em estruturação. Existem controles, mas ainda com risco de falhas por falta de checklist ou rastreabilidade.",
        "bom": "Operação organizada. A agência já possui boa base operacional, mas pode melhorar padronização e prevenção de erro.",
        "alto": "Operação bem estruturada. Existe controle consistente de reservas, documentos, confirmações e suporte."
    },
    "Dados": {
        "baixo": "Dados pouco estruturados. A agência toma decisões principalmente por percepção, sem registros mínimos.",
        "medio": "Dados em estruturação. Há alguma coleta, mas ainda sem consistência suficiente para análise.",
        "bom": "Dados organizados. A agência já mede parte da demanda, conversão e problemas, mas pode melhorar consolidação.",
        "alto": "Dados bem estruturados. A agência possui boa base para acompanhar desempenho e apoiar decisões."
    }
}

# Função para calcular a pontuação por área
# O .get() é um gatilho para procurar uma resposta salva
def calcular_pontuacao_por_area(respostas):
    pontuacao_areas = {
        "Atendimento / Vendas": 0,
        "Comercial": 0,
        "Operação": 0,
        "Dados": 0
    }

    for pergunta in perguntas:
        id_pergunta = pergunta["id"]
        area = pergunta["area"]

        resposta_usuario = respostas.get(id_pergunta)

        if resposta_usuario in pontuacao_respostas:
            pontos = pontuacao_respostas[resposta_usuario]
        else:
            pontos = 0

        pontuacao_areas[area] += pontos

    return pontuacao_areas


# Função para escolher o diagnóstico de uma área conforme a pontuação
def diagnosticar_area(area, pontos):
    if pontos <= 3:
        faixa = "baixo"
    elif pontos <= 6:
        faixa = "medio"
    elif pontos <= 8:
        faixa = "bom"
    else:
        faixa = "alto"

    return diagnosticos_por_area[area][faixa]


# Função para classificar o nível geral de maturidade digital
def classificar_maturidade(pontuacao_total):
    if pontuacao_total <= 10:
        return "Presença Digital Inicial"
    elif pontuacao_total <= 20:
        return "Digitalização Básica"
    elif pontuacao_total <= 30:
        return "Operação Digital em Estruturação"
    else:
        return "Gestão Digital Organizada"


# Função para gerar diagnóstico geral
def diagnosticar_geral(pontuacao_total):
    if pontuacao_total <= 10:
        return "A agência usa poucos processos digitais ou utiliza canais digitais sem organização operacional clara."
    elif pontuacao_total <= 20:
        return "A agência já utiliza ferramentas digitais, mas ainda depende de processos manuais, dispersos ou pouco padronizados."
    elif pontuacao_total <= 30:
        return "A agência possui práticas digitais relevantes, mas ainda precisa integrar melhor atendimento, comercial, operação e dados."
    else:
        return "A agência apresenta boa maturidade inicial, com processos mais claros e base para evoluir em automação, indicadores e gestão digital."


# Função para identificar o gargalo principal
# Values pega somente os números do dicionário
def identificar_gargalo(pontuacao_areas):
    menor_pontuacao = min(pontuacao_areas.values())

    for area in ordem_desempate:
        if pontuacao_areas[area] == menor_pontuacao:
            return area


# Função para calcular e salvar o resultado completo na session
def salvar_resultado_na_session():
    respostas = session.get("respostas")

    if respostas == None or len(respostas) < len(perguntas): # Verifica se não existe resposta salva OU se existem respostas salvas, mas em quantidade menor que o total de perguntas
        return False # Impede que o sistema gere diagnóstico com dados insuficientes

    pontuacao_areas = calcular_pontuacao_por_area(respostas)
    pontuacao_total = sum(pontuacao_areas.values())
    nivel_maturidade = classificar_maturidade(pontuacao_total)
    diagnostico_geral = diagnosticar_geral(pontuacao_total)
    gargalo_principal = identificar_gargalo(pontuacao_areas)

    diagnosticos_areas = {}

    for area, pontos in pontuacao_areas.items():
        diagnosticos_areas[area] = diagnosticar_area(area, pontos)

    session["pontuacao_areas"] = pontuacao_areas
    session["pontuacao_total"] = pontuacao_total
    session["nivel_maturidade"] = nivel_maturidade
    session["diagnostico_geral"] = diagnostico_geral
    session["gargalo_principal"] = gargalo_principal
    session["diagnosticos_areas"] = diagnosticos_areas

    return True


# Função auxiliar para verificar se existe resultado salvo
def resultado_existe():
    if "pontuacao_areas" in session and "pontuacao_total" in session:
        return True
    else:
        return False

# Rota inicial
# Sempre que o usuário volta para o início, o diagnóstico anterior é apagado.
@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

# Rota do diagnóstico
# Essa rota mostra uma parte por vez
# Também recebe a resposta da pergunta anterior quando o formulário é enviado
@app.route("/diagnostico", methods=["GET", "POST"])
def diagnostico():
    total_perguntas = len(perguntas)

    if "indice_pergunta" not in session:
        session["indice_pergunta"] = 0

    if "respostas" not in session:
        session["respostas"] = {}

    if request.method == "POST":
        resposta = request.form.get("resposta")
        id_pergunta = request.form.get("id_pergunta")

        if resposta == None:
            indice_atual = session["indice_pergunta"]
            pergunta_atual = perguntas[indice_atual]

            numero_pergunta = indice_atual + 1
            progresso = int((numero_pergunta / total_perguntas) * 100)

            return render_template(
                "diagnostico.html",
                pergunta=pergunta_atual,
                numero_pergunta=numero_pergunta,
                total_perguntas=total_perguntas,
                progresso=progresso,
                erro="Escolha uma resposta antes de continuar."
            )

        respostas = session["respostas"]
        respostas[id_pergunta] = resposta
        session["respostas"] = respostas

        session["indice_pergunta"] = session["indice_pergunta"] + 1

        if session["indice_pergunta"] >= total_perguntas:
            salvar_resultado_na_session()
            return redirect(url_for("resultado_areas"))

    if session["indice_pergunta"] >= total_perguntas:
        return redirect(url_for("resultado_areas"))

    indice_atual = session["indice_pergunta"]
    pergunta_atual = perguntas[indice_atual]

    numero_pergunta = indice_atual + 1
    progresso = int((numero_pergunta / total_perguntas) * 100)

    return render_template(
        "diagnostico.html",
        pergunta=pergunta_atual,
        numero_pergunta=numero_pergunta,
        total_perguntas=total_perguntas,
        progresso=progresso,
        erro=None
    )

# Resultado - Etapa 1
# Mostra apenas a interpretação da pontuação por área
@app.route("/resultado/areas")
def resultado_areas():
    if not resultado_existe():
        return redirect(url_for("index"))

    return render_template(
        "resultado.html",
        etapa_resultado="areas",
        pontuacao_areas=session["pontuacao_areas"],
        diagnosticos_areas=session["diagnosticos_areas"],
        pontuacao_total=session["pontuacao_total"],
        nivel_maturidade=session["nivel_maturidade"],
        diagnostico_geral=session["diagnostico_geral"],
        gargalo_principal=session["gargalo_principal"]
    )

# Resultado - Etapa 2
# Mostra a pontuação geral, nível de maturidade digital, diagnóstico geral e gargalo
@app.route("/resultado/geral")
def resultado_geral():
    if not resultado_existe():
        return redirect(url_for("index"))

    return render_template(
        "resultado.html",
        etapa_resultado="geral",
        pontuacao_areas=session["pontuacao_areas"],
        diagnosticos_areas=session["diagnosticos_areas"],
        pontuacao_total=session["pontuacao_total"],
        nivel_maturidade=session["nivel_maturidade"],
        diagnostico_geral=session["diagnostico_geral"],
        gargalo_principal=session["gargalo_principal"]
    )

# Resultado - Etapa 3
# Mostra o diagnóstico completo
@app.route("/resultado/completo")
def resultado_completo():
    if not resultado_existe():
        return redirect(url_for("index"))

    return render_template(
        "resultado.html",
        etapa_resultado="completo",
        pontuacao_areas=session["pontuacao_areas"],
        diagnosticos_areas=session["diagnosticos_areas"],
        pontuacao_total=session["pontuacao_total"],
        nivel_maturidade=session["nivel_maturidade"],
        diagnostico_geral=session["diagnostico_geral"],
        gargalo_principal=session["gargalo_principal"]
    )

# Rota de confirmação antes de reiniciar o diagnóstico - navbar
# Essa tela não limpa a session ainda
# Ela apenas avisa que o progresso será perdido
@app.route("/confirmar-reinicio")
def confirmar_reinicio():
    return render_template("confirmar_reinicio.html")

# Rota que reinicia o diagnóstico - navbar
# Aqui a session é limpa e o usuário volta para a tela inicial
@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))

# Executando o servidor local
if __name__ == "__main__":
    app.run(debug=True)