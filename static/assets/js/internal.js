$(document).ready(function(){
    "use strict"

	// Product Grid
	$('#grid-view').on('click',function(e){
		e.preventDefault();
		$('.mainpage .row .product-list').attr('class', 'product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12');
		localStorage.setItem('display', 'grid');
	});
	$('#list-view').on('click',function(e){
		e.preventDefault();
		$('.mainpage .row .product-grid').attr('class', 'product-layout product-list col-xs-12');
		localStorage.setItem('display', 'list');
	});
	
	// collapse
	$('.faq .collapse').on('shown.bs.collapse', function(){
	$(this).parent().removeClass('active').addClass('active');
	$(this).parent().find(".hidelink").remove("SHOW ANSWER").text("HIDE ANSWER");
	}).on('hidden.bs.collapse', function(){
	$(this).parent().find(".hidelink").remove("HIDE ANSWER").text("SHOW ANSWER");
	$(this).parent().removeClass("active").addClass("");
	});
	
	// collapse
	$('.feature .collapse').on('shown.bs.collapse', function(){
	$(this).parent().removeClass("active").addClass("active");
	$(this).parent().find(".fa-plus").removeClass("fa-plus").addClass("fa-minus");
	}).on('hidden.bs.collapse', function(){
	$(this).parent().find(".fa-minus").removeClass("fa-minus").addClass("fa-plus");
	$(this).parent().removeClass("active").addClass("");
	});
	
	
	
	//review
	$(".inreview").on("click", function(){
    	$('.outreview').hide();
	
		$(".nav-tabs .active").on("click", function(){
			$('.outreview').show();
		});
	});
	
	
});