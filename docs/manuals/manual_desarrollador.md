# Manual de Desarrollador

Este manual proporciona las pautas para contribuir y mantener el proyecto SENA_TEST.

## Estructura del proyecto
- `src/`: Código fuente principal (API, servicios, modelos, utilidades)
- `docs/`: Documentación y manuales
- `tests/`: Pruebas unitarias e integrales
- `uml/`: Diagramas UML

## Convenciones de código
- Seguir PEP8 y las reglas en `docs/context/coding_rules.md`
- Usar nombres descriptivos para archivos, funciones y variables
- Documentar funciones y clases con docstrings

## Agregar nuevos endpoints o servicios
1. Crear el endpoint en `src/api/endpoints/`
2. Implementar la lógica en `src/services/`
3. Definir modelos y esquemas en `src/db/models.py` y `src/db/schemas.py`
4. Agregar pruebas en `tests/`

## Seguridad y buenas prácticas
- Usar JWT para autenticación
- Validar permisos en cada endpoint
- Cifrar contraseñas con bcrypt
- Manejar errores y registrar logs críticos

## Pruebas
- Escribir pruebas unitarias con pytest
- Mantener una cobertura mínima del 80%

## Contribución
- Usar ramas para nuevas funcionalidades o correcciones
- Hacer commits pequeños y descriptivos
- Documentar cambios relevantes en el README o en la documentación

---

Para dudas técnicas, consulte al líder de proyecto o revise la documentación en `docs/`.
