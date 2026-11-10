Implemente em Python a função pura classificar_vigencia(fim, referencia) para classificar o término da vigência de uma parceria em vencido, vence_hoje, a_vencer ou vigente. As entradas são datas ISO e o horizonte de alerta é 30 dias. Use apenas a biblioteca padrão e rejeite entradas inválidas com ValueError.

Critérios de aceite:
1. As duas entradas precisam ser strings exatamente AAAA-MM-DD, com dígitos ASCII e datas reais.
2. Tipo, formato ou calendário inválido deve gerar ValueError para qualquer argumento.
3. Calcule dias civis como fim menos referencia; não use a data atual.
4. Diferença negativa resulta em vencido; zero resulta em vence_hoje.
5. Diferenças de 1 até 30 inclusive resultam em a_vencer; acima de 30 resultam em vigente.
6. Respeite mudanças de mês e ano e anos bissextos. A função não altera estado externo.
