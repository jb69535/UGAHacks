'use strict';

// Make navbar trasparent when it is on the top.
const navbar = document.querySelector('#Navbar');
const navbarHeight = navbar.getBoundingClientRect().height;
document.addEventListener(
    'scroll', () => {
        console.log(window.scrollY)
        console.log('navbarHeight: ${navbarHeight}');
        if (window.scrollY > navbarHeight) {
            navbar.classList.add('navbar--dark');
        } else {
            navbar.classList.remove('navbar--dark');
        }
    });

//Get location when Onclick button

const x = document.getElementById("current__Location");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, showError);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}

function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Location information is unavailable."
      break;
    case error.TIMEOUT:
      x.innerHTML = "The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "An unknown error occurred."
      break;
  }
}
