# Prompts para Sistema Facess - Controle de Chamada (Frequência) via Reconhecimento Facial

## Visão Geral do Sistema

Sistema web desenvolvido com Django (backend) e frontend servido por templates Django com Bootstrap 5 e Tailwind CSS, utilizando PostgreSQL. O objetivo é controle de chamada (frequência) de alunos por reconhecimento facial. O sistema inclui gestão de usuários (alunos, professores, secretária, coordenação, administração), estruturas acadêmicas (escola, curso, unidade curricular/matéria, série, turno, sala com sigla), dispositivos de reconhecimento facial (associados a salas) e registros de presença, além de auditoria/relatórios.

## Processos do Sistema Facess

### 1. Processo de Cadastro de Usuários
- **Cadastro inicial**: Secretaria/Administrador cadastra alunos, professores e demais perfis no sistema
- **Atribuição de perfil**: Usuário recebe um perfil específico (Aluno, Professor, Secretária, Coordenação, Admin)
- **Coleta biométrica**: Usuário tem suas características faciais capturadas e processadas
- **Validação**: Sistema valida a qualidade da imagem facial e armazena os dados biométricos
- **Ativação**: Usuário fica ativo no sistema e pode usar o reconhecimento facial

### 2. Processo de Registro de Presença (Chamada)
- **Aproximação**: Aluno se aproxima do dispositivo de reconhecimento facial na sala
- **Captura**: Câmera captura imagem facial em tempo real
- **Processamento**: Sistema processa a imagem e compara com banco de dados
- **Identificação**: Sistema identifica o aluno (ou falha na identificação)
- **Validação de contexto**: Sistema valida se há aula ativa para aquela sala/unidade curricular/horário
- **Registro de presença**: Marca status de presença (Presente, Falta, Atraso, Justificada) conforme regras
- **Registro de log**: Todas as tentativas são registradas (sucesso ou falha)

### 3. Processo de Gestão de Perfis e Permissões
- **Criação de perfis**: Admin cria perfis (Aluno, Professor, Secretária, Coordenação, Admin)
- **Definição de permissões**: Cada perfil recebe permissões específicas (acesso a módulos, operações de chamada)
- **Atribuição a usuários**: Usuários são associados a perfis
- **Alteração dinâmica**: Permissões podem ser alteradas em tempo real
- **Auditoria**: Todas as mudanças de perfil/permissões são logadas

### 4. Processo Acadêmico e de Agenda
- **Estruturas**: Cadastro de Escola, Curso, Unidade Curricular (Matéria), Série, Turno e Sala (com sigla única)
- **Horários**: Definição de horários de aulas por Unidade Curricular/Sala/Professor
- **Calendário**: Gerenciamento de calendário letivo, feriados e reposições
- **Associação**: Alunos associados às unidades curriculares e horários correspondentes

### 5. Processo de Monitoramento e Relatórios
- **Coleta de dados**: Sistema coleta todos os eventos de presença em tempo real
- **Relatórios de frequência**: Geração automática de relatórios por aluno, turma lógica (curso/série/turno/UC), sala e período
- **Alertas**: Sistema gera alertas para padrões anômalos (ausências repetidas, dispositivo offline)
- **Dashboard em tempo real**: Interface mostra aulas ativas, presença em andamento, status de dispositivos
- **Histórico**: Manutenção completa do histórico de presenças para auditoria e conformidade

### 6. Processo de Gestão de Dispositivos
- **Cadastro de dispositivos**: Registro de câmeras e leitores faciais no sistema
- **Associação a salas**: Dispositivos vinculados a salas (sigla) e contexto acadêmico
- **Monitoramento de status**: Verificação contínua do funcionamento dos dispositivos
- **Manutenção**: Processo de manutenção preventiva e corretiva
- **Sincronização**: Sincronização de dados entre dispositivos e servidor central

