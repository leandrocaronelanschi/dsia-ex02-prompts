from datetime import date
import re

def classificar_vigencia(fim, referencia):
    datas = []
    for valor in (fim, referencia):
        if not isinstance(valor, str) or re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', valor) is None:
            raise ValueError('Data ISO inválida')
        datas.append(date.fromisoformat(valor))
    dias = (datas[0] - datas[1]).days
    if dias < 0:
        return 'vencido'
    if dias == 0:
        return 'vence_hoje'
    if dias <= 30:
        return 'a_vencer'
    return 'vigente'
