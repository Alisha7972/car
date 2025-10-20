console.log("Ajax tutorial in one video.");

let fetchBtn = document.getElementById("fetchBtn");
fetchBtn.addEventListener('click', buttonClickHandler);

function buttonClickHandler() {
    console.log('You have clicked the fetchBtn');

    // Create an XMLHttpRequest object
    const xhr = new XMLHttpRequest();

    // Open the request
    xhr.open('GET', 'harry.txt', true);

    xhr.onprogress = function () {

    }


}
