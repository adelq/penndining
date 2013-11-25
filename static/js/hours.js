function Hours(name, startTime, endTime) {
    this.name = name;
    this.start = moment(startTime, 'HH:mm');
    this.end = moment(endTime, 'HH:mm');

    // Returns whether dining hall is open at given times
    // @return boolean
    this.isOpen = function() {
     return (moment().isAfter(this.start) && moment().isBefore(this.end));
    }

    // Returns the name of the dining hall if it is open, returns false otherwise
    // @return string/boolean
    this.open = function() {
        if (this.isOpen) {
            return this.name;
        } else {
            return false;
        }
    }

    // Returns whether dining hall is about to close
    // Closing defined as 30 minutes (1800 seconds)
    // @return boolean
    this.isClosing = function() {
        timeToClose = moment().diff(this.end, 'second');
        if (timeToClose > -1800 && timeToClose <= 0) {
            return true;
        } else {
            return false;
        }
    }

    // Returns how much time is left until hall closes
    // @return int (milliseconds)
    this.closingTime = function() {
        return moment().diff(this.end);
    }

    // Returns human readable amount of time until hall closes
    // @return string ("one minute")
    this.closingIn = function() {
        moment.lang('en');
        return moment.duration(moment().diff(this.end)).humanize();
    }
}

// JSON Objects representing each of the dining halls
// Contributions welcome
// TODO: Add more dining halls (Houston, King's Court, etc)
commons = {
  "name": "1920 Commons",
  "weekdays": [
    new Hours("Lunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "21:00")
  ],
  "friday": [
    new Hours("Lunch", "11:00", "14:00"),
    new Hours("Dinner", "17:00", "19:30")
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

// Main DOM manipulation function
// // Adds and removes classes to labels
// // Changes text in the label
function check() {
    if (isOpen(commons)) {
        if (isClosing(momentDay(commons))) {
            $('#commons-status')
		.addClass('label-warning')
		.removeClass('label-success')
		.removeClass('label-danger')
		.text('Closing in ' + isClosing(momentDay(commons)));
        } else{
            $('#commons-status')
		.addClass('label-success')
		.removeClass('label-danger')
		.removeClass('label-warning')
		.text('Open');
        }
    } else {
        $('#commons-status')
	    .addClass('label-danger')
	    .removeClass('label-success')
	    .removeClass('label-warning')
	    .text('Closed');
    }

    if (isOpen(hill)) {
        if (isClosing(momentDay(hill))) {
            $('#hill-status')
		.addClass('label-warning')
		.removeClass('label-danger')
		.removeClass('label-success')
		.text('Closing in ' + isClosing(momentDay(hill)));
        } else {
            $('#hill-status')
		.addClass('label-success')
		.removeClass('label-danger')
		.removeClass('label-warning')
		.text('Open');
        }
    } else {
        $('#hill-status').addClass('label-danger').removeClass('label-success').removeClass('label-warning').text('Closed');
    }

    if (isOpen(mcclelland)) {
        if (isClosing(momentDay(mcclelland))) {
            $('#mcclelland-status')
		.addClass('label-warning')
		.removeClass('label-danger')
		.removeClass('label-success')
		.text('Closing in ' + isClosing(momentDay(mcclelland)));
        } else {
            $('#mcclelland-status')
		.addClass('label-success')
		.removeClass('label-danger')
		.removeClass('label-warning')
		.text('Open');
        }
    } else {
        $('#mcclelland-status')
	    .addClass('label-danger')
	    .removeClass('label-success')
	    .removeClass('label-warning')
	    .text('Closed');
    }
}

// Returns boolean whether dining hall is open on given day
// @param day: array of Hours()
// @return boolean
function openDay(day) {
    var open = false;
    for (var i = 0; i<day.length; i++) {
        open = (open || day[i].isOpen());
    }
    return open;
}

// Returns whether hall is currently open
// @param hall: JSON object representing hall
// @return boolean
function isOpen(hall) {
    var day = moment().day();	// Current day of the week (int)
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

// Return whether dining hall is currently closing on given day
// @param day: array of Hours()
// @return boolean
function isClosing(day) {
    for (var i = 0; i<day.length; i++) {
        if (day[i].isClosing()) {
            return day[i].closingIn();
        }
    }
    return false;
}

// Return whether hall is closing
// Deprecated - not used in current iteration of code
// @return boolean
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
// @param hall: JSON object representing hall
// @return day: array of Hours()
function momentDay(hall) {
    var day = moment().day();	// Current day of the week (int)
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

// Running main code
check();			// Run checking code once immediately
setInterval(check, 2000);	// Run checking code every 2 seconds afterwards
