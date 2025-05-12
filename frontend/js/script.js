 document.getElementById('form-previsao').addEventListener('submit', function(event) {
      event.preventDefault();

      const dados = {
        Causa_Direta: document.getElementById('causa').value,
        Natureza: document.getElementById('natureza').value,
        Hora: parseInt(document.getElementById('hora').value)
      };

      fetch('http://127.0.0.1:5000/prever', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dados)
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('resultado').innerText = 
          `Interrupção prevista: ${data.interrupcao_prevista_h} h`;
      })
      .catch(error => {
        document.getElementById('resultado').innerText = 'Erro na previsão.';
        console.error(error);
      });
    });