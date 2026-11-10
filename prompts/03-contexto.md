Implemente em Python a função pura classificar_vigencia(fim, referencia) para classificar o término da vigência de uma parceria em vencido, vence_hoje, a_vencer ou vigente. As entradas são datas ISO e o horizonte de alerta é 30 dias. Use apenas a biblioteca padrão e rejeite entradas inválidas com ValueError.

Recorte do repositório didático novo — contexto/CONVENCOES.md:
API pública: classificar_vigencia(fim, referencia) -> str.
Datas são strings AAAA-MM-DD, exatamente dez caracteres ASCII, validadas como datas reais; entrada inválida gera ValueError. Não usar relógio do sistema.
Alertas de vigência: fim anterior à referência é vencido; igual é vence_hoje; do dia seguinte até 30 dias inclusive é a_vencer; depois é vigente.
A função é pura e usa apenas biblioteca padrão.
