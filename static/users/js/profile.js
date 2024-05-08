const yesRadio = document.getElementById('yes-radio');
const noRadio = document.getElementById('no-radio');
const divPassword = document.getElementById('div-password');
const userForm = document.getElementById('user-form');
const btnEdit = document.getElementById('btn-editar')
const divInfoPessoais = document.getElementById('info-pessoais')


yesRadio.addEventListener('click', () => {
    divPassword.classList.remove('is-hidden');
});

noRadio.addEventListener('click', () => {
    divPassword.classList.add('is-hidden');
});

btnEdit.addEventListener('click', () => {
    userForm.classList.remove('is-hidden');
    btnEdit.classList.add('is-hidden');
    divInfoPessoais.classList.add('is-hidden');
})


window.onload = () => {
    const amountTicketsPurshased = document.getElementById("amount-tickets-purshased");
    const amountTicketsSold = document.getElementById("amount-tickets-sold");
    const amountCreateEvents = document.getElementById("amount-create-events");
    const amountCreateAddress = document.getElementById("amount_user_address");

    const url = "http://127.0.0.1:8000/events/get_infos_events_tickets_address_user";
    fetch(url)
        .then(function(response) {
            if (!response.ok) {
                console.log('Erro na solicitação');
            }
            return response.json();
        })
        .then(function(data) {
            amountCreateEvents.innerHTML = data['amount_user_created_events'];
            amountTicketsPurshased.innerHTML = data['amount_user_tickets_purchased'];
            amountTicketsSold.innerHTML = data['amount_user_tickets_sold'];
            amountCreateAddress.innerHTML = data['amount_user_address'];
        });
};