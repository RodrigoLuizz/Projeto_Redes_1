## Cadastrar-se

| ITEM | VALUE |
| --- | --- |
| UseCase | Cadastrar-se |
| Summary | Ação responsável pelo cadastro de usuário no sistema, nesta ação teremos o formulário no qual o usuário deverá preencher para que possa ser cadastrado corretamente no sistema. |
| Actor | Usuário |
| Precondition | 1. Ter e-mail existente na instituição relativa ao sistema;  <br>2. Ter um CPF e RG válidos como matrícula;  <br>3. Estar matriculado na faculdade. |
| Postcondition | 1. Novo usuário cadastrado após verificação. |
| Base Sequence | 1. O usuário irá selecionar o tipo de cadastro (Professor/Aluno); <br> 2. O usuário irá preencher o formulário de cadastro de acordo com o tipo selecionado;<br> 3. O sistema irá validar os campos preenchidos pelo usuário;<br> 4. O usuário vai finalizar a ação. |
| Branch Sequence | 1.1 Dados não foram totalmente preenchidos:  <br>1.O sistema irá disparar que os dados devem ser preenchidos e são obrigatórios e o usuário terá que informá-los para continuar. <br>1.2 Dados inválidos:<br> 1. Caso o usuário insira algum dado que não seja válido (CPF, RG, Email) o sistema irá disparar um erro, avisando que os dados são inválidos. |
| Exception Sequence | 1. Caso os dados preenchidos estejam incorretos o cadastro não será realizado. |
| Sub UseCase | Verificar e-mail |
| Note |  |