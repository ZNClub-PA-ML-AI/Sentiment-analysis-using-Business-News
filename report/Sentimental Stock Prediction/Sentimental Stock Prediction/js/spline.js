//https://cdn.rawgit.com/ZNClub-PA-ML-AI/Sentiment-analysis-using-Business-News/95e16a9b/REL_score_open.json

//https://cdn.rawgit.com/ZNClub-PA-ML-AI/Sentiment-analysis-using-Business-News/4d982b42/data/json/REL_sentiment.json

$.getJSON('https://cdn.rawgit.com/ZNClub-PA-ML-AI/Sentiment-analysis-using-Business-News/4d982b42/data/json/REL_sentiment.json', function(data) {

  //var close_map = data.close_score;
  var size = Object.keys(data.date).length;
  var close = [];
  var open = [];

  for (var i = 0; i < size; i += 1) {
    console.log(data.date[i]);
    console.log(data.open_score[i]);
    console.log(data.close_score[i]);

    //split date ie key
    var dates = data.date[i].split('-');
    //adjust month
    var m = dates[1];
    m = parseInt(m) - 1;
    m = m.toString()
    if (m.length == 1) {
      m = "0" + m;
    }
    var dateUTC = Date.UTC(dates[0], m, dates[2]);

    open.push([dateUTC, data.open_score[i]]);
    close.push([dateUTC, data.close_score[i]]);

  }

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
      min: -0.30,
      gridLineWidth: 0,
      alternateGridColor: null,
      plotBands: [{ 
          from: 0.05,
          to: -0.05,
          color: 'rgba(0, 0, 0, 0)',
          label: {
            text: 'NEUTRAL',
            style: {
              color: '#606060'
            }
          }
        }, { 
          from: 0.05,
          to: 0.2,
          color: 'rgba(100, 255, 100, 0.2)',
          label: {
            text: 'POSITIVE',
            style: {
              color: '#0FFF0F'
            }
          }
        }, { // Light air
          from: 0.2,
          to: 0.4,
          color: 'rgba(100, 255, 100, 0.4)',
          label: {
            text: 'HIGHLY POSITIVE',
            style: {
              color: '#00F000'
            }
          }
        }, { 
          from: -0.05,
          to: -0.2,
          color: 'rgba(255, 100, 100, 0.2)',
          label: {
            text: 'NEGATIVE',
            style: {
              color: '#FF0F0F'
            }
          }
        },{
          from: -0.2,
          to: -0.4,
          color: 'rgba(255, 100, 100, 0.5)',
          label: {
            text: 'HIGHLY NEGATIVE',
            style: {
              color: '#FF0000'
            }
          }
        }

      ]
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
      name: 'RELIANCE OP sentiment',
      data: open
    }, {
      name: 'RELIANCE CP sentiment',
      data: close
    }]
  });
});
