// client-side js
// run by the browser each time your view template is loaded

$(function () {
  $('form').submit(function (event) {
    event.preventDefault();
    
    $('#new-releases').empty();
    let country = $('select').val();

    // Send a request to our backend (server.py) to get new releases for the currently selected country
    $.get('/new_releases?' + $.param({ country: country }), function (new_releases) {
      // Loop through each album in the list
      new_releases.albums.items.forEach(function (release) {
        let div = $('<div class="sp-entity-container"><a href="' + release.external_urls.spotify + 
                    '" target="_blank"><div style="background:url(\'' + release.images[0].url + 
                    '\')" class="sp-cover" alt="Album cover"></div></a><h3 class="sp-title">' + release.name + 
                    '</h3><p class="sp-by">By ' + release.artists[0].name + '</p></div>');

        div.appendTo('#new-releases');
      });
    });
  });
});

// Create a random starry background effect
function generateStars(numStars) {
  const starContainer = document.querySelector('.stars');
  for (let i = 0; i < numStars; i++) {
    const star = document.createElement('div');
    star.classList.add('star');
    const size = Math.random() * 2 + 1; // Random size between 1px and 3px
    const posX = Math.random() * 100; // Random X position in %
    const posY = Math.random() * 100; // Random Y position in %
    
    // Set the size and position for each star
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;
    star.style.left = `${posX}%`;
    star.style.top = `${posY}%`;
    
    // Add star to container
    starContainer.appendChild(star);
  }
}

// Call the function to generate 1000 stars
generateStars(1000);

