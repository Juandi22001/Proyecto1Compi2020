

//  PATHW:/home/juan/Documentos/ll

/* efeeeeeeeee*/



        


function session(){

    var success = sessionStorage.getItem("session-user");

    if(success == null){
        window.location.href = "login.html";
    }
    
}

