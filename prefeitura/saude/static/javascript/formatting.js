const tel = document.querySelector('input[name="telefone"]');
tel.addEventListener('keypress', (e) => mascaraTelefone(e.target.value))
tel.addEventListener('change', (e) => mascaraTelefone(e.target.value))
const mascaraTelefone = (value) => {
    let newValue = value.replace(/\D/g, '');
    newValue = newValue.replace(/^(\d{2})(\d)/g, '($1) $2');
    newValue = newValue.replace(/(\d)(\d{4})$/, '$1-$2');
    tel.value = newValue;
}