### 7. Processo de Segurança e Backup
- **Criptografia**: Todos os dados biométricos são criptografados
- **Backup automático**: Sistema realiza backups periódicos dos dados
- **Recuperação**: Processo de recuperação em caso de falhas
- **Auditoria de segurança**: Logs de segurança e tentativas de acesso ao sistema
- **Conformidade LGPD**: Processos para garantir conformidade com proteção de dados

## Instruções Gerais para IA

**IMPORTANTE - RESTRIÇÕES OBRIGATÓRIAS:**
- Execute APENAS a tarefa solicitada especificamente
- NÃO modifique código existente que já funciona
- NÃO adicione funcionalidades não solicitadas
- NÃO altere configurações de banco de dados existentes
- NÃO modifique arquivos de configuração (settings.py) sem solicitação explícita
- SEMPRE confirme qual parte específica do sistema deve ser implementada antes de começar
- Se houver código existente, preserve sua funcionalidade
- Implemente apenas incrementalmente conforme solicitado

## Melhorias Arquiteturais e Não Funcionais Recomendadas

Para tornar o sistema mais robusto, seguro e escalável, as seguintes melhorias são recomendadas e poderão ser incorporadas nos prompts conforme indicado:

- Assíncrono e filas: Celery + Redis/RabbitMQ para processamento de reconhecimento, relatórios e integrações, com retries e idempotência.
- Event-driven: publicar eventos de presença/reconhecimento; consumidores geram logs/alertas/relatórios.
- Armazenamento de imagens em objeto: MinIO/S3 para imagens; Postgres guarda metadados/URLs.
- Criptografia de campos sensíveis: templates biométricos e CPF com rotação de chaves (KMS quando possível).
- Políticas de retenção: expurgo automático de imagens e dados conforme base legal (LGPD) e configuração por tipo de dado.
- Autenticação forte de dispositivos: mTLS ou tokens de curta duração com rotação e vinculação por dispositivo.
- Controles de acesso: RBAC + ABAC (por atributos de contexto acadêmico e horário) com auditoria.
- Observabilidade: métricas (Prometheus/Grafana), logs e rastreamento (OpenTelemetry), Sentry para erros.
- Particionamento/índices: logs e presenças com partições por data e índices por escola/curso/sala/data.
- Versionamento de API e contrato: OpenAPI/Swagger, paginação/filtros, erros padronizados, rate limits.
- Tempo real: WebSocket (Django Channels + Redis) ou SSE para aulas ativas, presença e alertas.
- Entregabilidade: Docker/Compose (Postgres, Redis, MinIO), CI/CD com lint/testes/scan de segurança.
- Seeds/fixtures: dados de exemplo (perfis, cursos, UCs, salas, horários) e imagens sintéticas para testes.

---

# PROMPTS DE DESENVOLVIMENTO

## PROMPT 01: Configuração Inicial do Projeto

**Objetivo**: Criar a estrutura inicial de um projeto Django chamado "facess" para sistema de controle de chamada (frequência) via reconhecimento facial, com backend Django e frontend por templates Django usando Bootstrap 5 e Tailwind CSS (sem React).

