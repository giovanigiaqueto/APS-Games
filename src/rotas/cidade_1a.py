#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import especial
from ..narracao import narrador
from ..base import Opcao, Escolhas

def inicio():

    narrador(\
    """
    Com o pensamento de que poderiam passar despercebidos pelos zumbis,
    você decide ir com a ideia de ir pelos esgotos.
    """,
    """
    Já dentro do esgoto, alguns metros distantes de onde desceram,
    vocês encontram uma bifurcação.

    Mary comenta “Vamos pela esquerda, esquerda sempre é o caminho certo!”
    Já Edy, contesta “Isso é apenas uma possibilidade! Vamos continuar pela direita.”
    """, identacao=2)

    op1 = Opcao("Esquerda!", lambda: esgoto_esquerda)
    op2 = Opcao("Direita!",  lambda: esgoto_direita)

    return Escolhas(op1, op2, introducao="Mais uma vez, a decisão é sua")

def esgoto_esquerda():

    narrador(\
    """
    Você decide confiar na Mary e escolhe seguir pela esquerda.
    """,
    """
    Tudo parece tranquilo, até que vocês percebem que esse caminho não levaria a lugar nenhum.
    E pra piorar, havia vários zumbis por lá, que perceberam sua presença.
    """,
    """
    Ao dar meia volta, zumbis surgem do buraco que havia no esgoto,
    bloqueando a sua única saída.

    Você tenta matar os zumbis que haviam no caminho,
    porém você não imaginava que iriam aparecer tantos assim.
    """,
    """
    *click* *click*
    Sua munição acabou. Não tendo mais como se defender,
    você e seus amigos são encurralados, e suas vidas são tomadas.
    """, identacao=2, continuar_final=True)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def esgoto_direita():

    narrador(\
    """
    Já que foi Edy que recomendou os esgotos, faz sentido eu seguir o caminho que ele diz.
    Parece que ele realmente sabia o caminho, pois não parecia ter nenhum zumbi.
    """,
    """
    Até que você escuta Edy gritar de dor. Ao olhar pra trás você vê Edy sendo mordido
    no tornozelo por um zumbi que o pegou de surpresa, saindo de um buraco.
    """, identacao=2)

    op1 = Opcao("Atirar no zumbi", lambda: atirar_zumbi)
    op2 = Opcao("Não atirar no zumbi", lambda: nao_atirar_zumbi)

    return Escolhas(op1, op2, introducao="Você.")

def atirar_zumbi():

    narrador(\
    """
    Sem perder tempo, você decide atirar no zumbi pra deixar Edy livre.
    A atmosfera fica mais densa, ao perceberem a atual situação que se encontram.
    Edy foi mordido.
    """, identacao=2, continuar_final=True)

    return fim_esgoto

def nao_atirar_zumbi():

    narrador(\
    """
    Você decide ajudar Edy sem gastar munição, porém leva mais tempo,
    e isso faz com que a mordida seja mais severa.
    Edy vai precisar de um apoio para conseguir andar.
    """, identacao=2, continuar_final=True)

    return fim_esgoto

def fim_esgoto():

    narrador(\
    """
    Após alguns segundos você consegue ouvir o que seria
    uma grande quantidade de zumbis vindo de onde vocês vieram.
    """,
    """
    Ao chegar na saída, você ajuda Edy a subir primeiro por causa da mordida.
    Logo abaixo você sobe as escadas e percebe que ela está enferrujada.
    """,
    """
    Por último, Mary sobe as escadas, porém ela se quebra
    ao ser pisada e Mary cai de costas no chão do esgoto.
    """, identacao=2)

    op1 = Opcao("Descer e salvar Mary", lambda: ajudar_mary)
    op2 = Opcao("Abandonar Mary", lambda: nao_ajudar_mary)

    return Escolhas(op1, op2, introducao="Você ao ver Mary desacordada no chão do esgoto, decide:")

def ajudar_mary():

    narrador(\
    """
    Mesmo chamando várias vezes pela Mary, ela não acordava.
    Você decide se arriscar e pular de volta para tentar salvar ela.
    """,
    """
    Porém, não esperava ter tantos zumbis por perto. Infelizmente, não tinha saída.
    Não tinha como salvar Mary. Não tinha como você se salvar.
    """, identacao=2)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def nao_ajudar_mary():

    narrador(\
    """
    Após chamar várias vezes por Mary, você vê que ela não vai acordar a tempo.
    Zumbis surgem ao lado de Mary e encobrem toda a visão que você tinha dela.
    """,
    """
    Não tinha como ela sobreviver.
    Não querendo ver essa cena, você puxa Edy e decide seguir em frente.
    """, identacao=2, continuar_final=True)

    return descansar_ou_seguir

def descansar_ou_seguir():

    narrador(
    """
    Após andar alguns metros, você percebe que irá demorar bastante
    para chegar no refúgio se continuarem assim, porém, Edy não quer parar,
    pois quer chegar no refúgio o quanto antes.
    """, identacao=2)

    op1 = Opcao("Continuar em direção ao refúgio", lambda: continuar)
    op2 = Opcao("Descansar na casa abandonada", lambda: descansar_abrigo)

    return Escolhas(op1, op2, introducao="Há uma casa abandonada próxima a vocês, o que vão fazer?")

