Implemente em Python a função pura classificar_vigencia(fim, referencia) para classificar o término da vigência de uma parceria em vencido, vence_hoje, a_vencer ou vigente. As entradas são datas ISO e o horizonte de alerta é 30 dias. Use apenas a biblioteca padrão e rejeite entradas inválidas com ValueError.

Exemplos:
classificar_vigencia('2026-05-03', '2026-05-04') -> 'vencido'
classificar_vigencia('2026-05-04', '2026-05-04') -> 'vence_hoje'
classificar_vigencia('2026-06-03', '2026-05-04') -> 'a_vencer'
classificar_vigencia('2026-06-04', '2026-05-04') -> 'vigente'
classificar_vigencia('04/05/2026', '2026-05-04') -> ValueError
