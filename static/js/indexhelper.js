/**
 * Created by himanshu on 19/4/17.
 */

$(function () {

    $('.button-collapse').sideNav();

    $('#query').keypress(function(){

        if(this.value.length > 500){
            return false;
        }

        $("#remainingCharacters").html("Remaining characters : " +(500 - this.value.length));
    });

    $('#submitQuery').click(function () {

        var K = $('#query').val();

        $.post('/query', {'query' : K}, function (data, status) {

        });


    });

});


/*AIzaSyD-FJoLajGRJFINAUj5CJrCxXNl0YiZSf8  API Key*/




var map;
function initMap() {

    var Coordinates;

    navigator.geolocation.getCurrentPosition(function (place)
    {

        Coordinates = place.coords;
        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: Coordinates.latitude, lng: Coordinates.longitude},
            zoom: 16
        });

        var marker = new google.maps.Marker({
            position: {lat : Coordinates.latitude, lng : Coordinates.longitude },
            map: map
        });


    });

}


