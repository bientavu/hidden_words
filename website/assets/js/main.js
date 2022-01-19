
$('select').on('change', function() {
    var obj = { 'grid-size': $( "#grid-size option:selected" ).val(), 'words-number': $( "#words-number option:selected" ).val() };
    var newurl = 'https://4is90gmk99.execute-api.eu-west-1.amazonaws.com/production/generate-file?' + $.param(obj);
    $('#add-parameters').attr("href", newurl);
});

$(function download() {
    $('button').on('click', function () {
        var newDiv = $(
            '<div class="load-wrapp">\n' +
            '    <div class="load-7">\n' +
            '        <p style="margin-bottom: 0; color: white">Chargement...</p>\n' +
            '        <div class="square-holder">\n' +
            '            <div class="square"></div>\n' +
            '        </div>\n' +
            '    </div>\n' +
            '</div>'
        );
       $(".square-holder").append(newDiv);
       setTimeout(function (){
           newDiv.remove();
       }, 6500);

        theURL = $(this).attr('href');
        $.ajax({
            type: 'GET',
            url: theURL,
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
