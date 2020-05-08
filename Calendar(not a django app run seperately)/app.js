console.log("Calendar");
let startYear = 1900;
let yearGrid = document.querySelector(".yearGrid");
let backward = document.getElementById("backward");
let forward = document.getElementById("forward");

// yearGrid construction
function yearGridContruction() {
    function yearGridTable(startYear) {
        yearGrid.innerHTML = "";
        for (let i = 0; i < 30; i++) {
            yearGrid.innerHTML += `<div class="item">${i + startYear}</div>`;
        }
    }
    yearGridTable(startYear);
    backward.addEventListener("click", function (e) {
        startYear -= 30;
        yearGridTable(startYear);
        yearToMonth();
    });

    forward.addEventListener("click", function (e) {
        startYear += 30;
        yearGridTable(startYear);
        yearToMonth();
    });
}

// main calendar grid construction
function calendarGridConstruction() {
    let dayMonth = document.querySelector(".month");
    dayMonth = dayMonth.innerText.split(" ");
    let initialDate = dayMonth[0] + " 1 " + dayMonth[1];
    initialDate = new Date(initialDate);
    function daysInMonth(anyDateInMonth) {
        return new Date(
            anyDateInMonth.getFullYear(),
            anyDateInMonth.getMonth() + 1,
            0
        ).getDate();
    }

    console.log(initialDate.getDay(), daysInMonth(initialDate));

    let calendar = document.querySelector(".calendarContainer");
    function calendarGridTable(start, numDays) {
        calendar.innerHTML = "";
        for (let i = 1; i <= 42; i++) {
            if (i < start || i - start >= numDays) {
                if(i==36)
                    break;
                calendar.innerHTML += `<div class="item"></div>`;
            } else {
                calendar.innerHTML += `<div class="item">${
                    i - start + 1
                }</div>`;
            }
        }
    }

    calendarGridTable(
        parseInt(initialDate.getDay())+1,
        parseInt(daysInMonth(initialDate))
    );
    // Date retrieval
    Array.from(calendar.children).forEach(function (ele) {
        ele.addEventListener("click", function (e) {
            let someDate = new Date(initialDate);
            someDate.setDate(someDate.getDate() + parseInt(ele.innerText) - 1);
            console.log(someDate, initialDate);
        });
    });
}
calendarGridConstruction();

// Retrieving month and year

function yearToMonth() {
    Array.from(yearGrid.children).forEach(function (ele) {
        ele.addEventListener("click", function (e) {
            let year = ele.innerText;
            let yearGrid = document.querySelector(".yearCalendar");
            yearGrid.className += " disabled";
            let monthGrid = document.querySelector(".calendarMonthContainer");
            monthGrid.className = monthGrid.classList[0];
            console.log("hello", year);
            monthToCalendar(year);
        });
    });
}

function monthToCalendar(year) {
    let months = document.querySelector(".calendarMonth");
    Array.from(months.children).forEach(function(ele) {
        ele.addEventListener('click',function(e) {
            let month=ele.innerText;
            // console.log(ele,month);
            let yearMonth=document.querySelector('.month');
            yearMonth.innerHTML=`${month} ${year}`;

            let monthGrid = document.querySelector(".calendarMonthContainer");
            monthGrid.className += " disabled";            
            let calendar = document.querySelector(".calendar");
            calendar.className=calendar.classList[0];
            calendarGridConstruction();
        })
    })
}

dayMonth = document.querySelector(".month");
dayMonth.addEventListener("click", function () {
    yearGridContruction();
    let calendar = document.querySelector(".calendar");
    calendar.className += " disabled";
    let yearCalendar = document.querySelector(".yearCalendar");
    yearCalendar.className = yearCalendar.classList[0];

    yearToMonth();
});
