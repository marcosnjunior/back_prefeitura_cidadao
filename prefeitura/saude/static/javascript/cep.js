const cep = document.querySelector('input[name="cep"]');

cep.addEventListener('input', (e) => {
    e.target.value = formatacaoCep(e.target.value);
})

const formatacaoCep = (cep) => {
    const cleanedCep = cep.replace(/\D/g, '');
    const match = cleanedCep.match(/^(\d{5})(\d{3})$/);
    
    if (match) {
        return `${match[1]}-${match[2]}`;
    }
    
    return cleanedCep;
}