```
Crie a estrutura inicial de um projeto Django chamado "facess" para sistema de controle de chamada (frequência) via reconhecimento facial, com backend Django e frontend por templates Django usando Bootstrap 5 e Tailwind CSS (sem React).

RESTRIÇÕES:
- Configure apenas o projeto backend base
- Não implemente modelos ainda
- Use as seguintes configurações obrigatórias:
  - Django 4.2+
  - Django REST Framework para API
  - PostgreSQL como banco de dados
  - Configuração para timezone 'America/Sao_Paulo'
  - Idioma pt-br
  - DEBUG=True para desenvolvimento
  - Frontend via templates Django com Bootstrap 5 e Tailwind CSS
  - CORS opcional (apenas se necessário para dispositivos externos)

ESTRUTURA ESPERADA:
- requirements.txt com dependências mínimas (Django, DRF, psycopg2, Pillow, django-environ)
- Dependências recomendadas (para futuras funcionalidades): Celery, redis, django-channels, channels-redis, django-cors-headers (opcional), boto3/minio para storage de imagens
- settings.py configurado para PostgreSQL, DRF, idioma/timezone e staticfiles
- Configuração inicial de Tailwind/Bootstrap para uso nos templates (estrutura de static/ e base.html)
- urls.py principal preparado para API
- Configuração Channels/ASGI preparada (sem implementação de consumers ainda)
- Docker Compose recomendado (opcional) com serviços de Postgres, Redis e MinIO
- Não crie apps ainda

CONFIRME: Está claro que deve criar apenas a estrutura base do projeto Django com DRF e templates (Bootstrap/Tailwind), sem React?
```

## PROMPT 02: App de Usuários, Perfis e Permissões

**Objetivo**: Criar um app Django chamado "usuarios" para gerenciar autenticação, perfis (Aluno, Professor, Secretária, Coordenação, Admin) e sistema de permissões.

```
Crie um app Django chamado "usuarios" para gerenciar autenticação, perfis e sistema de permissões.

RESTRIÇÕES:
- Implemente APENAS este app
- Não modifique outros apps existentes
- Use AbstractUser como base

REQUISITOS ESPECÍFICOS:
1. Model CustomUser estendendo AbstractUser com:
   - cpf (CharField, max_length=14, unique=True)
   - telefone (CharField, max_length=20, blank=True)
   - foto_perfil (ImageField, blank=True)
   - ativo (BooleanField, default=True)
   - data_criacao (DateTimeField, auto_now_add=True)
   - data_atualizacao (DateTimeField, auto_now=True)
   - tipo_usuario (CharField com choices: ALUNO, PROFESSOR, SECRETARIA, COORDENACAO, ADMIN)
   - escola_padrao (ForeignKey para Escola, null=True, blank=True)  # será criado no app acadêmico

2. Model PerfilAcesso:
   - nome (CharField, max_length=100, unique=True)
   - descricao (TextField, blank=True)
   - ativo (BooleanField, default=True)
   - data_criacao (DateTimeField, auto_now_add=True)

3. Model Permissao:
   - nome (CharField, max_length=100)
   - codigo (CharField, max_length=50, unique=True)
   - descricao (TextField, blank=True)
   - ativa (BooleanField, default=True)

4. Model PerfilPermissao (ManyToMany):
   - perfil (ForeignKey para PerfilAcesso)
   - permissao (ForeignKey para Permissao)
   - data_atribuicao (DateTimeField, auto_now_add=True)

5. Model UsuarioPerfil:
   - usuario (ForeignKey para CustomUser)
   - perfil (ForeignKey para PerfilAcesso)
   - data_atribuicao (DateTimeField, auto_now_add=True)
   - ativo (BooleanField, default=True)

6. Admin personalizado para todos os models
7. DRF ViewSets e Serializers básicos

SEGURANÇA (recomendado):
- Criptografia de campo para CPF e templates biométricos (quando integrados)
- Auditoria de alterações (django-simple-history ou equivalente)

CONFIRME: Deve criar apenas o app de usuários com sistema de perfis e permissões?
```

## PROMPT 03: App Acadêmico (Escola/Curso/Sala/UC/Turno/Série) e Dispositivos

**Objetivo**: Criar um app Django chamado "academico" para gerenciar estruturas acadêmicas e dispositivos de reconhecimento facial associados às salas.

