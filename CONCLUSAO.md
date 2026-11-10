# Conclusão — Conferência de vigência de parcerias

A tarefa foi classificar o fim da vigência de uma parceria em quatro estados, usando uma referência explícita e um horizonte didático de 30 dias. A hipótese inicial era que critérios verificáveis ajudariam a tratar limites e entradas inválidas. Os 12 testes foram escritos antes das implementações e aplicados às quatro versões sem alterar o oráculo.

| Estratégia | Acertos de primeira | Correções | Tempo total (s) |
| --- | ---: | ---: | ---: |
| 01-direto | 12/12 | 0 | 11.213 |
| 02-few-shot | 12/12 | 0 | 13.589 |
| 03-contexto | 12/12 | 0 | 13.006 |
| 04-criterios | 12/12 | 0 | 15.371 |

Houve empate em acertos e retrabalho: todas as versões passaram em 12 de 12 testes de primeira, sem rodada corretiva. Assim, a hipótese de vantagem dos critérios explícitos não foi confirmada por esta observação. Nenhuma estratégia venceu em qualidade dentro da cobertura adotada. O prompt direto teve o menor tempo observado, mas isso não demonstra que seja mais rápido em geral.

Os exemplos do few-shot tornam visível a transição entre os estados. O contexto fornece a convenção do projeto para datas e a interface pública. Os critérios explicitam formato estrito, calendário e fronteiras. Embora essas informações sejam potencialmente úteis, não houve ganho mensurável de acerto nesta tarefa: o pedido básico e o conhecimento prévio do assistente já foram suficientes para todos os casos testados. Não se deve inventar erros para produzir um vencedor.

Há limitações fortes. Foi uma execução por estratégia, sem randomização, e o mesmo assistente conhecia os testes e as outras etapas. As implementações foram novas e separadas em arquivos, mas o contexto não foi isolado em quatro conversas. Portanto, o resultado não permite atribuir diferenças ao conteúdo de cada prompt. Além disso, o primeiro tempo incluiu criação do ambiente e ajuste da dependência; todos os tempos incluem ferramentas e gravação de arquivos, não somente geração. Não houve controle da temperatura ou informação do snapshot exato do modelo.

A conclusão sustentada é restrita: quatro variantes construídas nesta sessão atenderam ao oráculo didático sem retrabalho. Isso não prova ausência de bugs, superioridade de uma estratégia ou validade para processos administrativos reais. Uma continuação rigorosa precisa usar sessões independentes com parâmetros iguais, ambiente previamente pronto, ordem aleatória, mais tarefas e repetições. A exigência de isolamento do curso ainda precisa ser atendida antes de considerar este material um experimento completo para entrega.
