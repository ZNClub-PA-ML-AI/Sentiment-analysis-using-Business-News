//https://cdn.rawgit.com/ZNClub-PA-ML-AI/Sentiment-analysis-using-Business-News/95e16a9b/REL_score_open.json


$.getJSON('https://cdn.rawgit.com/ZNClub-PA-ML-AI/Sentiment-analysis-using-Business-News/95e16a9b/REL_score_open.json', function(data) {

  //console.log(data.score);



  var map = data.score;
  var response=[];
  
  for (var key in map) {
    if (map.hasOwnProperty(key)) {
      //console.log(key + " -> " + map[key]);

      //split date ie key
      var dates = key.split('-');
			if(dates[0]=='2015'){
      	console.log("2015");
        continue;
      }
      //adjust month
      var m = dates[1];
      m = parseInt(m) - 1;
      m = m.toString()
      if (m.length == 1) {
        m = "0" + m;
      }
      var dateUTC = Date.UTC(dates[0],m,dates[2]);
      var score = map[key];
      var temp=[dateUTC,score];
      
      //console.log(temp);
      
      response.push(temp);
    }
  }

console.log(response);

  Highcharts.chart('container2', {
    chart: {
      type: 'spline',
      zoomType: 'x'
    },
    title: {
      text: 'Market News Sentimental Graph'
    },
    subtitle: {
      text: 'Sentiment-analysis-using-Business-News'
    },
    xAxis: {
      type: 'datetime',
      dateTimeLabelFormats: { // don't display the dummy year
        month: '%e. %b',
        year: '%b'
      },
      title: {
        text: 'Months'
      }
    },
    yAxis: {
      title: {
        text: 'Sentimental Score'
      },
      min: -0.30
    },
    tooltip: {
      headerFormat: '<b>{series.name}</b><br>',
      pointFormat: '{point.x:%e. %b}: {point.y:.3f} value'
    },

    plotOptions: {
      spline: {
        marker: {
          enabled: true
        }
      }
    },

    series: [{
      name: 'RELIANCE',
      // Define the data points. All series have a dummy year
      // of 1970/71 in order to be compared on the same x axis. Note
      // that in JavaScript, months start at 0 for January, 1 for February etc.
      data: response


      
    }]
  });

});
