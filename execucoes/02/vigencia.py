from datetime import datetime

def classificar_vigencia(fim, referencia):
    def converter(texto):
        if not isinstance(texto, str):
            raise ValueError('A data deve ser texto ISO')
        try:
            data = datetime.strptime(texto, '%Y-%m-%d').date()
        except (ValueError, TypeError) as erro:
            raise ValueError('Data inválida') from erro
        canonico = f'{data.year:04d}-{data.month:02d}-{data.day:02d}'
        if texto != canonico:
            raise ValueError('Use AAAA-MM-DD')
        return data
    diferenca = (converter(fim) - converter(referencia)).days
    if diferenca < 0:
        return 'vencido'
    elif diferenca == 0:
        return 'vence_hoje'
    elif diferenca in range(1, 31):
        return 'a_vencer'
    else:
        return 'vigente'
