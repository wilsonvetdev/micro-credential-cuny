let $A = 8;
let $B = 2;
let $C = 0;
let result;

document.write(`$A=8, $B=2, $C=0`);
result = $A + $B;
document.write("<p>The answer for $A + $B is " + result + " .</p>");
result = $A - $B;
document.write("<p>The answer for $A - $B is " + result + " .</p>");
result = $A / $B;
document.write("<p>The answer for $A / $B is " + result + " .</p>");
result = $A * $B;
document.write("<p>The answer for $A * $B is " + result + " .</p>");
result = $A % $B;
document.write("<p>The answer for $A % $B is " + result + " .</p>");

let theOnlyH1 = document.querySelector('h1')
theOnlyH1.textContent = 'Assignment Operators +, -, /, *, %'