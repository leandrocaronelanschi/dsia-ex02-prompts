# Convenções do módulo de parcerias (projeto didático novo)
API pública: classificar_vigencia(fim, referencia) -> str.
Datas são strings AAAA-MM-DD, exatamente dez caracteres ASCII, validadas como datas reais; entrada inválida gera ValueError. Não usar relógio do sistema.
Alertas de vigência: fim anterior à referência é vencido; igual é vence_hoje; do dia seguinte até 30 dias inclusive é a_vencer; depois é vigente.
A função é pura e usa apenas biblioteca padrão.
