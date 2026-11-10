import datetime

def _ler_data(valor):
    if not isinstance(valor, str) or len(valor) != 10:
        raise ValueError('Data deve ter dez caracteres')
    if valor[4] != '-' or valor[7] != '-':
        raise ValueError('Separador inválido')
    digitos = valor[:4] + valor[5:7] + valor[8:]
    if any(c not in '0123456789' for c in digitos):
        raise ValueError('Somente algarismos ASCII')
    return datetime.date(int(valor[:4]), int(valor[5:7]), int(valor[8:]))

def classificar_vigencia(fim, referencia):
    distancia = (_ler_data(fim) - _ler_data(referencia)).days
    if distancia > 30:
        return 'vigente'
    if distancia > 0:
        return 'a_vencer'
    return 'vence_hoje' if distancia == 0 else 'vencido'