```
Crie um app Django chamado "academico" para gerenciar estruturas acadêmicas e dispositivos de reconhecimento facial associados às salas.

RESTRIÇÕES:
- Implemente APENAS este app
- Não modifique apps existentes
- Não altere configurações do projeto

REQUISITOS ESPECÍFICOS:
1. Model Escola:
   - nome (CharField, max_length=200)
   - codigo (CharField, max_length=50, unique=True)
   - endereco (TextField, blank=True)
   - ativa (BooleanField, default=True)
   - data_criacao (DateTimeField, auto_now_add=True)

2. Model Curso:
   - escola (ForeignKey para Escola)
   - nome (CharField, max_length=200)
   - codigo (CharField, max_length=50)
   - ativo (BooleanField, default=True)

3. Model UnidadeCurricular:
   - curso (ForeignKey para Curso)
   - nome (CharField, max_length=200)
   - codigo (CharField, max_length=50)
   - ativa (BooleanField, default=True)

4. Model Serie:
   - curso (ForeignKey para Curso)
   - nome (CharField, max_length=50)  # ex: 1º, 2º, 3º ano
   - ativa (BooleanField, default=True)

5. Model Turno:
   - nome (CharField, max_length=50)  # ex: Manhã, Tarde, Noite
   - ativo (BooleanField, default=True)

6. Model Sala:
   - escola (ForeignKey para Escola)
   - sigla (CharField, max_length=20, unique=True)
   - descricao (CharField, max_length=200, blank=True)
   - capacidade (PositiveIntegerField, null=True, blank=True)
   - ativa (BooleanField, default=True)

7. Model DispositivoReconhecimento:
   - nome (CharField, max_length=100)
   - sala (ForeignKey para Sala)
   - ip_endereco (GenericIPAddressField)
   - porta (PositiveIntegerField, default=80)
   - modelo (CharField, max_length=100)
   - status (CharField com choices: ONLINE, OFFLINE, MANUTENCAO)
   - ativo (BooleanField, default=True)
   - data_instalacao (DateTimeField)
   - ultima_comunicacao (DateTimeField, null=True, blank=True)

8. Model HorarioAula:
   - unidade_curricular (ForeignKey para UnidadeCurricular)
   - professor (ForeignKey para CustomUser, limitando a PROFESSOR)
   - sala (ForeignKey para Sala)
   - dia_semana (IntegerField, choices: 0-6 para seg-dom)
   - horario_inicio (TimeField)
   - horario_fim (TimeField)
   - turno (ForeignKey para Turno)
   - serie (ForeignKey para Serie)
   - ativo (BooleanField, default=True)

9. Admin para todos os models
10. DRF ViewSets e Serializers

MELHORIAS (recomendadas):
- Heartbeat de dispositivos e monitoramento básico
- Índices em (escola, sala, dia_semana, horario_inicio)

CONFIRME: Deve implementar apenas o app acadêmico e dispositivos conforme especificado?
```

## PROMPT 04: App de Biometria Facial

**Objetivo**: Criar um app Django chamado "biometria" para gerenciar dados biométricos faciais e reconhecimento para presença.

```
Crie um app Django chamado "biometria" para gerenciar dados biométricos faciais e reconhecimento.

RESTRIÇÕES:
- Implemente APENAS este app
- Não modifique apps existentes
- Mantenha relacionamentos apenas com apps já criados

REQUISITOS ESPECÍFICOS:
1. Model DadosBiometricos:
   - usuario (OneToOneField para CustomUser)
   - encoding_facial (TextField)  # Dados codificados da face
   - qualidade_imagem (FloatField)  # Score de qualidade da captura
   - data_cadastro (DateTimeField, auto_now_add=True)
   - data_atualizacao (DateTimeField, auto_now=True)
   - ativo (BooleanField, default=True)

2. Model ImagemFacial:
   - dados_biometricos (ForeignKey para DadosBiometricos)
   - imagem (ImageField)
   - tipo (CharField com choices: CADASTRO, ATUALIZACAO, VERIFICACAO)
   - qualidade (FloatField)
   - data_captura (DateTimeField, auto_now_add=True)

3. Model TentativaReconhecimento:
   - dispositivo (ForeignKey para DispositivoReconhecimento)
   - usuario_identificado (ForeignKey para CustomUser, null=True, blank=True)
   - sala (ForeignKey para Sala)
   - imagem_capturada (ImageField)
   - score_confianca (FloatField)
   - sucesso (BooleanField)
   - data_tentativa (DateTimeField, auto_now_add=True)

4. Model ConfiguracaoReconhecimento:
   - threshold_confianca (FloatField, default=0.8)
   - max_tentativas_por_minuto (PositiveIntegerField, default=10)
   - timeout_reconhecimento (PositiveIntegerField, default=30)  # segundos
   - salvar_imagens_falha (BooleanField, default=True)
   - ativa (BooleanField, default=True)

5. Admin para todos os models
6. DRF ViewSets e Serializers
7. Utils para processamento de imagens faciais

SEGURANÇA E LGPD (recomendado):
- Armazenar imagens em MinIO/S3 e criptografar templates
- Políticas de retenção diferenciadas por tipo (verificação vs cadastro)

CONFIRME: Deve implementar apenas o app de biometria facial conforme especificado?
```

