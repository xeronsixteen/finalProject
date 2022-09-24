async function sendFav(event) {
    event.preventDefault();
    let target = event.target;
    let url = target.href;
    let response = await fetch(url);
    let response_json = await response.json();
    let count = response_json.count;
    console.log(count);
    let photoId = target.dataset.photoId;
    let span = document.getElementById(photoId);
    span.innerText = `Положили в избранное: ${count}`;
    if (target.innerText === "В избранное") {
        K
        target.innerText = "В избранное";
    } else {
        target.innerText = "Удалить";
    }
}


function onloadFunc() {

    let favs = document.getElementsByClassName("favs");
    for (let i = 0; i < favs.length; i++) {
        favs[i].addEventListener("click", sendFav)
    }
}

window.addEventListener("load", onloadFunc)

