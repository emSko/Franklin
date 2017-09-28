/**
 * Created by kacper on 19.07.17.
 */

function updateTextInput(val) {
	var div = document.getElementsByClassName("ValofSlider");
	div.textContent = val;
}

function sliders(element) {

            var id = element.id;
            if(id.substr(0, 1) == 't'){
                id = id.substr(11, id.length);
                $.ajax({
                   type: 'POST',
                   url: 'http://192.168.100.190:5000/bulb/'+id+'/set-light-temperature',
                   data: JSON.stringify({'data': $('#temperature' + id).val()}),
                   contentType: 'application/json',
                   dataType: 'json',
                   /*error: function (xhr, ajaxOptions, thrownError) {
                       alert(xhr.status);
                       alert(thrownError);
                   }*/
               });

            } else if(id.substr(0, 1) == 'b') {
                id = id.substr(10, id.length);
                $.ajax({
                    type: 'POST',
                   url: 'http://192.168.100.190:5000/bulb/'+id+'/set-light-level',
                   data: JSON.stringify({'data': $('#brightness' + id).val()}),
                   contentType: 'application/json',
                   dataType: 'json',

                   /*error: function (xhr, ajaxOptions, thrownError) {
                       alert(xhr.status);
                       alert(thrownError);
                   }*/
                });
            } else {
                if(id.substr(0, 1) == 'h')
                    id = id.substr(3, id.length);
                else
                    id = id.substr(10, id.length);
                $.ajax({
                    type: 'POST',
                   url: 'http://192.168.100.190:5000/bulb/'+id+'/set-color',
                   data: JSON.stringify({'hue': $('#hue' + id).val(), 'saturation': $('#saturation' + id).val()}),
                   contentType: 'application/json',
                   dataType: 'json',

                   /*error: function (xhr, ajaxOptions, thrownError) {
                       alert(xhr.status);
                       alert(thrownError);
                   }*/
                });
            }
}
