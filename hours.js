var dinner_start = moment('17:00', 'HH:mm');
var dinner_end = moment('19:30', 'HH:mm');

moment().isBefore(dinner_end);

function Hours(startTime, endTime) {
    this.start = startTime;
    this.end = endTime;

    this.isOpen = function() {
	return (moment().isAfter(end) && moment().isBefore(end))
    }
}

function Day(meals) {
    this.meals = meals;

function Hall(name, days) {
    this.name = name;
    this.weekday = Day(days[0]);
    this.fri = Day(days[1]);
    this.sat = Day(days[2]);
    this.sun = Day(days[3]);

    
}

commons = new Hall("commons");