def continuar():

    narrador(\
    """
    Concordando com Edy, a melhor opção seria chegar o mais rápido no refúgio
    para curar a ferida que o zumbi deixou.
    """,
    """
    Porém, conforme vão andando, a situação do Edy piora, ele começa a suar,
    você checa a temperatura dele e ele parece estar muito febril.
    """,
    """
    Acelerando o passo, alguns minutos depois, Edy cai no chão desacordado.
    Você tenta acordá-lo, porém, sem resposta.
    """,
    """
    Pra não perder tempo, você decide carrega-lo no colo, em direção ao refúgio,
    visto que estavam relativamente perto.
    """,
    """
    Quando você menos espera, Edy por alguma razão te ataca,
    mordendo seu pescoço, acertando em cheio sua artéria carótida.
    Você desaba na hora. Você vê seu próprio amigo devorando você.
    """,
    """
    Talvez você tenha esquecido, mas Edy ao ser mordido por um zumbi,
    não ia demorar muito tempo para virar zumbi.
    """, identacao=2, continuar_final=True)

    op = Opcao("Menu Inicial", lambda: especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def descansar_abrigo():

    narrador(\
    """
    Vocês decidem descansar em uma casa próxima abandonada.

    Vendo como a mordida no tornozelo de Edy está,
    você lembra que se não cuidar, ele não irá resistir e até virar um deles.
    Pra sua sorte, havia um arco de serra no quintal da casa.
    """, identacao=2)

    op1 = Opcao("Serrar a perna de Edy", lambda: serrar_perna)
    op2 = Opcao("Não serrar a perna de Edy", lambda: nao_serrar_perna)

    return Escolhas(op1, op2, introducao="Você precisa tomar uma decisão.")

def serrar_perna():

    narrador(\
    """
    Edy sabia da situação que estava,
    e se fosse o único jeito de aumentar as chances de sobrevivência, ele faria.
    """,
    """
    Então após concordarem em continuar, você decide serrar a perna dele.
    Pode se dizer que isso foi a pior coisa que você já teve que fazer na vida.
    """,
    """
    Como a serra não cortava de uma vez, você demorou um bom tempo pra serrar a perna.
    Com a camisa na boca para não gritar, Edy não aguentava de dor.
    Após um longo tempo, Edy desmaia, porém, você consegue finalizar o corte.
    """, identacao=2)

    op1 = Opcao("Procurar pela casa por bandagens", lambda: bandagens)
    op2 = Opcao("Usar sua camisa como bandagem", lambda: camisa)

    return Escolhas(op1, op2,
        introducao="Não tendo nenhum tipo de bandagem pra cobrir o sangramento, você prefere:")

def nao_serrar_perna():

    narrador(\
    """
    Você decide que não vai serrar a perna de Edy pois não tem noção de como fazer isso.
    “Não tem problema, assim que amanhecer, iremos para o refúgio.”, disse Edy.
    """, identacao=2, continuar_final=True)

    return descansar

def camisa():

    narrador(\
    """
    Você tira a sua camisa e a usa como bandagem na perna de Edy.
    Agora ele só precisa descansar um tempo
    """, identacao=2, continuar_final=True)

def bandagens():

    narrador(\
    """
    Você deixa Edy no sofá desmaiado perdendo sangue pela perna,
    e corre para investigar a casa, na expectativa de encontrar bandagens.

    Mas como era uma casa abandonada, não haviam nenhum tipo de kit médico,
    pois provavelmente antigos moradores ou desertores pegaram antes de nós.
    """,
    """
    Após procurar pela casa, você desiste e volta para sala de estar,
    onde Edy parece estar caído no chão.
    """,
    """
    Você o segura e percebe que Edy não está mais respirando.
    Ele deve ter morrido por causa do sangramento.
    Você não se conforma que ele não está mais contigo e começa a chorar.
    Na sua cabeça, a culpa é sua por não conseguir salva-lo.
    """,
    """
    Quando você menos espera, Edy por alguma razão te ataca,
    mordendo seu pescoço, acertando em cheio sua artéria carótida.
    Você desaba na hora. Você vê seu próprio amigo devorando você.
    Talvez você tenha esquecido, mas Edy ao ser mordido por um zumbi,
    não ia demorar muito tempo para virar zumbi,
    o sangramento apenas o ajudou a morrer e se transformar mais rápido.
    """, identacao=2)

    op = Opcao("Menu Inicial", especial.menu)

    return Escolhas(op, introducao="Você morreu.")

def descansar():

    narrador(\
    """
    Como o sofá já estava ocupado,
    decidi dormir na sala ao lado onde havia um outro sofá meio que confortável.
    """,
    """
    Algum tempo depois...

    Um barulho de como se fosse algo caindo no chão te acorda.
    Ao abrir a porta que dava pra sala de estar, Edy se joga em você.
    O que você via na sua frente não era mais seu amigo, e sim, um zumbi.
    As únicas coisas que você consegue alcançar são sua mochila e um pedaço de pau.
    """, identacao=2)

    op1 = Opcao("Se defender com a mochila", especial.cidade_2a_inicio)
    op2 = Opcao("Se defender com o pedaço de pau", especial.cidade_2b_inicio)

    return Escolhas(op1, op2, introducao="Você decide:")
