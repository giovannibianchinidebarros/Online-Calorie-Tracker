const carbs = document.querySelectorAll(".row-item-carbs");
const proteins = document.querySelectorAll(".row-item-protein");
const fats = document.querySelectorAll(".row-item-fats");
const fiber = document.querySelectorAll(".row-item-fiber");
const calories = document.querySelectorAll(".row-item-calories");

var carbsCount = 0;
var proteinCount = 0;
var fatCount = 0;
var fiberCount = 0;
var calorieCount = 0;

for (let item of carbs) carbsCount += parseFloat(item.innerHTML);

for (let item of proteins) proteinCount += parseFloat(item.innerHTML);

for (let item of fats) fatCount += parseFloat(item.innerHTML);

for (let item of fiber) fiberCount += parseFloat(item.innerHTML);

for (let item of calories) calorieCount += parseFloat(item.innerHTML);

document.getElementById("totalCarbs").innerHTML = carbsCount.toFixed(2);
document.getElementById("totalProtein").innerHTML = proteinCount.toFixed(2);
document.getElementById("totalFats").innerHTML = fatCount.toFixed(2);
document.getElementById("totalFiber").innerHTML = fiberCount.toFixed(2);
document.getElementById("totalCalories").innerHTML = calorieCount.toFixed(0);

//////////////////////////////////////////////////////////////////////

var calorieExpected = 2000;
var caloriePct = (calorieCount / calorieExpected) * 100;
document
  .getElementById("caloriePct")
  .setAttribute("style", "width: " + caloriePct + "%");

var fiberExpected = 18;
var fiberPct = (fiberCount / fiberExpected) * 100;
document
  .getElementById("fiberPct")
  .setAttribute("style", "width: " + fiberPct + "%");

//////////////////////////////////////////////////////////////////////

var total = carbsCount + proteinCount + fatCount;
var carbsPct = (carbsCount / total) * 100;
var proteinPct = (proteinCount / total) * 100;
var fatPct = (fatCount / total) * 100;

const ctx = document.getElementById("myChart");

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: [
      `Fats: ${fatPct.toFixed(0)}%`,
      `Protein: ${proteinPct.toFixed(0)}%`,
      `Carbs: ${carbsPct.toFixed(0)}%`,
    ],
    datasets: [
      {
        data: [fatPct, proteinPct, carbsPct],
        backgroundColor: [
          "rgb(255, 99, 132)",
          "rgb(54, 162, 235)",
          "rgb(255, 205, 86)",
        ],
        borderWidth: 1,
      },
    ],
  },
});
