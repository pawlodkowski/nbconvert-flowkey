var now = new Date(); 
var curTimeStamp = now.toISOString().replace(/T/, ' @ ').replace(/\..+/, '').replace(/\-/g, '.');
document.getElementById("datetime").innerHTML = '<strong>' + curTimeStamp + ' (UTC)</strong>';