const tel = document.querySelector('input[name="telefone"]');


tel.addEventListener('input', (e) => {
    e.target.value = formatacaoCelular(e.target.value);
});

const formatacaoCelular = (phoneNumber) => {
    const cleanedPhoneNumber = phoneNumber.replace(/\D/g, '');
    const match = cleanedPhoneNumber.match(/^(\d{2})(\d{4})(\d{4})$/);
    
    if (match) {
        return `(${match[1]}) ${match[2]}-${match[3]}`;
    }
    
    return cleanedPhoneNumber;
};