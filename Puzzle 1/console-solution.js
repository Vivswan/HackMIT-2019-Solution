for (let i=0; i <= 10; i++) document.querySelector("body > center > div.full.flex > footer > button.btn.isButton.green").click()
for (let i=0; i <= 50; i++) document.querySelector("#spoiler1 > button").click()
for (let i=0; i <= 1000; i++) document.querySelector("#spoiler2 > button").click()

sendRequest = function (x,y) {
    x = parseInt(x);
    y = parseInt(y);
    if (window.myHomeAustinTexas == null) {
      // Check if cached
      var cachedHex = getCacheStore(x, y, false);
      if (cachedHex != null) {
        fillPosition(x, y, cachedHex);
        $("#revealed-pixels").text(revealedPixels);
        $("#smash-div").removeClass("hidden");
        setTimeout(function() {
          $("#smash-div").addClass("hidden");
        }, 200);
        return;
      }
    }
    
    // If already shown
    if (getCacheStore(x, y, true)) {
      return;
    }
    
    $("#revealed-pixels").text(revealedPixels);
    var pathname = window.location.pathname + "/" + x + "/" + y;
    console.log("QUERY " + pathname);
    fetch(pathname)
      .then(function(response) {
        if (response.status === 429) {
          return null;
        }
        if (response.status !== 200) {
          return null;
        }
        return response.text();
      }).then(function(text) {
        if (text == null) {
          return;
        }
        var lines = text.split("\n");
        for (var ind = 0; ind < lines.length; ind += 1) {
          var line = lines[ind].split(",");
          var locSpl = line[0].split("_");
          var hex = line[1];
          if (hex.length !== 7) {
            continue;
          }
  
            fillPosition(parseInt(locSpl[0]), parseInt(locSpl[1]), hex);
            didAction = true;
        }
      });
  
}
sendRequest = newRequest2
