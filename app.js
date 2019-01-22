async function updateData()
{
    document.getElementById("locdiv").style.display='none';
    document.getElementById("updt").style.display="none";
    document.getElementById("loader").style.display='block';
    
    
    /*req = await fetch('/combine', {headers: {
        'Access-Control-Allow-Origin':'*',
        'withCredentials': false
        }});
    data = await req.json();
    console.log(data);
    var lat = data.lat;
    var lng = data.lng;
    var typep = data.type;
    if (typep === 'ocean')
    {
        document.getElementById("loc").innerHTML = data.name;
        
    }
    else{
        document.getElementById("loc").innerHTML = data.name+", "+data.country;
        
    }
    document.getElementById("coords").innerHTML = data.lat+", "+data.lng;
    

    document.getElementById("loader").style.display='none';
    document.getElementById("locdiv").style.display="block";
    document.getElementById("updt").style.display="block";
    document.getElementById("updt").innerHTML = "<i>As of "+getFormattedDate()+"</i>";*/

    
    /*var tag = document.createElement("script");
    // tag.src = 'http://api.open-notify.org/iss-now.json?callback=isscall';
    document.getElementsByTagName("head")[0].appendChild(tag);*/

    req = await fetch('https://api.wheretheiss.at/v1/satellites/25544');
    data = await req.json();
    
    lat = data.latitude;
    lng = data.longitude;
        
    req = await fetch('https://api.opencagedata.com/geocode/v1/json?key=5bc2c47154ee40e8bc401d3fa9bf77df&q='+lat+'%2C'+lng+'&pretty=1&no_annotations=1')
    data = await req.json()
    if(data.results[0].country)
        text = data.results[0].city+', '+data.results[0].country;
    else
        text = data.results[0].formatted;

    document.getElementById("loc").innerHTML = text;
        
        
    document.getElementById("coords").innerHTML = lat+", "+lng;
    document.getElementById("loader").style.display='none';
    document.getElementById("locdiv").style.display="block";
    document.getElementById("updt").style.display="block";
    document.getElementById("updt").innerHTML = "<i>As of "+getFormattedDate()+"</i>";
}





function getLocation() {
    if(navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      console.log("Geo Location not supported by browser");
    }
}
//function that retrieves the position
function showPosition(position) {
var location = {
    longitude: position.coords.longitude,
    latitude: position.coords.latitude
}
console.log(location);
    localStorage['user_loc']=location;
}
  

function reload(){
    
    location.reload();
}

function getFormattedDate() {
    var date = new Date();
    var str = date.getDate()  +"/" + (date.getMonth() + 1) + "/" + date.getFullYear() +  " "+ date.getHours() + ":" + date.getMinutes();

    return str;
}


window.addEventListener('load', async e => {
    
    console.log(navigator.onLine);
    if ('serviceWorker' in navigator) {
        try {
            navigator.serviceWorker.register('serviceworker.js');
            console.log('SW registered');
        } catch (error) {
            console.log('SW failed');

        }
    }
    doload();
    
    await updateData();
    
    
});
var hamburger_on = false;
var hamburger = function()
{
    document.getElementById('sidenav').animate(
        [
            // keyframes
            { transform: 'translateX(-100%)' }, 
            { transform: 'translateX(0%)' }
          ], { 
            // timing options
            duration: 500,
            easing: 'ease-out'
          }
    ).onfinish = function(){
    document.getElementById('sidenav').style.transform = 'translateX(0)';
    }
    hamburger_on=true;

}

var hamburger_out = function()
{
    if(hamburger_on){
    document.getElementById('sidenav').animate(
        [
            // keyframes
            { transform: 'translateX(0%)' }, 
            { transform: 'translateX(-100%)' }
          ], { 
            // timing options
            duration: 500,
            easing: 'ease-out'
          }
        ).onfinish = function(){
        document.getElementById('sidenav').style.transform = 'translateX(-100%)';
        }
        hamburger_on=false;
    }

}

var nextpass = function()
{
    if(!localStorage.getItem('user_loc'))
    {
        getloc();
    }
    

}
var getloc = function()
{
    getLocation();
    getLocation();
    
}
var doload = function()
{
    document.getElementById('hamburger').onclick = hamburger;
    document.getElementById('rightside').onclick = hamburger_out;
    document.getElementById('location-sn').onclick = getloc;
    document.getElementById('next-sn').onclick = nextpass;
    var rect = document.getElementById('earth').getBoundingClientRect();
    console.log(rect);
    centerX = (rect.right + rect.left )/2;
    centerY = (rect.top + rect.bottom)/2;
    console.log(centerX+" "+centerY);
    var sat = document.getElementById('sat');
    
    sat.style.left = rect.left+53+'px';
    sat.style.top = rect.top-45+'px';

    
}

document.addEventListener('DOMContentLoaded', doload);
window.addEventListener("resize", doload);


