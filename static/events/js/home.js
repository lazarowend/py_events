const nameSearchInput = document.getElementById("name-search");
const btnSearch = document.getElementById("btn-search");
const divGrid = document.getElementById("grid");
const divSearchOptions = document.getElementById("search-options");


nameSearchInput.addEventListener('input', () => {
    nameSearch = nameSearchInput.value
    if (nameSearch != '') {
        SearchEvents(nameSearch)
            .then(function(events) {
                console.log(events);
                renderSearchOptions(events);
            });
    } else {
        divSearchOptions.innerHTML = '';
    }
});


btnSearch.addEventListener('click', () => {
    divSearchOptions.innerHTML = '';
    nameSearch = nameSearchInput.value
    SearchEvents(nameSearch)
        .then(function(events) {
            renderEventsSearch(events);
        });
});


function SearchEvents(nameSearch) {
    if (nameSearch == '') {
        nameSearch = 'all'
    }
    var url = 'http://127.0.0.1:8000/events/search_events/' + encodeURIComponent(nameSearch);
    return fetch(url)
        .then(function(response) {
            if (!response.ok) {
                console.log('Erro na solicitação');
            }
            console.log(response)
            return response.json();
        })
        .then(function(data) {
            return data;
        })
        .catch(function(error) {
            console.error('Erro:', error);
        });
}


function renderEventsSearch(events) {
    divGrid.innerHTML = "";
    if (events.length == 0) {
        divGrid.innerHTML = "Sem resultados";
        return;
    }
    events.forEach(e => {
                divGrid.innerHTML += `
            <div class="cell">
                <div class="card disabled">
                    <div class="card-image">
                        <figure class="image is-4by3">
                            <img src="${e.image}" alt="${e.name}" />
                        </figure>
                    </div>
                    <div class="card-content">
                        <div class="media">
                            <div class="media-content">
                                <p class="title is-4">${e.name}</p>
                                <p class="subtitle is-6">Organizado por: ${e.user}</p>
                            </div>
                        </div>
                        <div class="content">
                            <p>Data Prevista: <time datetime="${e.date_event}">${e.date_event}</time></p>
                        </div>
                        ${e.status ? `
                            <a href="{% url 'detail_event_view' slug=${e.status} %}" class="button is-warning">Ver mais</a>
                            <a href="{% url 'detail_event_view' slug=${e.status} %}" class="button is-primary">Comprar Ingresso</a>
                        ` : `
                            <a href="{% url 'detail_event_view' slug=${e.status} %}" class="button is-warning">Ver mais</a>
                            <a class="button is-primary" disabled>Evento Esgotado</a>
                        `}
                    </div>
                </div>
            </div>`;
    });
}


function renderSearchOptions(options) {
    divSearchOptions.innerHTML = '';
    options.forEach(option => {
        optionElement = document.createElement("a");
        optionElement.className = "panel-block is-active";
        optionElement.textContent = `${ option.name }`;
        optionElement.href = 'http://127.0.0.1:8000/events/detail/' + encodeURIComponent(option.slug);

        divSearchOptions.appendChild(optionElement)
    })
}