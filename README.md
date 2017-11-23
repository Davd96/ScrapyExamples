Para qué sirve.

Scrapy es una librería Open Source que nos permite extraer información importante que se encuentra en internet. Es posible leer el contenido de una web y movernos en su estructura HTML para analizar sus datos y explotarlos a diferentes formatos ya sea excel, xml, json, o a una base de datos.

Ejemplos de uso.

Para marketing de contenidos: Generar nuestro propio contenido a partir de otra página web.
Para ganar visibilidad en redes sociales: Interactuar a traves de un robot con usuarios en redes sociales
Para controlar la imagen y la visibilidad de nuestra marca en internet: Podríamos rastrear la posición en Google de todas las entradas de nuestro blog.
Primeros pasos.

Instalación.

Scrapy se puede instalar con PyPi (Python Package Index) desde el siguiente comando:

pip install Scrapy
Es altamente recomendable instalar Scrapy dentro de un entorno virtual, para no tener problemas con otros proyectos. Para empezar a usar los entornos virtuales antes hay que instalarlo con el siguiente comando:

[sudo] pip install virtualenv
Una vez instalado creamos un entorno virtual:

virtualenv -p /rutaDelInterprete /rutaDondeCrearlo
Para iniciar un entorno virtual nos vamos a la carpeta scripts dentro del entorno y ejecutamos el comando:

activate.bat
 

Una vez echo esto ya podemos instalar scrapy dentro del entorno virtual.

 

Crear proyecto.

 Para crear un proyecto con scrapy ponemos el siguiente comando desde la consola:

scrapy startproject nombreProyecto
 Al acabar te creará una carpeta con el nombre de tu proyecto y dentro de ella todo lo necesario para empezar a trabajar con Scrapy.

 

Principales funciones.

 Spiders

Dentro del proyecto de Scrapy podemos encontrar una carpeta llamada spiders, dentro de esta incluimos las clases que definen que sitio o grupos de sitio serán "scraped", que información será extraída de esta y algunas funciones adicionales como formas de continuar en otros enlaces (ej: enlaces de paginación). Dentro de esta carpeta podemos crear tantas clases "spider" como queramos, cada una de estas debe tener un nombre único dentro del proyecto. A continuación se puede ver un trozo de código comentado de una clase spider con sus elementos mínimos para funcionar y el seguimiento de paginación.

 https://pastebin.com/s6nnMCj5
