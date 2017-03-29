//getJSON
//https://cdn.rawgit.com/ZNClub-PA-ML-AI/Sentiment-analysis-using-Business-News/54103f1e/data/json/REL_qs.json

$.getJSON('https://cdn.rawgit.com/ZNClub-PA-ML-AI/Sentiment-analysis-using-Business-News/54103f1e/data/json/REL_qs.json',
  function(data) {
    //console.log(data['Unnamed: 0'][0]);

    var price = [];
    var sentiment = [];
    var size = Object.keys(data.Open).length;
    console.log(size);

    for (var i = 0; i < size; i += 1) {
      var temp = data['Unnamed: 0'][i];
      //split date ie key

      var dates = temp.split('-');
      //adjust month
      var m = dates[1];
      m = parseInt(m) - 1;
      m = m.toString()
      if (m.length == 1) {
        m = "0" + m;
      }
      var dateUTC = Date.UTC(dates[0], m, dates[2]);

      price.push([dateUTC, data.Open[i]]);
      sentiment.push([dateUTC, data.open_score[i]]);
      //console.log(i);
      //console.log(price[i]);
    }




    Highcharts.chart('container3', {
      chart: {
        zoomType: 'x'
      },
      title: {
        text: 'Open Price and Market sentiment'
      },
      subtitle: {
        text: 'Sentiment-analysis-using-Business-News'
      },
      xAxis: [{
        type: 'datetime',
        //categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        crosshair: true
      }],
      yAxis: [{ // Primary yAxis
        labels: {
          format: '{value} Rs',
          style: {
            color: Highcharts.getOptions().colors[1]
          }
        },
        title: {
          text: 'Stock Open Price',
          style: {
            color: Highcharts.getOptions().colors[1]
          }
        }
      }, { // Secondary yAxis
        title: {
          text: 'Sentiment Score',
          style: {
            color: Highcharts.getOptions().colors[0]
          }
        },
        labels: {
          format: '{value}',
          style: {
            color: Highcharts.getOptions().colors[0]
          }
        },
        opposite: true
      }],
      tooltip: {
        shared: true
      },
      legend: {
        layout: 'vertical',
        align: 'left',
        x: 70,
        y: 12,
        verticalAlign: 'top',

        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
      },
      series: [{
        name: 'Sentiment',
        type: 'spline',
        yAxis: 1,
        data: sentiment
          /*    [
                [Date.UTC(2017, 02, 22), -0.49],
                [Date.UTC(2017, 02, 23), 0.02],
                [Date.UTC(2017, 02, 28), -0.20]

              ]*/
          ,
        tooltip: {
          valueSuffix: ' '
        }

      }, {
        name: 'Open Price',
        type: 'spline',
        data: price
          /*    [
                [Date.UTC(2017, 02, 22), 1149.9],
                [Date.UTC(2017, 02, 23), 1171.5],
                [Date.UTC(2017, 02, 28), 1100.4]
              ]*/
          ,
        tooltip: {
          valueSuffix: 'Rs'
        }
      }]
    });



  });
