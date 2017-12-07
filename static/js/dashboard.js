// Pie chart for dashboard
function pie_chart() {
    var ctx = document.getElementById('pei_summary').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: ["Late", "Night Diff", "Undertime"],
            datasets: [{
                label: "",
                backgroundColor: ['#FFCC00', '#336688', '#FF9900'],
                borderColor: ['#FFCC00', '#336688', '#FF9900'],
                data: [8, 25, 4],
            }]
        },

        // Configuration options go here
        options: {}
    });
}

// Pie chart for dashboard
function pie_chart2() {
    var ctx = document.getElementById('pei_tardines').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: ["Absences", "Leave", "Lates"],
            datasets: [{
                label: "",
                backgroundColor: ['#F1582B', '#171717', '#F8981C'],
                borderColor: ['#F1582B', '#171717', '#F8981C'],
                data: [5, 2, 30],
            }]
        },

        // Configuration options go here
        options: {}
    });
}

function pei_attendace() {
    var ctx = document.getElementById('pei_attendace').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: ["Work Made", "Overtime", "Nigh Def"],
            datasets: [{
                label: "",
                backgroundColor: ['#17AB58', '#65479C', '#4356A6'],
                borderColor: ['#17AB58', '#65479C', '#4356A6'],
                data: [30, 5, 35],
            }]
        },

        // Configuration options go here
        options: {}
    });
}