//obtener el elemento lista

const lista= document.getElementById("lista");

// funcion para agregar

function agregar(){

    // guardar el texto en una variable
    let texto = document.getElementById("texto_entrada").value;
    //poner en la lista el elemento
    var nuevo_elemento = document.createElement("li");
    nuevo_elemento.appendChild(document.createTextNode(texto));
    lista.appendChild(nuevo_elemento)

    //borrar lo que está en el input
    document.getElementById("texto_entrada").value = '';


};


//funcion para borrar el ultimo elemento en la lista.

function borrar(){
    //si la lista tiene algun elemento borra el ultimo hijo de la lista.
    if(lista.children.length  >0){
    lista.removeChild(lista.lastChild);
    }

};