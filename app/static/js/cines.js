const getCines = async() => {
    const data = await fetch(`https://oaemdl.es/cinestar_sweb_php/cines`)
    if ( data.status == 200 ) {
        const cines = await data.json()
        let html = `
            {% extends ('index.html')%}
            {% block contenido_interno %}
            <br/><h1>Nuestros Cines</h1><br/>
            `
        cines.forEach(cine => {
            html += ` 
            <br/><h1>Nuestros Cines</h1><br/>
            <div class="contenido-cine">
                <img src="{{url_for('static',filename='img/cine/1.1.jpg')}}" width="227" height="170"/>
                   <div class="datos-cine">
                       <h4>Excelsior</h4><br/>
                    <span>Jirón de la Unión 780 - Lima<br/><br/>Teléfono: 714-1865 anexo 865</span>
                </div>
                <br/>
                <a href="http://www.cinestar.com.pe/multicines/cine/Cinestar-Excelsior">
                    <img src="{{url_for('static',filename='img/varios/ico-info2.png')}}" width="150" height="40"/>
                </a>
            </div>
            `
        });
        html += 
        '{% endblock %}'
        
        document.getElementById('contenido-interno').innerHTML = html
    }
}

getCines()