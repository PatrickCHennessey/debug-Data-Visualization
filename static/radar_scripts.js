//const update_radar = () => {
function update_radar() {

    // Get year from dropdown selector
    let e = document.getElementById("year_selector");
    let year = e.options[e.selectedIndex].text;
    console.log(year);

    d3.select("#radar_container")
    //google d3 select element and clear .html set to indie string)

    // Call MONGODB API with the year using fetch command
    d3.json(`/api/${year}`) // flask is accepting input from year as argument
    //.then(response => response.json())
    .then(function(data){
        console.log(data)
        
        Danceability = []
        Duration = []
        Energy = []
        Liveness = []
        Loudness = []
        headers = []
        
        data.forEach(function(d){
            // Add in missing Spotify ranges 
            Danceability.push(d.Danceability)
            Duration.push(d.Duration)
            Energy.push(d.Energy)
            Liveness.push(d.Liveness)
            Loudness.push(d.Loudness)
            
            headers.push(d.top_genre)
        })
        
        // Add in missing Spotify ranges
        norm_Danceability = Danceability.map(x => (x-Math.min(...Danceability))/(Math.max(...Danceability)-Math.min(...Danceability)))
        norm_Duration = Duration.map(x => (x-Math.min(...Duration))/(Math.max(...Duration)-Math.min(...Duration)))
        norm_Energy = Energy.map(x => (x-Math.min(...Energy))/(Math.max(...Energy)-Math.min(...Energy)))
        norm_Liveness = Liveness.map(x => (x-Math.min(...Liveness))/(Math.max(...Liveness)-Math.min(...Liveness)))
        norm_Loudness = Loudness.map(x => (x-Math.min(...Loudness))/(Math.max(...Loudness)-Math.min(...Loudness)))
        
        // Add in missing Spotify ranges
        Danceability = ['Danceability'].concat(norm_Danceability)
        Duration = ['Duration'].concat(norm_Duration)
        Energy = ['Energy'].concat(norm_Energy)
        Liveness = ['Liveness'].concat(norm_Liveness)
        Loudness = ['Loudness'].concat(norm_Loudness)
        headers = ['#'].concat(headers)

        var chartData = {
            title: 'Top Spotify Songs by Attributes (1999-2019)',
            header: headers,
            rows: [
                Danceability,
                Duration,
                Energy,
                Liveness,
                Loudness
                //Add other Spotify attributes here as well
            ]
        };
        // create radar chart
        var chart = anychart.radar();

        // set default series type
        chart.defaultSeriesType('area');

        // set chart data
        chart.data(chartData);
        
        // force chart to stack values by Y scale.
        chart.yScale().stackMode('percent');
        
        // set yAxis settings
        chart.yAxis().stroke('#545f69');
        chart.yAxis().ticks().stroke('#545f69');

        // set yAxis labels settings
        chart.yAxis().labels().fontColor('#545f69').format('{%Value}%');

        // set xAxis labels appearance settings
        var xAxisLabels = chart.xAxis().labels();
        xAxisLabels.padding(5);

        // set chart legend settings
        chart.legend().enabled(true).align('center').position('center-bottom');

        // set container id for the chart
        chart.container('radar_container');

        // initiate chart drawing
        chart.draw();

    }).catch(function(error){console.log(error)});

}
//Event Listener
d3.select("#update_radar").on("click"), update_radar()
    


    // Left off here 10/15/2020: Problem with JS attempts to decode the reply from MongoDB XXXXXXX
    // Current Issue: Getting the data from Mongo DB into Javascript
    // use of filter function on variable year


    // Sanhita : Will need to convert Music_Genre.ipynb into a music_genre.py
    // Sanhita: Will then need to create a route in app.py to call music_genre.py
    // Sanhita: Conversion will be very similar to "Mission to MArs scrape example" used
    //              in scrape_mars.py

    // Read response from API


    // Update/display the graph





//the codes for the viz (AnyChart)


// anychart.onDocumentReady(function () {
//     // create data set on our data
//     var chartData = {
//       title: 'Region Sales by Year (2007-2011) (Stacked)',
//       header: ['#', 'Arizona', 'Florida', 'Nevada'],
//       rows: [
//         ['2007', 1368763, 1991297, 431097],
//         ['2008', 799873, 1254823, 561983],
//         ['2009', 1497653, 1732987, 1019874],
//         ['2010', 1351874, 332871, 2027634],
//         ['2011', 1582987, 649853, 1961085]
//       ]
//     };
  
//     // create radar chart
//     var chart = anychart.radar();
  
//     // set default series type
//     chart.defaultSeriesType('area');
  
//     // set chart data
//     chart.data(chartData);
  
//     // force chart to stack values by Y scale.
//     chart.yScale().stackMode('value');
  
//     // set yAxis settings
//     chart.yAxis().stroke('#545f69');
//     chart.yAxis().ticks().stroke('#545f69');
  
//     // set yAxis labels settings
//     chart
//       .yAxis()
//       .labels()
//       .fontColor('#545f69')
//       .format('{%Value}{scale:(1000000)|(M)}');
  
//     // set chart legend settings
//     chart.legend().align('center').position('center-bottom').enabled(true);
  
//     // set container id for the chart
//     chart.container('container');
//     // initiate chart drawing
//     chart.draw();
//   });