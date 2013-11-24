function Hours(name, startTime, endTime) {
    this.name = name;
    this.start = moment(startTime, 'HH:mm');
    this.end = moment(endTime, 'HH:mm');

    this.isOpen = function() {
     return (moment().isAfter(this.start) && moment().isBefore(this.end));
    }

    this.open = function() {
        if (this.isOpen) {
            return this.name;
        } else {
            return "Closed";
        }
    }

    this.isClosing = function() {
        timeToClose = moment().diff(this.end, 'second');
        if (timeToClose > -1800 && timeToClose <= 0) {
            return true;
        } else {
            return false;
        }
    }

    this.closingTime = function() {
        return moment().diff(this.end);
    }

    this.closingIn = function() {
        moment.lang('en');
        return moment.duration(moment().diff(this.end)).humanize();
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

mcclelland = {
  "name": "McClelland",
  "weekdays": [
    new Hours("Meal", "08:00", "20:00")
  ],
  "friday": [
    new Hours("Meal", "08:00", "20:00")
  ],
  "saturday": [
    new Hours("Meal", "12:00", "14:00")
  ],
  "sunday": [
    new Hours("Meal", "12:00", "14:00")
  ]
}

function check() {
    if (isOpen(commons)) {
        if (isClosing(momentDay(commons))) {
            $('#commons-status').addClass('label-warning').removeClass('label-success').removeClass('label-danger').text('Closing in ' + isClosing(momentDay(commons)));
        } else{
            $('#commons-status').addClass('label-success').removeClass('label-danger').removeClass('label-warning').text('Open');
        }
    } else {
        $('#commons-status').addClass('label-danger').removeClass('label-success').removeClass('label-warning').text('Closed');
    }

    if (isOpen(hill)) {
        if (isClosing(momentDay(hill))) {
            $('#hill-status').addClass('label-warning').removeClass('label-danger').removeClass('label-success').text('Closing in ' + isClosing(momentDay(hill)));
        } else {
            $('#hill-status').addClass('label-success').removeClass('label-danger').removeClass('label-warning').text('Open');
        }
    } else {
        $('#hill-status').addClass('label-danger').removeClass('label-success').removeClass('label-warning').text('Closed');
    }

    if (isOpen(mcclelland)) {
        if (isClosing(momentDay(mcclelland))) {
            $('#mcclelland-status').addClass('label-warning').removeClass('label-danger').removeClass('label-success').text('Closing in ' + isClosing(momentDay(mcclelland)));
        } else {
            $('#mcclelland-status').addClass('label-success').removeClass('label-danger').removeClass('label-warning').text('Open');
        }
    } else {
        $('#mcclelland-status').addClass('label-danger').removeClass('label-success').removeClass('label-warning').text('Closed');
    }
}

function openDay(day) {
    var open = false;
    for (var i = 0; i<day.length; i++) {
        open = (open || day[i].isOpen());
    }
    return open;
}

function isOpen(hall) {
    var day = moment().day();
    if (day === 5) {
        return openDay(hall.friday);
    } else if (day === 6){
        return openDay(hall.saturday);
    } else if (day === 0) {
        return openDay(hall.sunday);
    } else {
        return openDay(hall.weekdays);
    }
}

function isClosing(day) {
    for (var i = 0; i<day.length; i++) {
        if (day[i].isClosing()) {
            return day[i].closingIn();
        }
    }
    return false;
}

function timeToClose() {
    if (isOpen(hall)) {
        var day = moment().day();
        if (day === 5) {
            return isClosing(hall.friday);
        } else if (day === 6){
            return isClosing(hall.saturday);
        } else if (day === 0) {
            return isClosing(hall.sunday);
        } else {
            return isClosing(hall.weekdays);
        }  
    } else {
        return "Closed"
    }
}

// Helpful for future refactoring
function momentDay(hall) {
    var day = moment().day();
    if (day === 5) {
        return hall.friday;
    } else if (day === 6){
        return hall.saturday;
    } else if (day === 0) {
        return hall.sunday;
    } else {
        return hall.weekdays;
    }
}

check();
setInterval(check, 2000);
