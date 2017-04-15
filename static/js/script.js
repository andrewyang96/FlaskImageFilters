$(document).ready(function () {
    $('form input[type=range]').change(function (event) {
        var displayId = '#' + event.target.name + '_display';
        $(displayId).text(event.target.value);
    });
});
