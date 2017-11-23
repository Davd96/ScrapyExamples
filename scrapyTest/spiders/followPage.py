import scrapy #Importamos scrapy


class QuotesSpider(scrapy.Spider):
    name = "follow"     #Aqui indicamos el nombre unico para la clase spider, este nombre será
                        #Utilizado para ejecutar la aplicacion desde la linea de comandos.
    start_urls = [      #Aqui indicamos las urls de las que queremos extraer la informacion
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):  #Este metodo se encarga de extraer la información que queramos
        for quote in response.css('div.quote'):     # Creamos un bucle que recorra cada elemento selecionado
                                                    # mediante un selector css en este caso cada quote sera un div
                                                    # de una web el cual tiene otras equitas dentro

            yield {
                'text': quote.css('span.text::text').extract_first(),           # Selecionamos dentro del div mencionado anteriormente los elementos
                'author': quote.css('span small::text').extract_first(),        #  que nos interesen.
                'tags': quote.css('div.tags a.tag::text').extract(),            # Siempre seleccionado mediante selectores css y el metodo extract() o
            }                                                                   # extract_first() nos devolveria el valor.

        next_page = response.css('li.next a::attr(href)').extract_first()       # Esta linea se encarga de extraer la url de la siguiente pagina
        if next_page is not None:                                               # Comprueba si existe un siguiente enlace
            yield response.follow(next_page, callback=self.parse)               # Aqui con la funcion follow vuelve a llamar a la funcion parse
                                                                                # Pasandole la url de la siguiente pagina.