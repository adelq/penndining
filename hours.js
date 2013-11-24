function Hours(name, startTime, endTime) {
    this.name = name;
    this.start = moment(startTime, 'HH:mm');
    this.end = moment(endTime, 'HH:mm');

    this.isOpen = function() {
	   return (moment().isAfter(this.start) && moment().isBefore(this.end))
    }
}

commons = {
  "name": "1920 Commons",
  "weekdays": [
    new Hours("Lunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "21:00")
  ],
  "friday": [
    new Hours("Lunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "21:00")
  ],
  "saturday": [
    new Hours("Brunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "21:00")
  ],
  "sunday": [
    new Hours("Brunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "21:00")
  ]
}

hill = {
  "name": "Hill",
  "weekdays": [
    new Hours("Breakfast", "07:30", "10:00"),
    new Hours("Lunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "20:00")
  ],
  "friday": [
    new Hours("Breakfast", "07:30", "10:00"),
    new Hours("Lunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "19:00")
  ],
  "saturday": [
    new Hours("Brunch", "11:00", "15:00"),
    new Hours("Dinner", "17:00", "19:00")
  ],
  "sunday": [
    new Hours("Brunch", "11:00", "15:00"),
    new Hours("Dinner", "17:00", "20:00")
  ]
}

commons_is_open = false;

if (isOpen(commons)) {
    $('#commons').addClass('label-success').removeClass('label-danger').text('Open');
}

function openDay(day) {
    var open = false;
    for (var i = 0; i<day.length; i++) {
        open = (open || day[i].isOpen())
    }
    return open
}

function isOpen(hall) {
    var day = moment().day();
    if (day === 5) {
        var meals = hall.friday;
    } else if (day === 6){
        var meals = hall.saturday;
    } else if (day === 0) {
        var meals = hall.sunday;
        console.log(openDay(hall.sunday));
    } else {
        var meals = hall.weekdays;
    }
}
