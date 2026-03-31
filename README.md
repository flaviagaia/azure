# azure

## Português

Este repositório foi organizado como um monorepo de portfólio para projetos orientados a **Microsoft Azure**, separando implementações demonstráveis de blueprints arquiteturais.

### Organização do monorepo

```text
azure/
├── projects/
│   ├── azure_streaming/
│   │   └── payment_anomaly_stream_azure/
│   ├── azure_search/
│   │   └── enterprise_policy_search_azure/
│   ├── azure_workflows/
│   │   └── claims_approval_workflow_azure/
│   └── azure_blueprints/
├── src/
├── tests/
└── main.py
```

### Topologia técnica do repositório

O monorepo foi dividido para separar claramente:

- `projects/`
  Camada de domínio, contendo um diretório por projeto.
- `src/projects.py`
  Camada agregadora que coleta os outputs dos projetos implementados e produz um relatório consolidado.
- `main.py`
  Entry point do bundle, responsável por executar os casos implementados e persistir o artefato final.
- `tests/test_portfolio.py`
  Camada de regressão mínima para garantir integridade estrutural e presença dos principais indicadores.

### Projetos implementados

1. `payment_anomaly_stream_azure`
   Caso de uso orientado a eventos e streaming para monitoramento de pagamentos suspeitos.
2. `enterprise_policy_search_azure`
   Caso de uso de busca corporativa com foco em indexação e retrieval de políticas internas.
3. `claims_approval_workflow_azure`
   Caso de uso de workflow operacional para autoaprovação e fila de revisão manual.

### Semântica dos projetos implementados

- `payment_anomaly_stream_azure`
  Representa uma arquitetura orientada a eventos em que sinais de pagamento são ingeridos continuamente e analisados por uma camada de detecção de anomalia.
- `enterprise_policy_search_azure`
  Representa um serviço de knowledge retrieval corporativo, em que políticas internas são indexadas e recuperadas por similaridade.
- `claims_approval_workflow_azure`
  Representa uma arquitetura de workflow operacional com regras de autoaprovação, desvio para revisão manual e integração entre sistemas.

### Blueprints adicionais

O repositório também inclui blueprints para:

- `loan-approval-mlops-azure`
- `document-lakehouse-azure`
- `customer-360-etl-azure`
- `risk-dashboard-webapp-azure`
- `financial-helpdesk-bot-azure`
- `product-defect-inspection-azure`

### Ferramentas Azure mapeadas

- `Azure Event Hubs`
- `Azure Stream Analytics`
- `Azure Machine Learning`
- `Azure AI Search`
- `App Service`
- `Azure SQL Database`
- `Logic Apps`
- `Azure Functions`
- `Blob Storage`
- `Azure Data Factory`
- `Azure Data Lake Storage`
- `Azure AI Bot Service`
- `Azure Custom Vision`
- `API Management`

### Tradução de workloads para Azure

Os projetos deste monorepo foram escolhidos para representar três famílias de workload comuns na plataforma:

- `streaming e detecção em tempo real`
  melhor representado por `Event Hubs + Stream Analytics + Azure Machine Learning`
- `search e knowledge retrieval`
  melhor representado por `Azure AI Search + App Service + Azure SQL Database`
- `workflow e automação operacional`
  melhor representado por `Logic Apps + Azure Functions + Blob Storage + API Management`

### Arquitetura Azure de referência

```mermaid
flowchart LR
    A["Applications / Devices / Uploads"] --> B["Event Hubs"]
    A --> C["Blob Storage"]
    B --> D["Stream Analytics"]
    C --> E["Azure AI Search"]
    C --> F["Data Factory"]
    D --> G["Azure SQL Database"]
    F --> G
    G --> H["Azure Machine Learning"]
    H --> I["App Service / Functions"]
    I --> J["API Management"]
    G --> K["Power BI"]
```

### O que cada ferramenta faz

- `Event Hubs`
  É o serviço de streaming de eventos da Azure.
  Serve para ingerir telemetria, transações, logs e sinais em tempo real em alto volume.
- `Stream Analytics`
  É o motor de processamento contínuo de streams da Azure.
  Serve para aplicar regras, agregações, janelas temporais e detecção operacional em eventos que chegam continuamente.
- `Azure Machine Learning`
  É a plataforma gerenciada de machine learning da Azure.
  Serve para treino, versionamento, registry, deployment e monitoramento de modelos.
