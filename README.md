# lnpg-cap9-subprogramas-Manoel-Silva
# Nome: Manoel Vitor Vieira da Silva
# Turma: LNPG-BSI-2026.1
***************************************************************************************************************************************************************************
TAREFA-1 JAVA

Descrição: O sistema de controle acadêmico em Java foi desenvolvido para cadastrar alunos, registrar notas, calcular médias e informar a situação final de cada estudante. O programa utiliza modularização para organizar as funcionalidades em métodos específicos, tornando o código mais legível, reutilizável e fácil de manter.

Intruções de execução:
Execute a versão monolítica no VS Code inserindo o seguinte comando no terminal:
1- javac ControleAcademicoMonolitico.java ( cria uma arquivo .class )
2- java ControleAcademicoMonolitico ( executa o programa )

Execute a versão modularizada no VS Code inserindo o seguinte comando no terminal:
1- javac ControleAcademico.java ( cria uma arquivo .class )
2- java ControleAcademico ( executa o programa )

Comparação:
Versão Monolítica: A versão monolítica concentra toda a lógica do sistema dentro do método main, deixando o código maior e mais difícil de organizar. Apesar de funcionar corretamente, possui menor legibilidade, manutenção mais complexa e pouca reutilização de código.

Versão Modularizada: A versão modularizada divide o sistema em métodos específicos, como leitura de dados, cálculo de média e impressão do relatório. Essa organização melhora a legibilidade, facilita a manutenção, reduz repetições e torna o código mais reutilizável e estruturado.

Legibilidade: Na versão modularizada, o código fica mais organizado e fácil de entender, pois cada função possui uma responsabilidade específica.
Reutilização: As funções podem ser reutilizadas em outros programas, evitando repetição de código.
Facilidade de manutenção: Alterações podem ser feitas apenas na função necessária sem modificar todo o sistema.
Clareza do fluxo: O método main() apresenta o fluxo principal do sistema de maneira mais clara e organizada.
Tamanho dos métodos: As funções menores tornam o código mais limpo, simples e fácil de testar.
Coesão: Cada função executa apenas uma tarefa específica, melhorando a organização e a eficiência do sistema.

***************************************************************************************************************************************************************************

TAREFA-2 PYTHON

Descrição: Desenvolvimento de um sistema de compras em Python utilizando funções para organizar o programa. O sistema permite selecionar produtos, calcular subtotais, aplicar descontos conforme o valor da compra, gerar o total final e exibir um cupom com as informações da compra.

Instruções de execução:
Execute a versão monolítica no VS Code:
python tarefa-2-monolitica.py
Execute a versão modularizada no VS Code:
python tarefa-2-refatorada.py

Comparação:
Versão monolítica (tarefa-2-monolitica.md)
Tudo está em um único bloco de código
Entrada, cálculo e impressão estão misturados
Possui repetição de validação e lógica no loop
Fácil de entender como “um programa só”
Difícil de reaproveitar partes isoladas

Versão modularizada (tarefa-2-refatorada.md)
Código dividido em funções com responsabilidades claras
Cada função trata só uma tarefa
Fluxo principal em main() fica mais limpo
Torna mais fácil testar, ajustar ou reaproveitar

Legibilidade: a modularização torna o código mais organizado e fácil de compreender, pois cada função possui um objetivo específico, evitando blocos grandes e confusos.
Reutilização: funções podem ser reaproveitadas em diferentes partes do sistema ou em outros programas, reduzindo repetição de código e aumentando a produtividade.
Facilidade de manutenção: alterações e correções ficam mais simples, já que cada função é independente e pode ser modificada sem afetar todo o sistema.
Clareza do fluxo: o main() apresenta o passo a passo do programa de maneira organizada, facilitando a visualização da lógica de execução.
Tamanho dos métodos: funções menores deixam o código mais limpo, objetivo e fácil de testar, além de melhorar a identificação de erros.
Coesão: cada função executa apenas uma responsabilidade específica, aumentando a organização, eficiência e qualidade do sistema.

***************************************************************************************************************************************************************************

