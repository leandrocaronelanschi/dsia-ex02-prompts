"""Oráculo escrito antes das quatro implementações; 12 casos por estratégia."""
import importlib.util
import os
from pathlib import Path
import pytest

RAIZ = Path(__file__).resolve().parents[1]
ESCOLHAS = [os.environ['ESTRATEGIA']] if 'ESTRATEGIA' in os.environ else ['01','02','03','04']

@pytest.fixture(params=ESCOLHAS)
def classificar(request):
    caminho = RAIZ / 'execucoes' / request.param / 'vigencia.py'
    spec = importlib.util.spec_from_file_location('vigencia_' + request.param, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.classificar_vigencia

@pytest.mark.parametrize('fim,referencia,esperado', [
    ('2026-11-09','2026-11-10','vencido'),
    ('2026-11-10','2026-11-10','vence_hoje'),
    ('2026-11-11','2026-11-10','a_vencer'),
    ('2026-12-10','2026-11-10','a_vencer'),
    ('2026-12-11','2026-11-10','vigente'),
    ('2028-03-01','2028-02-01','a_vencer'),
    ('2027-01-01','2026-12-01','vigente'),
])
def test_faixas(classificar,fim,referencia,esperado):
    assert classificar(fim,referencia) == esperado

@pytest.mark.parametrize('fim,referencia', [
    ('2026-02-29','2026-11-10'),
    ('2026-1-01','2026-11-10'),
    ('2026-11-10','10/11/2026'),
    ('','2026-11-10'),
    (None,'2026-11-10'),
])
def test_invalidos(classificar,fim,referencia):
    with pytest.raises(ValueError):
        classificar(fim,referencia)
