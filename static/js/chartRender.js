"use strict";

async function getData(url) {

    let response = await fetch(url);

    if (response.ok) {
        let json = await response.json();
        const dataset = JSON.parse(JSON.stringify(json));
        console.log(dataset)
        return dataset

    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function renderChart(url, chartLabel, xlabel, ylabel) {


    const type = 'bar';
    let json = await getData(url);
    console.log(json);
    let dataset = {}
    let mainLabels = []
    let labels = [];

    for (var key in json.data) {
        for (let k in json.data[key]) {
            if (k != "name") {
                if (!(k in dataset)) dataset[k] = [json.data[key][k]]
                else dataset[k].push(json.data[key][k])

                if (!labels.includes(k)) labels.push(k)

            } else {
                mainLabels.push(json.data[key][k])
            }

        }
    }

    // compute colors step in hsl
    let colors = [];
    let diff = 360 / labels.length;
    for (let i = 0; i < labels.length; i++) {

        if (colors[i - 1]) colors.push(diff + colors[i - 1]);
        else colors.push(diff);
    }


    let datasets = []
    let i = 0;
    for (let key in dataset) {
        datasets.push({
            label: key,
            data: dataset[key],
            backgroundColor: `hsla(${colors[i]}, 80%, 60%, .5)`,
        })
        i++;
    }

    const config = {
        type: type,
        data: {
            labels: mainLabels,
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                },
                title: {
                    display: true,
                    align: 'center',
                    text: chartLabel
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: xlabel
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: ylabel
                    }
                }
            }
        },
    };


    const ctx = document.getElementById('chart').getContext('2d');

    const chart = new Chart(ctx, config);

}
