

//  PATHW:/home/juan/Documentos/ggP

/******************************************************************
 * ============================================================== *
 * ============================================================== *
 * ============================================================== *
 * ===================ARCHIVO DE PRUEBA DE JS==================== *
 * ============================================================== *
 * ================PATHL -> /home/user/output/js/================ *
 * =================PATHW -> c:\user\output\js\================== *
 * ============================================================== *
 * ============================================================== *
 * ============================================================== *
 ******************************************************************/



        


function session(){

    var success = sessionStorage.getItem("session-user");

    if(success == null){
        window.location.href = "login.html";
    }
    
}


function obtener(){
    session();^

    var f = new Date();

    var date = f.getFullYear() + "" + ( f.getMonth() + 1 ) + "" + f.getDate(); // YYYYMMDD

    var nit = document.getElementById("nit").value;

    var datos = {
        fecha: parseInt(date,"10"), // fecha de pedido
        nit: nit,                   // nit del cliente
    };

    var url = 'http://ejemplo_sitio_web/endpoint1/';

    ajax({url,
        type: 'POST',
        dataType: 'json',
        data: datos,
        async: true,
        success: function(response){
            addProducts(response);
        }
    });

}



function addProducts(data){

    ^var toJSON = JSON.parse(JSON.stringify(data));

    var tbody = document.getElementById('body');

    var inputTotal = document.getElementById("total");

    var total = 0.0;

    toJSON.forEach(function(element) {
        total = total + parseFloat(element.precio);
    });

    inputTotal.value = total;

    return '200';
}



function facturar(){

    var doc = new jsPDF();``

    var nit = document.getElementById("nit").value;

    var total = document.getElementById("total").value;
    

    var specialElementHandlers = {
        '#elementH': function (element, renderer) {
            return true;
        }
    };


    doc.fromHTML(elementHTML, 15, 15, {
        'width': 170,
        'elementHandlers': specialElementHandlers
    });



