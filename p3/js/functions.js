//maximum
function myMax() {
    "use strict";
    var a = document.getElementById("n1").value, b = document.getElementById("n2").value, c = document.getElementById("n3").value, temp;
    
    temp = Math.max(a, b, c);
    window.alert("The max of the three numbers is " + temp);
}

//minimum
function myMin() {
    "use strict";
    var a = document.getElementById("n1").value, b = document.getElementById("n2").value, c = document.getElementById("n3").value, temp;
    
    temp = Math.min(a, b, c);
    window.alert("the min of the three numbers is " + temp);
}

//average (arithmetic mean)
function myAverage() {
    "use strict";
    var a = parseInt(document.getElementById("n1").value, 10), b = parseInt(document.getElementById("n2").value, 10), c = parseInt(document.getElementById("n3").value, 10), average;
        
    average = (a + b + c) / 3;
    window.alert("the average of the three numbers is " + average);
}
//median
function myMedian() {
    "use strict";
    var a = parseInt(document.getElementById("n1").value, 10), b = parseInt(document.getElementById("n2").value, 10), c = parseInt(document.getElementById("n3").value, 10), median;
    
    window.alert("Hello");
    
    if (a >= b && a >= c && b >= c) {
        median = b;
    }
    else if (a >= b && a >= c && c >= b) {
        median = c;
    }
    else if (b >= a && b >= c && a >= c) {
        median = a;
    }
    else if (b >= a && b >= c && c >= a) {
        median = c;
    }
    else if (c >= a && c >= b && a >= b) {
        median = a;
    }
    else if (c >= a && c >= b && b >= a) {
        median = b;
    }

    window.alert("the median of the three numbers is " + median);
}

//range (max - min)
function myRange() {
    "use strict";
    var a = document.getElementById("n1").value, b = document.getElementById("n2").value, c = document.getElementById("n3").value, range;
    
    range = Math.max(a, b, c) - Math.min(a, b, c);
    window.alert("the range of the three numbers is " + range);
}