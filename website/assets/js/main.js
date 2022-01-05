
$('select').on('change', function() {
    var obj = { 'grid-size': $( "#grid-size option:selected" ).val(), 'words-number': $( "#words-number option:selected" ).val() };
    var newurl = 'https://4is90gmk99.execute-api.eu-west-1.amazonaws.com/production/generate-file?' + $.param(obj);
    $('#add-parameters').attr("href", newurl);
});