- `Azure AI Search`
  É o serviço de busca e indexação corporativa da Azure.
  Serve para indexar documentos, FAQs, políticas e bases internas, permitindo retrieval textual e semântico.
- `App Service`
  É a plataforma gerenciada para hospedar aplicações web.
  Serve para publicar frontends, backends e APIs com operação simplificada.
- `Azure SQL Database`
  É o banco relacional gerenciado da Azure.
  Serve para armazenar dados estruturados em aplicações transacionais e em workloads analíticos menores.
- `Logic Apps`
  É a ferramenta de orquestração low-code/no-code da Azure.
  Serve para montar workflows de integração, aprovação e automação entre sistemas.
- `Azure Functions`
  É o serviço serverless baseado em funções.
  Serve para executar lógica sob demanda em resposta a eventos, timers, filas e triggers HTTP.
- `Blob Storage`
  É a camada de object storage da Azure.
  Serve para guardar arquivos, documentos, imagens, modelos e artefatos brutos.
- `Azure Data Factory`
  É o serviço de integração e orquestração de dados da Azure.
  Serve para ETL/ELT, movimentação de dados e integração entre fontes distintas.
- `Azure Data Lake Storage`
  É a camada de armazenamento analítico em escala da Azure.
  Serve para organizar dados brutos e curados em arquitetura de data lake ou lakehouse.
- `Azure AI Bot Service`
  É o serviço de construção e operação de bots conversacionais da Azure.
  Serve para conectar bots a canais, fluxos conversacionais e serviços cognitivos.
- `Azure Custom Vision`
  É um serviço de visão computacional customizável da Azure.
  Serve para treinar classificadores e detectores visuais voltados a imagens específicas do negócio.
- `API Management`
  É a camada de governança de APIs da Azure.
  Serve para publicar APIs com autenticação, rate limit, versionamento, documentação e controle de consumo.

### Como ler essa arquitetura

Em termos de camadas, o desenho pode ser entendido assim:

- `ingestão`
  `Event Hubs` e `Blob Storage`
- `processamento e integração`
  `Stream Analytics`, `Logic Apps`, `Azure Functions` e `Azure Data Factory`
- `armazenamento e consulta`
  `Azure SQL Database` e `Azure Data Lake Storage`
- `IA e busca`
  `Azure Machine Learning`, `Azure AI Search`, `Azure AI Bot Service` e `Azure Custom Vision`
- `exposição e consumo`
  `App Service`, `API Management` e `Power BI`

### Contrato do artefato consolidado

O bundle salva um artefato unificado em:

- `data/processed/azure_portfolio_report.json`

Cada item do relatório contém, no mínimo:

- `project_name`
- lista de `azure_services`
- métricas centrais do caso de uso

Exemplos:

- streaming:
  - `events_processed`
  - `anomaly_rate`
  - `precision`
  - `recall`
- search:
  - `documents_indexed`
  - `top_match_doc_id`
  - `top_match_score`
- workflow:
  - `claims_processed`
  - `auto_approved`
  - `manual_review_queue`
  - `auto_approval_rate`

### Leitura técnica do bundle

O objetivo aqui não é reproduzir o runtime gerenciado da Azure dentro do repositório, mas mostrar:

- decomposição arquitetural por tipo de workload;
- mapeamento entre problema de negócio e serviço cloud;
- implementação local mínima para validar a lógica do caso de uso;
- organização do portfólio em um formato fácil de escalar com novos projetos.

Isso torna o repositório útil tanto como demonstração prática quanto como blueprint de arquitetura.

### Execução

```bash
python3 main.py
python3 -m unittest discover -s tests -v
python3 -m py_compile main.py src/projects.py \
  projects/azure_streaming/payment_anomaly_stream_azure/project.py \
  projects/azure_search/enterprise_policy_search_azure/project.py \
  projects/azure_workflows/claims_approval_workflow_azure/project.py
```

### Artefato gerado

- `data/processed/azure_portfolio_report.json`

Esse arquivo é gerado em runtime e não é versionado.

### Referência oficial

