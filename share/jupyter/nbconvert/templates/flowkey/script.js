var timestamp = document.getElementById('timestamp_container');
var header = document.getElementById('header');
header.parentNode.insertBefore(timestamp, header.nextSibling);

var execSummary = document.getElementById('executive-summary-text');
var placeholder = document.getElementById('executive-summary-placeholder');
placeholder.appendChild(execSummary);