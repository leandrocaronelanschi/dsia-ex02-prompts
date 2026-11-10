from datetime import date
from re import fullmatch

def classificar_vigencia(fim, referencia):
    def validar(entrada):
        if type(entrada) is not str or fullmatch('[0-9]{4}-[0-9]{2}-[0-9]{2}', entrada) is None:
            raise ValueError('Esperada data AAAA-MM-DD')
        try:
            ano, mes, dia = map(int, entrada.split('-'))
            return date(ano, mes, dia)
        except ValueError as causa:
            raise ValueError('Data inexistente') from causa
    dias_restantes = (validar(fim) - validar(referencia)).days
    if dias_restantes < 0:
        status = 'vencido'
    elif dias_restantes == 0:
        status = 'vence_hoje'
    elif 1 <= dias_restantes <= 30:
        status = 'a_vencer'
    else:
        status = 'vigente'
    return status
