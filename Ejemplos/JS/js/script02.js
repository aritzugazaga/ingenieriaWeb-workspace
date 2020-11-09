$(document).ready( function () {
    //-Selector de todos los elementos de clase "rojo" 
    //$(".rojo").css("border","3px solid red");
    //-Selector del elemento de id "segundo" 
    //$("#segundo").css("border","3px solid green");
    //-Selector de la etiqueta p 
    //$("p").css("color","blue");
    //-Selector de todos los elementos de clase "rojo" 
    //$(".rojo, h2").css("border","3px solid red");
    //-Selector del elemento de id "segundo" 
    //$("p.rojo .negrita").css("color","blue");
    //-Selector de la etiqueta p 
    //$("p:not(.rojo)").css("background-color","silver");
    //Selector de todos los elementos ul descendientes (hijos, //nietos, bisnietos) de un ol de clase "ordenada" 
    $("ol.ordenada ul").css("background-color","silver"); 
    //Selector de todos los elementos li hijos (solamente 
    //hijos) de ul de clase "desordenada"
    $("ul.desordenada > li").css("color","gray");
    //Selector del siguiente elemento li después de otro con 
    //id "primero"
    $("#primero + li").css("color","yellow");
    //Selector de todos los elementos li hermanos después de 
    // otro con id "primero"
    $("#primero ~ li").css("background-color", "green");
});