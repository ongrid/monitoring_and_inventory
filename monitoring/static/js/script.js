$(document).ready(function () {
    for (var i = 0; i < $('.worker').length; i++) {
        var hr = $('.worker:eq('+i+')').data('claymore');
        if (Number(hr) == 0) {
            $('.worker:eq('+i+')').addClass('red lighten-1');
        }
    }
    $('select').material_select();
    $('.modal').modal();
});

