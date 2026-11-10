# Protocolo anterior às implementações

Tarefa exploratória do domínio de gestão de parcerias: classificar a proximidade do término de vigência de um instrumento. Não se afirma vínculo com uma pesquisa já definida pelo participante. Os dados são fictícios; a função não decide prorrogações nem produz parecer jurídico.

Contrato: `classificar_vigencia(fim, referencia)` recebe duas strings ISO estritas `AAAA-MM-DD`. Data inválida, tipo diferente de string ou formato diferente produzem ValueError. Diferença negativa: vencido; zero: vence_hoje; 1 a 30 dias inclusive: a_vencer; acima de 30: vigente. Datas civis, sem relógio e sem fuso. A referência é explícita, sem consultar a data atual.

Os 12 testes por estratégia são escritos e versionados antes de qualquer código gerado. Cada pasta começa vazia e não importa código de outra estratégia. A primeira versão é preservada. Uma edição corretiva completa conta como uma rodada de retrabalho; não se contam linhas editadas. Limite: duas rodadas por estratégia, com falha final explicitada se ocorrer.

Acertos: testes aprovados na primeira execução / 12. Tempo total: segundos de relógio monotônico desde o início da escrita do arquivo de prompt até o término da primeira execução com todos os testes aprovados, incluindo gravação dos arquivos e acionamento das ferramentas. Não é tempo de CPU nem latência isolada do modelo. O relatório de teste mede separadamente a duração do pytest. Preparação do oráculo e publicação não entram. Registros são gravados durante o processo, não reconstruídos ao fim.

Hipótese: os critérios explícitos devem ajudar nos limites de 30 dias e no formato estrito; o contexto também pode evitar divergências das convenções. Não se prevê vencedor em tempo.

Limitação conhecida ANTES: um único assistente escreve as quatro soluções nesta mesma conversa. Não há quatro contextos de modelo independentes, e o assistente já conhece o oráculo. Pastas isoladas não eliminam esse vazamento. Este é um estudo demonstrativo intrassessão, não uma comparação causal válida entre prompts. Não se inventarão sessões novas, chamadas API, parâmetros, identificadores de versão ou resultados.
