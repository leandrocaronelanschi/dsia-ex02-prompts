"""Cronômetro e coleta reais; não executa modelos nem fabrica saídas."""
import csv, hashlib, json, os, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[1]
acao, numero = sys.argv[1:3]
pasta = R/'execucoes'/numero
if acao == 'iniciar':
    assert not (pasta/'medicao.json').exists(), 'Não sobrescrever medição.'
    dados = {'inicio_monotonico':time.monotonic(),'inicio_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
    (pasta/'medicao.json').write_text(json.dumps(dados,indent=2))
elif acao == 'avaliar':
    dados = json.loads((pasta/'medicao.json').read_text())
    primeira = not (pasta/'primeira.py').exists()
    if primeira:
        (pasta/'primeira.py').write_bytes((pasta/'vigencia.py').read_bytes())
    ambiente = dict(os.environ, ESTRATEGIA=numero)
    resultado = subprocess.run(['uv','run','pytest','-q','--junitxml='+str(pasta/'pytest.xml')],cwd=R,env=ambiente,capture_output=True,text=True)
    tentativa = dados.get('avaliacoes',0)+1
    (pasta/f'teste-{tentativa:02}.txt').write_text(resultado.stdout+resultado.stderr)
    import xml.etree.ElementTree as ET
    suites = ET.parse(pasta/'pytest.xml').getroot()
    total = sum(int(s.get('tests',0)) for s in suites)
    falhas = sum(int(s.get('failures',0))+int(s.get('errors',0))+int(s.get('skipped',0)) for s in suites)
    dados.update(avaliacoes=tentativa, ultimo_retorno=resultado.returncode, total_testes=total)
    if primeira: dados['acertos_primeira']=total-falhas
    dados['retrabalho']=tentativa-1
    dados['tempo_total_s']=round(time.monotonic()-dados['inicio_monotonico'],3)
    dados['fim_utc']=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    dados['sha256_primeira']=hashlib.sha256((pasta/'primeira.py').read_bytes()).hexdigest()
    (pasta/'medicao.json').write_text(json.dumps(dados,indent=2))
    print(resultado.stdout, resultado.stderr)
    print(json.dumps(dados))
    sys.exit(resultado.returncode)
