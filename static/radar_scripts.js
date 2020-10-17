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
        Popularity = []
        Tempo = []
        Valence = []
        headers = []
        
        data.forEach(function(d){
        //Issue: Needed to add in additional attributes
        //Issue: Certain genres given 1 value by default obviously misrepresenting actual data values   
            Danceability.push(d.Danceability)
            Duration.push(d.Duration)
            Energy.push(d.Energy)
            Liveness.push(d.Liveness)
            Loudness.push(d.Loudness)
            Popularity.push(d.Popularity)
            Tempo.push(d.Tempo)
            Valence.push(d.Valence)
            headers.push(d.top_genre)
        })
        
        norm_Danceability = Danceability.map(x => (x-Math.min(...Danceability))/(Math.max(...Danceability)-Math.min(...Danceability)))
        norm_Duration = Duration.map(x => (x-Math.min(...Duration))/(Math.max(...Duration)-Math.min(...Duration)))
        norm_Energy = Energy.map(x => (x-Math.min(...Energy))/(Math.max(...Energy)-Math.min(...Energy)))
        norm_Liveness = Liveness.map(x => (x-Math.min(...Liveness))/(Math.max(...Liveness)-Math.min(...Liveness)))
        norm_Loudness = Loudness.map(x => (x-Math.min(...Loudness))/(Math.max(...Loudness)-Math.min(...Loudness)))
        norm_Popularity = Popularity.map(x => (x-Math.min(...Popularity))/(Math.max(...Popularity)-Math.min(...Popularity)))
        norm_Tempo = Tempo.map(x => (x-Math.min(...Tempo))/(Math.max(...Tempo)-Math.min(...Tempo)))
        norm_Valence = Valence.map(x => (x-Math.min(...Valence))/(Math.max(...Valence)-Math.min(...Valence)))

        Danceability = ['Danceability'].concat(norm_Danceability)
        Duration = ['Duration'].concat(norm_Duration)
        Energy = ['Energy'].concat(norm_Energy)
        Liveness = ['Liveness'].concat(norm_Liveness)
        Loudness = ['Loudness'].concat(norm_Loudness)
        Popularity = ['Popularity'].concat(norm_Popularity)
        Tempo = ['Tempo'].concat(norm_Tempo)
        Valence = ['Valence'].concat(norm_Valence)
        headers = ['#'].concat(headers)
        
        //Test to eliminate faulty data representation
        console.log(Valence)

        var chartData = {
            title: 'Top Spotify Songs by Attributes (1999-2019)',
            header: headers,
            rows: [
                Danceability,
                Duration,
                Energy,
                Liveness,
                Loudness,
                Popularity,
                Tempo,
                Valence
            ]
        };
        // create radar chart
        var chart = anychart.radar();

        // set default series type
        //chart.defaultSeriesType('area');
        chart
        .title('Comparison Chart')
        
        // set chart legend
        .legend(true);

        // set chart data
        chart.data(chartData);
        
        // force chart to stack values by Y scale.
        chart.yScale().minimum(0).maximum(1).ticks({ interval:0.25}).stackMode('percent');
        
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
d3.select("#update_radar").on("click", function(){update_radar()})