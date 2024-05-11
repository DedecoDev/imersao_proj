$(document).ready(function() {
    $("#perguntar").click(function() {
      var pergunta = $("#pergunta").val();
  
      // Mostrar título e loading
      $("#TituloChatBot").removeClass("dnone").addClass("dblock");
      $("#loading").removeClass("dnone").addClass("dblock");
  
      // Previne o comportamento padrão do botão de enviar o formulário
      event.preventDefault();
  
      $.post("/perguntar", { pergunta: pergunta }, function(resposta) {
        // Esconder loading
        $("#loading").addClass("dnone");
  
        // Exibir resposta
        $("#BoxRespostaGemini").text(resposta);
      });
    });
  
    // Limpar busca (também oculta o título e o loading)
    $("#limpaGe").click(function() {
      $("#pergunta").val("");
      $("#BoxRespostaGemini").html("");
      $("#TituloChatBot").addClass("dnone");
      $("#loading").addClass("dnone");
    });
  
    // Acionar busca ao pressionar Enter no campo de busca
    $("#pergunta").keypress(function(event) {
      if (event.which == 13) {
        $("#perguntar").click();
        $("#TituloChatBot").removeClass("dnone").addClass("dblock");
        $("#loading").removeClass("dnone").addClass("dblock");
      }
    });
  });