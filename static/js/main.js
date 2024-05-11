
/*refresh*/
document.getElementById('AtualizaF5').addEventListener('click', function() {
    location.reload(true);
});



        // Função para obter a data e hora atual formatada
        function obterDataHoraAtual() {
            var dataAtual = new Date();
            var dia = String(dataAtual.getDate()).padStart(2, '0');
            var mes = String(dataAtual.getMonth() + 1).padStart(2, '0');
            var ano = dataAtual.getFullYear();
            var hora = String(dataAtual.getHours()).padStart(2, '0');
            var minuto = String(dataAtual.getMinutes()).padStart(2, '0');
            var segundo = String(dataAtual.getSeconds()).padStart(2, '0');

            return `${dia}/${mes}/${ano} - ${hora}:${minuto}:${segundo}`;
        }

        // Atualiza o conteúdo do elemento com a data e hora atual
        function atualizarDataHoraAtual() {
            var elementoDadoAtualizado = document.getElementById('DadoAtualizado');
            if (elementoDadoAtualizado) {
                elementoDadoAtualizado.textContent = `Hoje é dia ${obterDataHoraAtual()}`;
            }
        }

        // Atualiza a cada segundo (1000 milissegundos)
        setInterval(atualizarDataHoraAtual, 1000);



        


/*voltar ao topo*/
$(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('a[href="#top"]').fadeIn();
        } else {
            $('a[href="#top"]').fadeOut();
        }
    });

    $('a[href="#top"]').click(function(){
        $('html, body').animate({scrollTop : 0},800);
        return false;
    });
});

/*Dia*/
        // Função para obter a data atual
        function obterDataAtual() {
            var dataAtual = new Date();
            var dia = String(dataAtual.getDate()).padStart(2, '0');
            var mes = String(dataAtual.getMonth() + 1).padStart(2, '0');
            var ano = dataAtual.getFullYear();

            return dia + '/' + mes + '/' + ano;
        }

        // Função para aplicar a data atual em um elemento com o ID especificado
        function aplicarDataAtual(id) {
            var elemento = document.getElementById(id);
            if (elemento) {
                elemento.innerText = obterDataAtual();
            } else {
                console.error('Elemento não encontrado com o ID:', id);
            }
        }

        // Aplicar a data atual em elementos com diferentes IDs
        aplicarDataAtual('dataAtual1');
        aplicarDataAtual('dataAtual2');
        aplicarDataAtual('dataAtual3');
