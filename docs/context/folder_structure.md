SENA_TEST/
├── LICENSE
├── README.md
├── docs/
│   ├── context/
│   │   ├── architecture.md
│   │   ├── coding_rules.md
│   │   ├── folder_structure.md
│   │   ├── raw_prd.md
│   │   ├── requirements_project.md
│   └── original_pdf/
│       └── REQUERIMIENTOS AGRO V3.pdf
├── src/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── inventory.py
│   │   │   ├── sales.py
│   │   │   ├── users.py
│   │   │   └── reports.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── __init__.py
│   ├── db/
│   │   ├── models/
│   │   │   ├── inventory.py
│   │   │   ├── sales.py
│   │   │   ├── users.py
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   ├── inventory.py
│   │   │   ├── sales.py
│   │   │   ├── users.py
│   │   │   └── __init__.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── inventory_service.py
│   │   ├── sales_service.py
│   │   ├── user_service.py
│   │   └── report_service.py
│   ├── utils/
│   │   ├── logger.py
│   │   ├── helpers.py
│   │   └── __init__.py
│   └── main.py
├── tests/
│   ├── unit/
│   │   ├── test_inventory.py
│   │   ├── test_sales.py
│   │   ├── test_users.py
│   │   └── test_reports.py
│   ├── integration/
│   │   ├── test_endpoints.py
│   │   └── test_database.py
│   └── __init__.py
├── uml/
└── requirements.txt


--------------------

> src/: Contiene el código fuente de la aplicación.

> api/: Define los endpoints de la API.
> core/: Configuración central del proyecto (e.g., configuración, seguridad).
> db/: Modelos, esquemas y conexión a la base de datos.
> services/: Lógica de negocio y servicios.
> utils/: Utilidades y funciones auxiliares.
>  main.py: Punto de entrada de la aplicación.
> tests/: Contiene las pruebas unitarias e integrales.

> unit/: Pruebas unitarias para cada módulo.
> integration/: Pruebas de integración para endpoints y base de datos.
> docs/: Documentación del proyecto.

> context/: Documentos contextuales como reglas de codificación y arquitectura.
> original_pdf/: Archivos PDF originales.
> uml/: Diagramas UML del proyecto.
> requirements.txt: Lista de dependencias del proyecto.
