const page = document.querySelector("body");
const accountLink = document.querySelector('#account-link');
const accountContent = document.querySelector('#account-content');
const starOne = document.querySelector('#star-one');
const starTwo = document.querySelector('#star-two');
const starThree = document.querySelector('#star-three')
const starFour = document.querySelector('#star-four')
const starFive = document.querySelector('#star-five')
const starsSelected = document.querySelector('#stars-selected');
const emptyStarOne = document.querySelector('#empty-star-one');
const emptyStarTwo = document.querySelector('#empty-star-two');
const emptyStarThree = document.querySelector('#empty-star-three');
const emptyStarFour = document.querySelector('#empty-star-four');
const emptyStarFive = document.querySelector('#empty-star-five');
const filledStarOne = document.querySelector('#filled-star-one');
const filledStarTwo = document.querySelector('#filled-star-two');
const filledStarThree = document.querySelector('#filled-star-three');
const filledStarFour = document.querySelector('#filled-star-four');
const filledStarFive = document.querySelector('#filled-star-five');

// toggle account dropdown
// accountLink.addEventListener('click', () => {
//     accountContent.classList.toggle('account');
//     accountContent.classList.toggle('account-content');
// });

// show one star
starOne.addEventListener('click', () => {
    starsSelected.setAttribute('value', '1');
    emptyStarOne.classList.add('stars-emptied');
    filledStarOne.classList.remove('stars-emptied');
    emptyStarTwo.classList.remove('stars-emptied');
    filledStarTwo.classList.add('stars-emptied');
    emptyStarThree.classList.remove('stars-emptied');
    filledStarThree.classList.add('stars-emptied');
    emptyStarFour.classList.remove('stars-emptied');
    filledStarFour.classList.add('stars-emptied');
    emptyStarFive.classList.remove('stars-emptied');
    filledStarFive.classList.add('stars-emptied');
    console.log("one");
});

// show two stars
starTwo.addEventListener('click', () => {
    starsSelected.setAttribute('value', '2');
    emptyStarOne.classList.add('stars-emptied');
    filledStarOne.classList.remove('stars-emptied');
    emptyStarTwo.classList.add('stars-emptied');
    filledStarTwo.classList.remove('stars-emptied');
    emptyStarThree.classList.remove('stars-emptied');
    filledStarThree.classList.add('stars-emptied');
    emptyStarFour.classList.remove('stars-emptied');
    filledStarFour.classList.add('stars-emptied');
    emptyStarFive.classList.remove('stars-emptied');
    filledStarFive.classList.add('stars-emptied');
    console.log("two");
});

// show three stars
starThree.addEventListener('click', () => {
    starsSelected.setAttribute('value', '3');
    emptyStarOne.classList.add('stars-emptied');
    filledStarOne.classList.remove('stars-emptied');
    emptyStarTwo.classList.add('stars-emptied');
    filledStarTwo.classList.remove('stars-emptied');
    emptyStarThree.classList.add('stars-emptied');
    filledStarThree.classList.remove('stars-emptied');
    emptyStarFour.classList.remove('stars-emptied');
    filledStarFour.classList.add('stars-emptied');
    emptyStarFive.classList.remove('stars-emptied');
    filledStarFive.classList.add('stars-emptied');
    console.log("three");
});

// show four stars
starFour.addEventListener('click', () => {
    starsSelected.setAttribute('value', '4');
    emptyStarOne.classList.add('stars-emptied');
    filledStarOne.classList.remove('stars-emptied');
    emptyStarTwo.classList.add('stars-emptied');
    filledStarTwo.classList.remove('stars-emptied');
    emptyStarThree.classList.add('stars-emptied');
    filledStarThree.classList.remove('stars-emptied');
    emptyStarFour.classList.add('stars-emptied');
    filledStarFour.classList.remove('stars-emptied');
    emptyStarFive.classList.remove('stars-emptied');
    filledStarFive.classList.add('stars-emptied');
});

// show five stars
starFive.addEventListener('click', () => {
    starsSelected.setAttribute('value', '5');
    emptyStarOne.classList.add('stars-emptied');
    filledStarOne.classList.remove('stars-emptied');
    emptyStarTwo.classList.add('stars-emptied');
    filledStarTwo.classList.remove('stars-emptied');
    emptyStarThree.classList.add('stars-emptied');
    filledStarThree.classList.remove('stars-emptied');
    emptyStarFour.classList.add('stars-emptied');
    filledStarFour.classList.remove('stars-emptied');
    emptyStarFive.classList.add('stars-emptied');
    filledStarFive.classList.remove('stars-emptied');
});