## PROMPT 05: App de Frequência e Logs

**Objetivo**: Criar um app Django chamado "frequencia" para gerenciar todas as presenças/ausências e um app "logs" (ou módulo dentro de frequencia) para auditoria do sistema.

```
Crie um app Django chamado "frequencia" para gerenciar todos os registros de presença e um módulo de logs de auditoria do sistema.

RESTRIÇÕES:
- Implemente APENAS este app
- Não modifique apps existentes
- Use relacionamentos apenas com apps já criados

REQUISITOS ESPECÍFICOS:
1. Model AulaAtiva:
   - horario_aula (ForeignKey para HorarioAula)
   - sala (ForeignKey para Sala)
   - inicio (DateTimeField)
   - fim (DateTimeField, null=True, blank=True)
   - status (CharField com choices: EM_ANDAMENTO, ENCERRADA, CANCELADA)

2. Model RegistroPresenca:
   - aula (ForeignKey para AulaAtiva)
   - aluno (ForeignKey para CustomUser, limitando a ALUNO)
   - dispositivo (ForeignKey para DispositivoReconhecimento)
   - status (CharField com choices: PRESENTE, FALTA, ATRASO, JUSTIFICADA)
   - data_hora (DateTimeField, auto_now_add=True)
   - imagem_captura (ImageField, blank=True)
   - score_confianca (FloatField, null=True, blank=True)
   - duracao_processo (FloatField, null=True, blank=True)
   - origem (CharField, max_length=30, default='FACIAL')  # ex: FACIAL, MANUAL, IMPORTADO

3. Model JustificativaFalta:
   - registro (ForeignKey para RegistroPresenca)
   - motivo (TextField)
   - anexos (FileField, blank=True)
   - aprovado (BooleanField, default=False)
   - avaliado_por (ForeignKey para CustomUser, null=True, blank=True)
   - data_avaliacao (DateTimeField, null=True, blank=True)

4. Model LogSistema:
   - usuario_sistema (ForeignKey para CustomUser, null=True, blank=True)
   - acao (CharField, max_length=100)
   - modulo (CharField, max_length=50)
   - detalhes (TextField, blank=True)
   - ip_origem (GenericIPAddressField)
   - data_hora (DateTimeField, auto_now_add=True)
   - nivel (CharField com choices: INFO, WARNING, ERROR, CRITICAL)

5. Model AlertaOperacional:
   - titulo (CharField, max_length=200)
   - descricao (TextField)
   - tipo (CharField com choices: AUSENCIAS_REPETIDAS, DISPOSITIVO_OFFLINE, MULTIPLAS_TENTATIVAS)
   - sala (ForeignKey para Sala, null=True, blank=True)
   - dispositivo (ForeignKey para DispositivoReconhecimento, null=True, blank=True)
   - data_criacao (DateTimeField, auto_now_add=True)
   - resolvido (BooleanField, default=False)
   - resolvido_por (ForeignKey para CustomUser, null=True, blank=True)
   - data_resolucao (DateTimeField, null=True, blank=True)

6. Admin para todos os models
7. DRF ViewSets e Serializers
8. Métodos para geração de estatísticas e relatórios (por aluno, UC, sala, período)

MELHORIAS (recomendadas):
- Particionamento por data e índices em (aluno, sala, data_hora)
- Retenção e expurgo configuráveis por tipo de registro

CONFIRME: Deve implementar apenas o app de frequência e logs conforme especificado?
```

