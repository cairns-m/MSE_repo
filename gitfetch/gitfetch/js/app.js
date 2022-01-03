const inputValue = document.querySelector("#search");
const searchButton = document.querySelector(".searchButton");
const nameContainer = document.querySelector(".main__profile-name");
const unContainer = document.querySelector(".main__profile-username");
const reposContainer = document.querySelector(".main__profile-repos");
const urlContainer = document.querySelector(".main__profile-url");


const client_id = "Iv1.374df8c2ac317af4";
const client_secret = "2921ccf7ca2031f98fe9e555741b2d780b296304";

const fetchUsers = async (user) => {
    // const api_call = await fetch('https://api.github.com/users/${user}?client_id=${client_id}&client_secret=${client_secret}');
    const api_call = await fetch('https://api.github.com/users/${user}');

    const data = await api_call.json();
    return { data } 
}

const showData = () => {
    fetchUsers(inputValue.value).then((reponse) => {
        console.log(reponse);
    })
}



searchButton.addEventListener("click", () => {
    showData();

})