## Atualizar dados

| ITEM | VALUE |
| --- | --- |
| UseCase | Atualizar dados |
| Summary | Ação responsável pela atualização cadastral do usuário já existente no sistema. |
| Actor | Usuário |
| Precondition | 1. Estar cadastrado no sistema; <br> 2. Estar logado no sistema; <br> 3. Estar na página do perfil de usuário. |
| Postcondition | 1. O usuário terá seus dados atualizados. |
| Base Sequence | 1. O usuário irá entrar no seu perfil; <br> 2. O usuário irá optar por alterar seus dados; <br> 3. O usuário irá preencher os campos que deseja atualizar; <br> 4. O sistema irá validar os campos atualizados pelo usuário; <br> 5. O usuário terá seu cadastro atualizado.  |
| Branch Sequence | 1.1 Campos inválidos/em falta: <br> 1. Caso os campos atualizados pelo usuário sejam inválidos o sistema irá exibir uma mensagem de erro e o usuário terá que informá-los novamente. |
| Exception Sequence | 1. O usuário não poderá atualizar seus dados pois há campos inválidos/em falta. |
| Sub UseCase |  |
| Note |  |