## PROMPT 06: App de Processamento de Reconhecimento

**Objetivo**: Criar um app Django chamado "reconhecimento" para processar e gerenciar o reconhecimento facial em tempo real para chamada.

```
Crie um app Django chamado "reconhecimento" para processar e gerenciar o reconhecimento facial em tempo real.

RESTRIÇÕES:
- Implemente APENAS este app
- Não modifique apps existentes
- Use apenas bibliotecas de processamento de imagem

REQUISITOS ESPECÍFICOS:
1. Model SessaoReconhecimento:
   - dispositivo (ForeignKey para DispositivoReconhecimento)
   - usuario_identificado (ForeignKey para CustomUser, null=True, blank=True)
   - status (CharField com choices: PROCESSANDO, SUCESSO, FALHA, TIMEOUT)
   - inicio_processo (DateTimeField, auto_now_add=True)
   - fim_processo (DateTimeField, null=True, blank=True)
   - tempo_processamento (FloatField, null=True, blank=True)

2. Model FilaProcessamento:
   - dispositivo (ForeignKey para DispositivoReconhecimento)
   - imagem_capturada (ImageField)
   - prioridade (IntegerField, default=1)
   - status (CharField com choices: AGUARDANDO, PROCESSANDO, CONCLUIDO, ERRO)
   - data_criacao (DateTimeField, auto_now_add=True)
   - data_processamento (DateTimeField, null=True, blank=True)
   - resultado (TextField, blank=True)

3. Model ConfiguracaoProcessamento:
   - max_processos_simultaneos (PositiveIntegerField, default=5)
   - timeout_processamento (PositiveIntegerField, default=30)
   - qualidade_minima_imagem (FloatField, default=0.7)
   - limpar_fila_apos_horas (PositiveIntegerField, default=24)
   - ativa (BooleanField, default=True)

4. Services para:
   - Processamento de imagens faciais
   - Comparação biométrica
   - Gerenciamento de fila (Celery/Redis)
   - Comunicação com dispositivos
   - Publicação de eventos de presença processada

5. Admin para todos os models
6. DRF ViewSets para integração
7. Tasks assíncronas para processamento

MELHORIAS (recomendadas):
- Retries com backoff e idempotência por imagem/processo
- Métricas de FAR/FRR, distribuição de scores e alarmes de drift

CONFIRME: Deve implementar apenas o app de processamento de reconhecimento conforme especificado?
```

## PROMPT 07: API e Integração com Dispositivos

**Objetivo**: Criar um app Django chamado "api" para gerenciar APIs e integração com dispositivos externos para presença.

