var canAttendMeetings = function(intervals) {
    
    intervals.sort((a, b) => a[0] - b[0]);
    for (let i = 0; i < intervals.length; i++) {
        if (i && intervals[i][0] < intervals[i-1][1]) return false
    }
    return true
};

