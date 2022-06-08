## Validar cadastro de estágio

| ITEM | VALUE |
| --- | --- |
| UseCase | Validar cadastro de estágio |
| Summary | Ação responsável por avaliar se as informações fornecidas pelo aluno são validas. |
| Actor | Divisão de estágio, Aluno. |
| Precondition | 1. Administrador estar logado no sistema; <br> 2. Ter o aluno cadastrado no sistema;	 <br> 3. O aluno ter solicitado o cadastro de estágio. |
| Postcondition | 1. Cadastro de estágio validado.  |
| Base Sequence | 1. Divisão de estágio faz validação das informações enviadas pelo aluno; <br> 2. Divisão de estágio divulga a situação do cadastro, no sistema, para o aluno. |
| Branch Sequence | 1.1 Dados inválidos: <br>  1.  Caso os dados enviados estejam incorretos ou estejam em falta, o responsável pela validação deixará uma mensagem informando quais dados precisam ser corrigidos ou enviados novamente. |
| Exception Sequence | 1. O cadastro não será realizado. |
| Sub UseCase |  |
| Note |  |