```
Crie um app Django chamado "api" para gerenciar APIs e integração com dispositivos externos.

RESTRIÇÕES:
- Implemente APENAS este app
- Este é o app principal para comunicação externa
- Use relacionamentos apenas com apps já criados

REQUISITOS ESPECÍFICOS:
1. ViewSets DRF para todas as entidades:
   - DispositivoReconhecimentoViewSet
   - UsuarioViewSet (dados básicos)
   - RegistroPresencaViewSet
   - TentativaReconhecimentoViewSet
   - AulaAtivaViewSet (listar/abrir/encerrar)

2. API Endpoints específicos:
   - POST /api/reconhecimento/processar/  # recebe imagem para processar presença
   - GET/PUT /api/dispositivos/status/   # status dos dispositivos
   - POST /api/frequencia/registrar/     # registra presença manual ou via integração
   - GET  /api/aulas/ativas/             # aulas em andamento por sala/UC
   - GET/POST /api/usuarios/biometria/   # dados biométricos

3. Serializers customizados:
   - DispositivoSerializer
   - ReconhecimentoSerializer
   - RegistroPresencaSerializer
   - AulaAtivaSerializer
   - UsuarioBasicoSerializer

4. Autenticação e permissões:
   - Autenticação por token forte ou mTLS para dispositivos
   - Permissões por tipo de endpoint e perfil (Aluno, Professor, Secretaria, Coordenação, Admin)
   - Rate limiting para APIs públicas e por dispositivo
   - Idempotency-Key para endpoints de registro de presença

5. WebSocket para comunicação em tempo real:
   - Status de dispositivos
   - Notificações de presença e aulas ativas
   - Alertas operacionais

6. Middleware para:
   - Logging de todas as requisições
   - Validação de dispositivos autorizados
   - Controle de rate limiting
   - Correlação de requisições (trace ID)

7. Contrato e versionamento de API:
   - OpenAPI/Swagger documentado e versionado (v1)
   - Padrão de erros, paginação, filtros por escola/curso/sala/período

CONFIRME: Deve implementar apenas o app de API e integração conforme especificado?
```

    ## PROMPT 08: Frontend React - Configuração Inicial

    **Objetivo**: Criar a estrutura inicial do frontend React para o sistema Facess.

    ```
    Crie a estrutura inicial do frontend React para o sistema Facess.

    RESTRIÇÕES:
    - Crie APENAS a estrutura base do React
    - Não implemente funcionalidades complexas ainda
    - Use bibliotecas modernas e padrões atuais

    REQUISITOS ESPECÍFICOS:
    1. Configuração do projeto React:
    - Create React App ou Vite
    - TypeScript configurado
    - Axios para requisições HTTP
    - React Router para navegação
    - Material-UI ou Ant Design para componentes

    2. Estrutura de pastas:
    - /src/components (componentes reutilizáveis)
    - /src/pages (páginas principais)
    - /src/services (chamadas API)
    - /src/hooks (hooks customizados)
    - /src/contexts (contexts para estado global)
    - /src/utils (utilitários)

    3. Configuração inicial:
    - Arquivo de configuração de ambiente (.env)
    - Configuração do Axios base
    - Roteamento básico
    - Layout principal com header e sidebar

    4. Páginas básicas (apenas estrutura):
    - Login
    - Dashboard
    - Usuários
    - Locais
    - Dispositivos
    - Logs

    5. Componentes base:
    - Header
    - Sidebar
    - Loading
    - ErrorBoundary

    CONFIRME: Deve criar apenas a estrutura base do frontend React?
```

## PROMPT 09: Frontend React - Páginas Principais

**Objetivo**: Implementar as páginas principais do sistema Facess em React.

```
Implemente as páginas principais do sistema Facess em React.

RESTRIÇÕES:
- Implemente APENAS as páginas listadas
- Use componentes já criados na estrutura base
- Não implemente funcionalidades de edição ainda

REQUISITOS ESPECÍFICOS:
1. Página de Login:
   - Formulário de login com validação
   - Integração com API de autenticação
   - Redirecionamento após login
   - Tratamento de erros

2. Dashboard Principal:
   - Cards com estatísticas gerais
   - Gráficos de acessos por período
   - Lista de alertas recentes
   - Status dos dispositivos em tempo real
   - Últimos acessos

3. Página de Usuários:
   - Listagem de usuários com filtros
   - Busca por nome, CPF, perfil
   - Indicadores de status (ativo/inativo)
   - Modal para visualizar detalhes

4. Página de Locais:
   - Listagem de locais
   - Filtros por tipo e status
   - Indicadores de dispositivos por local
   - Mapa/layout dos locais (se possível)

5. Página de Dispositivos:
   - Lista de dispositivos com status
   - Filtros por local e status
   - Indicadores de conectividade
   - Última comunicação

6. Página de Logs de Acesso:
   - Listagem de logs com filtros
   - Filtros por data, usuário, local
   - Paginação
   - Exportação de dados

7. Serviços API (services):
   - authService
   - usuariosService
   - locaisService
   - dispositivosService
   - logsService

CONFIRME: Deve implementar apenas as páginas principais conforme especificado?
```

