

//  PATHW:/home/juan/Documentos/kio

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
