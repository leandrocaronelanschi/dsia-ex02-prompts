"""Consolida somente medições existentes; não altera nem repete execuções."""
import csv, json
from pathlib import Path
R = Path(__file__).resolve().parents[1]
nomes = ['direto', 'few-shot', 'contexto', 'criterios']
colunas = ['estrategia','acertos','total_testes','retrabalho','tempo_s','tempo_min','modelo','versao','temperatura','data','inicio_utc','fim_utc','status']
with (R/'execucoes'/'registro.csv').open('w',newline='') as arquivo:
    writer = csv.DictWriter(arquivo,fieldnames=colunas)
    writer.writeheader()
    for i,nome in enumerate(nomes,1):
        d=json.loads((R/'execucoes'/f'{i:02}'/'medicao.json').read_text())
        writer.writerow(dict(estrategia=f'{i:02}-{nome}',acertos=d['acertos_primeira'],total_testes=d['total_testes'],retrabalho=d['retrabalho'],tempo_s=d['tempo_total_s'],tempo_min=round(d['tempo_total_s']/60,4),modelo='GPT-6 / Codex',versao='snapshot nao exposto pela interface',temperatura='nao exposta',data=d['inicio_utc'][:10],inicio_utc=d['inicio_utc'],fim_utc=d['fim_utc'],status='aprovado' if d['ultimo_retorno']==0 else 'falha'))
