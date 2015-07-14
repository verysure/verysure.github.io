$(window).scroll(function() {
    
    var position = $(document).scrollTop()
    if (position < $("#intro").offset().top ) {
        $(".navbar").addClass('hide-bar');
    } 
    
    else {
        $(".navbar").removeClass('hide-bar');
    }
});



        // $('.navbar-default .navbar-brand').removeClass('hidden-element');
        
        // if (position+30 < $('#about').offset().top) {
        //     // $('#logo-text').text( $('#name').text());
        //     $('#logo-text').addClass('hidden-element');
        // }
        
        // else if (position+30 < $('#research').offset().top) {
        //     $('#logo-text').text( $('#about').text() );
        //     $('#logo-text').removeClass('hidden-element');
        // }
        
        // else if (position+30 < $('#interest').offset().top) {
        //     $('#logo-text').text( $('#research').text() );
        //     $('#logo-text').removeClass('hidden-element');
        // }
        // else {
        //     $('#logo-text').text( $('#interest').text() );
        //     $('#logo-text').removeClass('hidden-element');
        // }
        
        
        
        // $('.navbar-default').css('background-color', '#000000');