## PROMPT 10: Sistema de Relatórios e Analytics

**Objetivo**: Implementar sistema de relatórios e analytics para o sistema Facess.

```
Implemente sistema de relatórios e analytics para o sistema Facess.

RESTRIÇÕES:
- Implemente APENAS funcionalidades de relatórios
- Não modifique estrutura de banco existente
- Use bibliotecas adequadas para geração de relatórios

REQUISITOS ESPECÍFICOS:
1. Backend - App "relatorios":
   - Views para geração de dados estatísticos
   - Endpoints para diferentes tipos de relatórios
   - Serializers para dados de relatórios
   - Utils para processamento de dados

2. Relatórios Disponíveis:
   - Relatório de acessos por usuário (período customizável)
   - Relatório de acessos por local (com gráficos)
   - Relatório de tentativas não autorizadas
   - Relatório de status de dispositivos
   - Relatório de alertas de segurança

3. Frontend React - Páginas de Relatórios:
   - Página de seleção de relatórios
   - Filtros avançados (datas, usuários, locais)
   - Visualização de dados com gráficos (Chart.js ou D3)
   - Exportação para PDF, Excel, CSV
   - Agendamento de relatórios (futuro)

4. Funcionalidades de Analytics:
   - Gráficos de pizza, linha e barra
   - Tabelas interativas
   - Métricas em tempo real
   - Comparativos entre períodos

5. Exportação:
   - PDF com formatação profissional
   - Excel com múltiplas abas
   - CSV para análises externas
   - Envio por email (futuro)

CONFIRME: Deve implementar apenas o sistema de relatórios e analytics conforme especificado?
```

---

## Notas Importantes

### Para o Desenvolvedor IA:
- **SEMPRE** pergunte qual parte específica implementar antes de começar
- **NUNCA** assuma que deve implementar todo o sistema de uma vez
- **SEMPRE** preserve código existente e funcional
- **CONFIRME** os requisitos antes de cada implementação
- **TESTE** cada parte antes de considerar concluída

### Ordem Sugerida de Implementação:
1. Configuração inicial do projeto Django + DRF
2. App usuarios (usuários, perfis e permissões)
3. App locais (locais e dispositivos)
4. App biometria (dados biométricos e reconhecimento)
5. App logs (logs de acesso e auditoria)
6. App reconhecimento (processamento facial)
7. App api (APIs e integração)
8. Frontend React - estrutura base
9. Frontend React - páginas principais
10. Sistema de relatórios e analytics

### Comandos Úteis Backend:
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações  
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor Django
python manage.py runserver

# Executar testes
python manage.py test
```

### Comandos Úteis Frontend:
```bash
# Criar projeto React
npx create-react-app facess-frontend --template typescript
# ou
npm create vite@latest facess-frontend -- --template react-ts

# Instalar dependências
npm install

# Executar servidor de desenvolvimento
npm start
# ou
npm run dev

# Build para produção
npm run build
```

### Tecnologias Principais:
- **Backend**: Django 4.2+, Django REST Framework, PostgreSQL
- **Frontend**: React 18+, TypeScript, Material-UI/Ant Design
- **Reconhecimento Facial**: OpenCV, face_recognition, dlib
- **Comunicação**: WebSockets, REST API
- **Relatórios**: Chart.js, jsPDF, xlsx
