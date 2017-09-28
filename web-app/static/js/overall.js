/**
 * Created by kacper on 8/9/17.
 */


function GetDynamicPanelIkeaGU10(id, name) {
    return '<div class="panel">' +
        '<h2>' + name + '</h2>' +
        '<p>Brightness</p>' +
        '<input class="slider" id="brightness' + id + '" type="range" max="100" onclick="sliders(this)"></input>' +
        '<p>Temperature</p>' +
        '<input class="slider" id="temperature' + id + '" type="range" max="100" onclick="sliders(this)"></input>' +
        '<p>Color</p>' +
        '<p class="color">hue</p><p class="color">saturation</p><div id="nl"></div>' +
        '<input class="slider1" id="hue' + id + '" type="range" max="360" onclick="sliders(this)"></input>' +
        '<input class="slider1" id="saturation' + id + '" type="range" max="100" onclick="sliders(this)"></input>' +
        '</br><input type="button" class="on" id="on' + id + '" value="turn on" onclick="turn_on(this)"></input>' +
        '<input type="button" class="off" id="off' + id + '" value="turn off" onclick="turn_off(this)"></input>' +
        '</div>';
}

window.onload = $(function(){
   $.ajax({
       url: 'http://192.168.100.190:5000/home/bulbs',

       contentType: 'application/json',

       success: function (data) {

           if (data.status == 'success') {
               for (i = 0; i < data.message.length; i++) {
                   $("#container").append(GetDynamicPanelIkeaGU10(data.message[i].serialNo, data.message[i].name));
               }
           } else {
               alert('No connection to the homegate')
           }
       },
       error: function (xhr, ajaxOptions, thrownError) {
           alert(xhr.status);
       }
   });
});