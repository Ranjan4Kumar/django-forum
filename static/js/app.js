//////////////////////
// javascrip for Apps page
//////////////////////////
$(function(){

    // Executed when js-menu-icon js menu is clicked
    $(' .js-menu-icon').click(function(){

        // $(this) : self element  namely div.js-menu-icon
        // next() : next to div.js-menu-icon, namely div.menu
        // toggle() : Switch show or hide
        
        
        $(this).next().toggle();
        

    })
})