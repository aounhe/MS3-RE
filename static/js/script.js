/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $('select').formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});
