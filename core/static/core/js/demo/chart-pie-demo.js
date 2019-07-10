
// $( document ).ready(function() {
//   var remainingUnits = $('#remaining-units').html();
//   console.log(remainingUnits);
// });

// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';


var remainingUnits = parseInt($('#remaining-units').html());

var passedUnits = parseInt($('#passed-units').html());

var passedPer = (passedUnits/remainingUnits) *100;

var remainingPer = 100 - passedPer;



var x = $('#passed-units-span').html(passedPer + "%");

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["گذرانده شده", "باید گذرانده شود"],
    datasets: [{
      data: [passedPer , remainingPer],
      backgroundColor: ['#90EE90' ,'#ffae42'],
      hoverBackgroundColor: ['#198643','#ff7034'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    // tooltips: {
    //   backgroundColor: "rgb(255,255,255)",
    //   bodyFontColor: "#858796",
    //   borderColor: '#dddfeb',
    //   borderWidth: 1,
    //   xPadding: 15,
    //   yPadding: 15,
    //   displayColors: false,
    //   caretPadding: 10,
    // },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },

});
