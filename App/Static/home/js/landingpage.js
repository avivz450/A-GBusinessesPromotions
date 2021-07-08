let choose_website_button = document.getElementById("choose_website_button");
let register_website_button = document.getElementById("register_website_button");
let choose_website_div = document.getElementById("choose_website_div");
let register_website_div = document.getElementById("register_website_div");

choose_website_div.style.display = "none";
register_website_div.style.display = "none";

choose_website_button.onclick = function () {
    register_website_div.style.display = "none";
    choose_website_div.style.display = "block";
}

register_website_button.onclick = function () {
    choose_website_div.style.display = "none";
    register_website_div.style.display = "block";
}
