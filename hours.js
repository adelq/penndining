function Hours(startTime, endTime) {
    this.start = startTime;
    this.end = endTime;

    this.isOpen = function() {
	return (moment().isAfter(end) && moment().isBefore(end))
    }
}

commons = {
  "name": "1920 Commons",
  "weekdays": {
    "lunch": {
        "start": "11:00",
        "end": "14:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "21:00"
    }
  },
  "friday": {
    "lunch": {
        "start": "11:00",
        "end": "14:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "21:00"
    }
  },
  "saturday": {
    "lunch": {
        "start": "11:00",
        "end": "14:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "21:00"
    }
  },
  "sunday": {
    "lunch": {
        "start": "11:00",
        "end": "14:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "21:00"
    }
  }
}

hill = {
  "name": "Hill",
  "weekdays": {
    "breakfast": {
        "start": "7:30",
        "end": "10:00"
    },
    "lunch": {
        "start": "11:00",
        "end": "14:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "20:00"
    }
  },
  "friday": {
    "breakfast": {
        "start": "7:30",
        "end": "10:00"
    },
    "lunch": {
        "start": "11:00",
        "end": "14:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "19:00"
    }
  },
  "saturday": {
    "brunch": {
        "start": "11:00",
        "end": "15:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "19:00"
    }
  },
  "sunday": {
    "brunch": {
        "start": "11:00",
        "end": "15:00"
    },
    "dinner": {
        "start": "17:00",
        "end": "20:00"
    }
  }
}
