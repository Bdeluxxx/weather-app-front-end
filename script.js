// O Front End "chama" o Back End para obter os dados
fetch('fetch('https://bdeluxxx.pythonanywhere.com/clima')')
    .then(response => response.json())
    .then(data => {
        // Pega os elementos do HTML
        const tempElement = document.getElementById('temp');
        const descricaoElement = document.getElementById('descricao');

        // Atualiza o HTML com os dados da API
        if (data.temperatura) {
            tempElement.textContent = data.temperatura;
            descricaoElement.textContent = data.descricao;
        } else {
            tempElement.textContent = 'Erro';
            descricaoElement.textContent = 'Erro';
            console.error('Dados da API estão incompletos:', data);
        }
    })
    .catch(error => {
        console.error('Erro ao buscar dados:', error);
    });