<h4>Para qué sirve.</h4>
<p><span><span><span>Scrapy es una librería Open Source que nos permite extraer información importante que se encuentra en internet. Es posible leer el contenido de una web y movernos en su estructura HTML para analizar sus datos y explotarlos a diferentes formatos ya sea excel, xml, json, o a una base de datos.</span></span></span></p>
<h5><span><span><span>Ejemplos de uso.</span></span></span></h5>
<ul>
<li>Para marketing de contenidos: Generar nuestro propio contenido a partir de otra página web.</li>
<li>Para ganar visibilidad en redes sociales: Interactuar a traves de un robot con usuarios en redes sociales</li>
<li>Para controlar la imagen y la visibilidad de nuestra marca en internet: Podríamos rastrear la posición en Google de todas las entradas de nuestro blog.<em><br /></em></li>
</ul>
<h4><span><span>Primeros pasos.</span></span></h4>
<h5><span><span>Instalación.</span></span></h5>
<p><span><span>Scrapy se puede instalar con PyPi (Python Package Index) desde el siguiente comando:</span></span></p>
<pre><span><span>pip install Scrapy<br /></span></span></pre>
<p><span><span>Es altamente recomendable instalar Scrapy dentro de un entorno virtual, para no tener problemas con otros proyectos. Para empezar a usar los entornos virtuales antes hay que instalarlo con el siguiente comando:</span></span></p>
<pre><span><span>[sudo] pip install virtualenv</span></span></pre>
<p><span><span>Una vez instalado creamos un entorno virtual:</span></span></p>
<pre><span><span>virtualenv -p /rutaDelInterprete /rutaDondeCrearlo</span></span></pre>
<p><span><span>Para iniciar un entorno virtual nos vamos a la carpeta scripts dentro del entorno y ejecutamos el comando:</span></span></p>
<pre><span><span>activate.bat</span></span></pre>
<p> </p>
<p><span><span>Una vez echo esto ya podemos instalar scrapy dentro del entorno virtual.</span></span></p>
<p> </p>
<h5><span><span>Crear proyecto.</span></span></h5>
<p> Para crear un proyecto con scrapy ponemos el siguiente comando desde la consola:</p>
<pre>scrapy startproject nombreProyecto</pre>
<p> Al acabar te creará una carpeta con el nombre de tu proyecto y dentro de ella todo lo necesario para empezar a trabajar con Scrapy.</p>
<p> </p>
<h4><span><span><span><span>Principales funciones.</span></span></span></span></h4>
<h5> Spiders</h5>
<p>Dentro del proyecto de Scrapy podemos encontrar una carpeta llamada spiders, dentro de esta incluimos clases que definen a que url o grupos de urls se realizara el web scraping, que información será extraída de esta y algunas funciones adicionales como formas de continuar en otros enlaces (ej: enlaces de paginación). Dentro de esta carpeta podemos crear tantas clases "spider" como queramos, cada una de estas debe tener un nombre único dentro del proyecto. A continuación se puede ver un trozo de código comentado de una clase spider con sus elementos mínimos para funcionar y el seguimiento de paginación.</p>
<p>Código del ejemplo:<a class="text-info" title="Codigo Ejemplo" href="https://pastebin.com/s6nnMCj5" rel="noreferrer" target="_blank"> https://pastebin.com/s6nnMCj5</a></p>
<p>Pagina a la que se realiza la prueba: <a title="pagina scraping" href="http://quotes.toscrape.com/">http://quotes.toscrape.com/</a></p>
<p> </p>
<p>Para poder ejecutar la aplicación debemos escribir el siguiente comando en la consola.</p>
<pre>scrapy crawl nombreDelSpider</pre>
<p>Para este ejemplo seria:</p>
<pre><span class="n">scrapy</span> <span class="n">crawl</span> follow</pre>
<p>y si queremos guardar los resultados en algun archivo por ejemplo en formato json podemos hacer lo siguiente:</p>
<pre><span class="n">scrapy</span> <span class="n">crawl</span> <span>follow</span><span class="n"> -o <span>follow.json</span></span></pre>
<p> </p>
<h4><span><span><span><span><span><span><span><span>Proyecto de ejemplo.</span></span></span></span></span></span></span></span></h4>
<p><span><span><span><span><span><span><span><span>Repositorio git: <a title="Repositorio git" href="https://github.com/Davd96/ScrapyExamples.git">https://github.com/Davd96/ScrapyExamples.git</a></span></span></span></span></span></span></span></span></p>
