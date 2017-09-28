function turn_on(element) {

    var id = element.id;
    id = id.substr(2, id.length);

    var xhr = new XMLHttpRequest();
    var url = 'http://192.168.100.190:5000/bulb/'+id+'/on';
    xhr.open("POST", url, true);
    xhr.send();
}


function turn_off(element) {

    var id = element.id;
    id = id.substr(3, id.length);

    var xhr = new XMLHttpRequest();
    var url = 'http://192.168.100.190:5000/bulb/'+id+'/off';
    xhr.open("POST", url, true);
    xhr.send();

}


function reload() {

    var xhr = new XMLHttpRequest();
    var url = 'http://192.168.100.190:5000/home/reload';
    xhr.open("POST", url, true);
    xhr.send();
}