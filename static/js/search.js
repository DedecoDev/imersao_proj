$(document).ready(function(){
    $("#Pesquisar").click(function(){
        // Obter termo de busca
        var termoBusca = $("#campoBusca").val().toLowerCase();
        $("#TituloBusca").removeClass("d-none").addClass("d-block"); // Mostrar o título

        // Limpar resultados anteriores
        $("#ResultadoBuscaGemini").html("");

        // Loop por cada BlocoLinhaDaNoticia
        $(".LinhaDaNoticia").each(function(){
            var bloco = $(this);
            var nomeJornal = bloco.find("span").text(); // Obter o nome do jornal
            var descricao = bloco.find("h3").text().toLowerCase(); // Assuming description is in this class
            var link = bloco.find("LinkLerMateria a").attr("href");

            // Verificar se o termo de busca existe no título E na descrição
            if (descricao.includes(termoBusca)) {
                // Criar estrutura HTML para o resultado
                var resultadoHTML = '<div class="LinhaResultado">';
                resultadoHTML += '<h3>' + descricao + '</h3>';
                resultadoHTML += '<p><strong>' + nomeJornal + '</strong></p>'; // Exibir o nome do jornal
                resultadoHTML += '<a href="' + link + '" target="_blank">Leia Mais</a>';
                resultadoHTML += '</div>';

                // Adicionar resultado ao ResultadoBuscaGemini
                $("#ResultadoBuscaGemini").append(resultadoHTML);
            }
        });
    });

    // Limpar busca (também oculta o título)
    $("#Limpar").click(function(){
        $("#campoBusca").val("");
        $("#ResultadoBuscaGemini").html("");
        $("#TituloBusca").addClass("d-none");
    });

    // Acionar busca ao pressionar Enter no campo de busca
    $("#campoBusca").keypress(function(event) {
        if (event.which == 13) {
            $("#Pesquisar").click();
            $("#TituloBusca").removeClass("d-none").addClass("d-block"); // Mostrar o título
        }
    });
});