- [Azure products](https://azure.microsoft.com/en-us/products)

---

## English

This repository is organized as an Azure-focused portfolio monorepo, separating implemented demo projects from architectural blueprints.

### Implemented projects

- `payment_anomaly_stream_azure`
- `enterprise_policy_search_azure`
- `claims_approval_workflow_azure`

### Repository topology

- `projects/`
  One folder per project, grouped by Azure workload family.
- `src/projects.py`
  Aggregation layer that executes the implemented projects and packages a single report.
- `main.py`
  Entry point that runs the bundle and persists the runtime artifact.
- `tests/test_portfolio.py`
  Regression layer for structural checks and output integrity.

### Implemented project semantics

- `payment_anomaly_stream_azure`
  Event-driven anomaly monitoring workload.
- `enterprise_policy_search_azure`
  Enterprise retrieval and search workload.
- `claims_approval_workflow_azure`
  Operational approval workflow workload.

### Additional blueprints

- `loan-approval-mlops-azure`
- `document-lakehouse-azure`
- `customer-360-etl-azure`
- `risk-dashboard-webapp-azure`
- `financial-helpdesk-bot-azure`
- `product-defect-inspection-azure`

### Core Azure services covered

- `Azure Event Hubs`
- `Azure Stream Analytics`
- `Azure Machine Learning`
- `Azure AI Search`
- `App Service`
- `Azure SQL Database`
- `Logic Apps`
- `Azure Functions`
- `Blob Storage`
- `Azure Data Factory`
- `Azure Data Lake Storage`
- `Azure AI Bot Service`
- `Azure Custom Vision`
- `API Management`

### What each Azure service is used for

- `Azure Event Hubs`
  Azure event streaming service.
  Used for high-volume ingestion of transactions, telemetry, and operational events.
- `Azure Stream Analytics`
  Azure stream processing engine.
  Used for continuous rules, aggregations, windowing, and near-real-time event analytics.
- `Azure Machine Learning`
  Azure managed ML platform.
  Used for training, registry, deployment, and operationalization of ML models.
- `Azure AI Search`
  Azure enterprise search and indexing layer.
  Used for document indexing, retrieval, and knowledge search workloads.
- `App Service`
  Azure managed web application hosting platform.
  Used to expose web apps, backends, and lightweight APIs.
- `Azure SQL Database`
  Azure managed relational database.
  Used for structured transactional storage and smaller analytical workloads.
- `Logic Apps`
  Azure workflow orchestration service.
  Used to automate integrations and approval-style business processes.
- `Azure Functions`
  Azure serverless execution model.
  Used for event-driven automation and lightweight backend logic.
- `Blob Storage`
  Azure object storage layer.
  Used for raw files, images, documents, and model artifacts.
- `Azure Data Factory`
  Azure data integration and orchestration platform.
  Used for ETL/ELT pipelines and source-to-source data movement.
- `Azure Data Lake Storage`
  Azure scalable analytical storage layer.
  Used for lakehouse-style raw and curated data zones.
- `Azure AI Bot Service`
  Azure bot-building service.
  Used for conversational assistants integrated with channels and enterprise workflows.
- `Azure Custom Vision`
  Azure custom computer vision service.
  Used for image classification and defect inspection scenarios.
- `API Management`
  Azure API governance layer.
  Used for secure publishing, throttling, versioning, and lifecycle control of APIs.

### How to read this architecture

The reference design can be interpreted in layers:

- `ingestion`
  `Event Hubs` and `Blob Storage`
- `processing and orchestration`
  `Stream Analytics`, `Logic Apps`, `Azure Functions`, and `Azure Data Factory`
- `storage and query`
  `Azure SQL Database` and `Azure Data Lake Storage`
- `AI and search`
  `Azure Machine Learning`, `Azure AI Search`, `Azure AI Bot Service`, and `Azure Custom Vision`
- `exposure and consumption`
  `App Service`, `API Management`, and `Power BI`

### Consolidated artifact contract

The monorepo writes:

- `data/processed/azure_portfolio_report.json`

Each project entry contains, at minimum:

- `project_name`
- `azure_services`
- workload-specific operational metrics

Typical examples:

- streaming:
  - `events_processed`
  - `anomaly_rate`
  - `precision`
  - `recall`
- search:
  - `documents_indexed`
  - `top_match_doc_id`
  - `top_match_score`
- workflow:
  - `claims_processed`
  - `auto_approved`
  - `manual_review_queue`
  - `auto_approval_rate`

### Technical positioning

The goal of this repository is not to emulate managed Azure runtime behavior locally. Instead, it is designed to show:

- architectural decomposition by workload family
- mapping between business problems and Azure services
- lightweight local implementations that validate the core logic
- a scalable monorepo structure for portfolio growth
