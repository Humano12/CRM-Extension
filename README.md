# Boom Solutions CRM Extension

Módulo personalizado para Odoo V18 que extiende las capacidades del módulo nativo de Ventas CRM. Este desarrollo añade campos técnicos para la gestión de asignaciones, despacho de servicios y un flujo básico de aprobación de registros.

## Funcionalidades

* **Categorización de leads:** Clasificación en residencial, empresarial o gubernamental.
* **Control de instalaciones y soporte:** Registro dinámico de requerimientos técnicos postventa y fechas programadas de instalación.
* **Flujo de aprobación:** Botón integrado en la vista formulario que registra automáticamente el usuario aprobador, la fecha de aprobación y establece la fecha límite de entrega.
* **Cálculo de tiempos:** Campo computado que mide los días transcurridos desde la aprobación de la orden.
* **Historial y Chatter:** Seguimiento completo de los cambios y notas internas integrado a mano derecha del formulario.



## Instalación
1. Descargar o clonar el repositorio dentro de la carpeta de complementos del servidor
2. Activar el Modo Desarrollador
3. Actualizar lista de aplicaciones
4. Buscar: Boom Solutions CRM Extension y Activar.


## Cómo Probar el Módulo
1 Ingresar al modulo CRM 
2. Abre cualquiera de los leads
3.En la barra superior del formulario, haga clic en el botón **Aprobar Orden**. El botón desaparecerá instantáneamente para evitar duplicados.
   * Los campos *Aprobado por*, *Fecha de Aprobación* y *Fecha Límite de Entrega* se auto-completarán con su usuario y la fecha del día de hoy.
   * El contador *Días desde aprobación* se calculará automáticamente en tiempo real.