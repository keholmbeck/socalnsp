function getRSS()
{

    var x = new XMLHttpRequest();
    x.open("GET", "http://www.socalnsp.blogspot.com/feeds/posts/default?alt=rss", true);
    x.onreadystatechange = function () {
      if (x.readyState == 4 && x.status == 200)
      {
        var doc = x.responseXML;
        // ?
      }
    };
    x.send(null);
    
}