$(document).ready(function(){
    $("#Pesquisar").click(function(){
        // Obter termo de busca
        var termoBusca = $("#campoBusca").val().toLowerCase();
      
        // Mostrar o título
        $("#TituloBusca").removeClass("d-none").addClass("d-block"); 
      
        // Limpar resultados anteriores
        $("#ResultadoBuscaGemini").empty();
      
        // Loop por cada BlocoLinhaDaNoticia
        $(".LinhaDaNoticia").each(function(){
          var bloco = $(this);
          var nomeJornal = bloco.find("span").text(); 
          var descricao = bloco.find("h3").text().toLowerCase(); 
          var link = bloco.find("LinkLerMateria a").attr("href");
      
          // Verificar se o termo de busca existe no título E na descrição
          if (descricao.includes(termoBusca)) { 
            // Criar estrutura HTML para o resultado
            var resultadoHTML = '<div class="LinhaResultado">';
            resultadoHTML += '<h3>' + descricao + '</h3>';
            resultadoHTML += '<p><strong>' + nomeJornal + '</strong></p>';
            resultadoHTML += '<a href="' + link + '" target="_blank">Leia Mais</a>';
            resultadoHTML += '</div>';
      
            // Adicionar resultado ao ResultadoBuscaGemini
            $("#ResultadoBuscaGemini").append(resultadoHTML); 
          }
        });
      
        // Mostrar mensagem se não houver resultados
        if ($("#ResultadoBuscaGemini").is(':empty')) {
          $("#ResultadoBuscaGemini").append("<p>Desculpe, mas não foram encontrados resultados para essa busca.</p>");
        }
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