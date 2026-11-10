# Exercício 2 — Quatro estratégias de prompt

## Tarefa e tema proposto
Tema exploratório proposto neste trabalho: apoio automatizado à conferência de vigência de parcerias institucionais. Este recorte foi escolhido para a nova solução; não é apresentado como tema de pesquisa previamente aprovado do participante. A tarefa pequena é implementar uma função de classificação de datas, útil como componente de uma futura ferramenta de acompanhamento. Não foi consultado o repositório de uma entrega anterior.

`classificar_vigencia(fim, referencia)` recebe strings ISO estritas e retorna vencido, vence_hoje, a_vencer (1–30 dias) ou vigente (>30 dias). Entrada inválida gera ValueError. Não há dados reais, decisão administrativa ou regra legal embutida: 30 dias é uma convenção didática.

## Rodar
Requer Python 3.12+ e uv. Na raiz do projeto:

```sh
uv sync --locked
uv run pytest
# Apenas uma estratégia (Linux/macOS):
ESTRATEGIA=01 uv run pytest
# Na plataforma Windows PowerShell:
$env:ESTRATEGIA='01'; uv run pytest
Remove-Item Env:ESTRATEGIA
```

Não é necessária API, token ou arquivo .env para executar os testes. `uv.lock` fixa as dependências. A execução original usou Python 3.12.14 e pytest 9.2.0.

## Critério de acerto e medições
O protocolo, hipótese e os 12 testes parametrizados foram gravados no primeiro commit, antes das implementações. Os testes atuais são os mesmos. Cada estratégia é carregada isoladamente por importlib, totalizando 48 verificações. A primeira versão de cada código está preservada em primeira.py; vigencia.py é a versão final. Como não houve falhas, os dois arquivos são idênticos.

O arquivo PROTOCOLO.md fixa acertos de primeira, rodadas de retrabalho e tempo de parede. `execucoes/registro.csv` contém uma linha por estratégia; medicao.json e teste-01.txt preservam os dados da coleta. Tempos são reais e incluem ferramentas e gravação; não representam latência de API. A primeira estratégia também incluiu a criação do ambiente e ajuste da versão de pytest, enquanto as demais aproveitaram o ambiente pronto. Essa assimetria prejudica comparações de tempo; nenhum ranking causal é sustentado.

## Quatro estratégias e limitações
Os quatro prompts compartilham o pedido básico. Apenas o segundo acrescenta exemplos; o terceiro inclui um recorte de convenções do projeto didático; o quarto explicita condições verificáveis. Cada implementação foi escrita de novo, sem importar ou copiar arquivos das outras pastas.

**Atenção metodológica:** não houve quatro conversas independentes com um modelo externo. O mesmo assistente, com conhecimento dos testes e do histórico, escreveu todas as variantes nesta conversa. Os prompts são instruções documentadas de construção, não logs de quatro chamadas API isoladas. A geração e a avaliação não são independentes. O resultado é demonstrativo e não satisfaz integralmente a exigência de isolamento experimental do curso. Repetir apenas pytest reproduz a avaliação, não a geração.

Ferramenta: ChatGPT Work / assistente Codex, família de modelo informada no ambiente: GPT-6. Snapshot exato, seed e temperatura não foram expostos. A versão instalada do cliente CLI (0.167.0-alpha.4) não identifica o modelo e esse cliente não foi usado para gerar as variantes. Ver USO-DE-IA.md.

Para repetir com isolamento: congelar testes e convenções; abrir quatro sessões novas com o mesmo modelo e parâmetros; fornecer somente o respectivo prompt; não mostrar testes nem variantes anteriores; salvar as respostas brutas, medir desde a escrita do pedido, testar e contar cada rodada de correção. Não misturar os novos resultados com este registro.

## Publicação e entrega
Este pacote ainda não foi publicado nem enviado à atividade. O GitHub exigiu login, e o repositório anterior não foi aberto. A plataforma pede repositório público chamado dsia-ex02-prompts, branch main e envio do link. Se esse nome já existir na conta, não sobrescrever a entrega anterior: usar outra conta autorizada ou decidir explicitamente como preservar o projeto existente.

O pacote ZIP contém o histórico Git local para verificar a ordem dos commits. Depois de descompactar, `git log --oneline --reverse` mostra protocolo/testes antes das implementações. Antes de entregar, é preciso corrigir a limitação de isolamento descrita acima e conferir acesso público ao repositório.
