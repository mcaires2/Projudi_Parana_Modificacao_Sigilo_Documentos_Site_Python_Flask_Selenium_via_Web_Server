function ProsseguirAutomacao(){

          
       
    feedback_time_stamp=myJobTimeStamp();
    $("#mensagem1").html('Job ' + feedback_time_stamp + ' iniciado...');
    $("#uploadarquivo2").css("display", "block");
    $("#containerGeral").css("opacity",0.5);

    ajaxAutomacaoSeleniumFormSubmit();


}

function VoltarHome(){

    window.location.href = "/";
}



function RetomarEstadoOriginal(){

    $("#uploadarquivo2").css("display", "none"); // mudar após teste
    $("#containerGeral").css("opacity",1);      
    
   
}


$(document).ready(function () {
          
     RetomarEstadoOriginal();
       
});

function myJobTimeStamp() {
    
    var d = new Date();
    var meu_timeStamp = d.getTime();

    return meu_timeStamp
    
  }

