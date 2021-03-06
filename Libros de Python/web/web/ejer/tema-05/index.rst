
==========
Ejercicios
==========

-------------------------------
 *Tema 5:* Diseñando con Glade
-------------------------------

Mejoras en GFits
~~~~~~~~~~~~~~~~

Los ejercicios de esta sección son mejoras sobre el programa GFits que
hemos visto durante las clases del curso. Puedes descargarte el código
fuente de la versión inicial de la web de material del curso.

*Las soluciones de esta relación se encuentran todas implementadas en
la carpeta ``gfits2`` del código fuente del tema 5 en la sección de
recursos.*

#. Cambia la vista de las tablas del fichero FITS para que se puedan
   ordenar los datos por una columna y se pueda redimensionar el
   tamaño del campo.

   .. hint:: Todo el código que tienes que modificar está en el
      la clase ``FitsTablePage`` en el fichero ``src/doc.py``.

   .. hint:: Utiliza la propiedad ``resizable`` y el método
      ``set_sort_column_id`` de la clase ``TreeViewColumn``

#. Añade un díalogo ``about`` que muestre información general sobre el
   programa. Se recomienda crear definir el diálogo con Glade.

   .. hint:: Crea un nuevo fichero de interfaz ``src/gui/about.glade``
      con el diálogo de tipo ``about``.  Hay muchos campos que puedes
      editar.
   
   .. hint:: Conecta un manejador con la señal ``activate`` del botón
      adecuado del menú en ``src/gui/main.glade``. Recuerda que en la
      lista de objetos puedes pulsar botón derecho y ``Edit`` para
      acceder a los elementos del menú y sus señales.

   .. hint:: El el manejador, carga el fichero de interfaz con
      ``gtk.Builder``, busca el objeto del diálogo, invoca ``run ()``
      y recuerda destruirlo finalmente.

#. Añade una barra de navegación estándar de Matplotlib para asistir
   la visualización de la imagen.

   .. hint:: Todo el código que tienes que modificar está en el
      constructor de ``FitsImagePage`` en el fichero ``src/doc.py``.

   .. hint:: Aunque el segundo parámetro de la ``NavigationToolbar``
      parezca ser una ventana, basta con que establezcas el padre que
      del objeto.

   .. hint:: El objeto del fichero de interfaz en Glade
      ``image-container`` es ya de tipo ``gtk.VBox``, puedes
      simplemente usar ``pack_start``, asegurándote de pasarle los
      parámetros correctos según lo descrito en el curso.

#. La función ``imshow ()`` de un `matplotlib.axis.Axis
   <http://matplotlib.sourceforge.net/api/axis_api.html>`__ que usamos
   para representar la imagen puede usar diferentes funciones para
   mapear los valores de la matriz a píxeles de colores. Ahora, por
   defecto, se utiliza ``matplotlib.cm.gray``. La lista completa de
   opciones disponibles `la tienes aquí
   <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.colormaps>`__. Añade
   la posibilidad de cambiar la función utilizada con un menú
   desplegable en la barra de herramientas principal. 

   .. hint:: ``matplotlib.cm.cmap_d`` es un diccionario que contiene
      todos los mapas de color disponibles en Matplotlib.

   .. hint:: Todo el código que tienes que modificar está en el
      la clase ``FitsImagePage`` en el fichero ``src/doc.py`` y el
      fichero glade ``src/gui/primary.glade``.

   .. hint:: La barra de herramientas principal es el objeto
      ``primary-toolbar`` en el fichero ``primary.glade``, añade otro
      ``ComboBox`` de forma similar al que ya hay. Es un elemento de
      la barra herramientas de tipo *especial*, lo cual te provee un
      hueco en el que puedes añadir directamente el *widget* que te de
      la gana.

   .. hint:: Glade no es capaz de editar la lista de opciones del
      ``ComboBox`` directamente cuando trabajamos en formato
      ``GtkBuilder``, por lo que tendrás que llenarlo desde el
      código. Dale un nombre significativo al objeto para obtenerlo
      del documento. Puedes inspirarte para ver como llenar el objeto
      con el código que maneja el otro ``ComboBox`` del menú.

   .. hint:: Te puede ser muy útil hacer que las opciones del
      ``ComboBox`` coincidan con los nombres de los mapas de color,
      así basta con que utilices la función ``get_active_text`` para
      obtener la opción seleccionada y obtener el mapa de color
      finalmente con ``matplotlib.cm.get_cmap``.

   .. hint:: Conecta un manejador a la señal ``changed`` del
      ``ComboBox``. Ahí puedes comprobar que opción ha sido
      seleccionara y repintar la interfaz.
