1. Introducción  
Este documento contiene la especificación de requerimientos de software con la propuesta de desarrollo de una aplicación que le permita al personal encargado de la administración de la granja agrícola del SENA regional Risaralda automatizar los procesos de comercialización de los productos que allí se generan de forma eficiente y segura, garantizando la administración y control del sistema de inventario, reemplazando lo que actualmente se realiza de forma manual por un sistema de información.  

Para lograrlo, se propone el desarrollo e implementación de una aplicación que permita el registro, consulta, acceso y control del inventario que se maneja en la granja y que a la fecha no cuenta con ningún sistema que permita realizar dicha labor.  

Con el desarrollo y posterior implementación de esta aplicación se les permitirá a los administradores de la granja automatizar sus procesos y posicionarse acorde a las exigencias de los mercados actuales. Asimismo, hacia un futuro se podrán incluir nuevos módulos como el sistema de pagos en línea que facilitarán la comercialización de los productos.  

---

2. Justificación  
Actualmente, el SENA regional Risaralda cuenta con una sede agrícola en una vereda de Santa Rosa de Cabal. Allí se desarrollan procesos enmarcados en el sector agrícola, pecuario y servicios ambientales. De los procesos que allí se desarrollan se generan unidades productivas para administrar la producción del centro. Estas unidades funcionan con recursos SENA y lo que se genera allí nuevamente es invertido para el sostenimiento de dichas unidades.  

La venta y comercialización de los productos generados en la granja se realiza de forma manual. Esta administración no permite llevar un registro apropiado y detallado de la información, por lo que generar informes detallados y a tiempo no es posible.  

Todos los reportes se realizan de forma manual, por lo que no se cuenta con una sistematización para el manejo de los recursos. Se manejan registros de la información en hojas de cálculo de una forma básica que no permite la administración y el control adecuado de la producción.  

La sistematización de los procesos les permitirá a los usuarios gestionar las solicitudes de manera ágil y al personal de administración gestionar y controlar el inventario, lo cual también facilitará los procesos de comercialización y permitirá obtener respuestas sobre:  
- **Cuánto se vende**  
- **Cuáles son los productos con mayor demanda**  
- **Cuáles son las ventas por periodo y por producto**  
- **Cuánto hay en inventario**  
    - **Gráficos interactivos**: Representación visual de las ventas mediante gráficos de barras, líneas o circulares para facilitar la interpretación de datos.  
    - **Filtrado de información**: Opción de seleccionar periodos específicos y comparar ventas entre diferentes meses o años.  
    - **Exportación de datos**: Posibilidad de descargar informes en formatos como PDF o Excel para su análisis externo.  

**Beneficio esperado**  
Optimizar la gestión comercial mediante el análisis detallado del comportamiento de ventas, permitiendo identificar patrones, evaluar estrategias de negocio y tomar decisiones fundamentadas para mejorar la rentabilidad y la planificación de inventario.  

---

4. Diseño de la integración  

4.1 Arquitectura del sistema  

✔ **Modelo de arquitectura**:  
Arquitectura monolítica es un estilo de arquitectura de software en el que una aplicación se desarrolla como una sola unidad o componente indivisible. Tiene como característica el uso de una base de código única para sus servicios o funcionalidades. En este enfoque, todos los componentes y funcionalidades de la aplicación están interconectados y desplegados juntos como una sola entidad en un entorno de ejecución.  

En una arquitectura monolítica, la aplicación se compila y se despliega como un único archivo o un conjunto de archivos interdependientes. Todos los aspectos funcionales, como la lógica de negocio, la interfaz de usuario, el acceso a datos y otros servicios, están empaquetados y ejecutados dentro del mismo proceso.  

Los componentes de una arquitectura monolítica se comunican directamente entre sí a través de llamadas a funciones o métodos internos. La aplicación monolítica generalmente se ejecuta en un solo servidor o instancia, lo que significa que no hay una separación física o lógica entre los diferentes componentes de la aplicación.  

✔ **Diagrama UML de interacción**:  
- **Casos de uso**: Gestionar productos, Gestionar ventas, Generar facturas, Generar informes, Gestionar usuarios.  
- **Diagrama de secuencia**: Muestra el flujo entre los usuarios, la plataforma y los sistemas externos.  
- **Diagrama de componentes**: Define los módulos principales como base de datos y servicios. Proporciona una visión general del sistema y documenta la organización de los componentes del sistema y sus relaciones y dependencias mutuas.  

---

**Requerimientos adicionales**  
Luego de una segunda reunión con los stakeholders se agregaron los siguientes requerimientos:  
- **Módulo de Bodegas múltiples**: La sede principal controlará el inventario completo, pero se realizará la distribución de pequeños inventarios a diferentes sedes para poder comercializarlos. El número de sub-bodegas es ilimitado.  
- **Módulos de analítica**: Inicialmente para agrupamiento de productos más vendidos por características poblacionales y sector de la bodega. Para este requerimiento se requiere inicialmente un registro de todas las operaciones transaccionales en un histórico para su posterior procesamiento.  
- **Migración a aplicación móvil (app)**  

---

**Entrega**  
- Código fuente en repositorio, código en email (documentado, refactorizado, buenas prácticas, patrones de diseño).  
- Diagramas de clase, estados, secuencia, entidad-relación.  
- Manuales de usuario, manual de despliegue, manual de desarrollador.  
