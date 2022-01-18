
$('select').on('change', function() {
    var obj = { 'grid-size': $( "#grid-size option:selected" ).val(), 'words-number': $( "#words-number option:selected" ).val() };
    var newurl = 'https://4is90gmk99.execute-api.eu-west-1.amazonaws.com/production/generate-file?' + $.param(obj);
    $('#add-parameters').attr("href", newurl);
});

$(function () {
    $('button').on('click', function () {
        theURL = $(this).attr('href');
        $.ajax({
            type: 'GET',
            url: theURL,
            async: false,
            beforeSend: (xhr) => {
              if (xhr && xhr.overrideMimeType) {
                xhr.overrideMimeType('application/json;charset=utf-8');
              }
            },
            dataType: 'json',
            success: (data) => {
                var json = JSON.parse(data);
                window.open(json.body, "_blank");
            }
        });
    });
})
