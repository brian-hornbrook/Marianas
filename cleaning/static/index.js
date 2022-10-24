const accountLink = document.querySelector('#account-link');
const accountContent = document.querySelector('#account-content');

    accountLink.addEventListener('click', () => {
        accountContent.classList.toggle('account');
        accountContent.classList.toggle('account-content');
    })