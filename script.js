const searchInput = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestions");

searchInput.addEventListener("keyup", function(){

let query = searchInput.value;

if(query.length === 0){
    suggestionsBox.innerHTML = "";
    return;
}

fetch("/suggest?q=" + query)
.then(response => response.json())
.then(data => {

    suggestionsBox.innerHTML = "";

    data.forEach(item => {

        let div = document.createElement("div");
        div.classList.add("suggest-item");
        div.innerText = item;

        div.onclick = function(){
            searchInput.value = item;
            suggestionsBox.innerHTML = "";
        };

        suggestionsBox.appendChild(div);

    });

});

});