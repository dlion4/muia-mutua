$(document).ready(function(){
"use strict"

/*slideshow script code start here*/
$('.slideshow').owlCarousel({
	loop: false,
	margin: 0,
	autoplay: true,
	smartSpeed: 1500,
	dots: true,
	nav:true,
	navText:['<i class="icofont icofont-bubble-left fa1"></i>', '<i class="icofont icofont-bubble-right fa2"></i>'],
	responsiveClass: true,
	responsive: {
		0: {
			items: 1
		},
		991: {
			items: 1
		},
		1180: {
			items: 1
		}
	}
});
/*slideshow script code end here*/

/*courses script code start here*/

$('.courses').owlCarousel({
	loop: false,
	margin: 30,
	items: 4,
	autoplay: true,
	smartSpeed: 2500,
	dots: true,
	nav:true,
	navText:['<i class="icofont icofont-bubble-left fa1"></i>', '<i class="icofont icofont-bubble-right fa2"></i>'],
	responsiveClass: true,
	responsive: {
		0: {
			items: 1
		},
		768: {
			items: 2
		},
		991: {
			items: 3
		},
		1180: {
			items: 4
		}
	}
});
/*courses script code end here*/

/*bloggs script code start here*/
$('.bloggs').owlCarousel({
	loop: false,
	margin: 0,
	autoplay: true,
	smartSpeed: 1500,
	dots: true,
	nav:true,
	navText:['<i class="icofont icofont-bubble-left fa1"></i> Prev', 'Next <i class="icofont icofont-bubble-right fa2"></i>'],
	responsiveClass: true,
	responsive: {
		0: {
			items: 1
		},
		991: {
			items: 1
		},
		1180: {
			items: 1
		}
	}
});
/*bloggs script code end here*/
	
});