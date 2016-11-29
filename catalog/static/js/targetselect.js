(function( $ ) {
    $.fn.targetSelect = function() {
        this.each(function () {
            var select = $(this);
            select.css({"display":"none"});
            console.log(select);
            var options = select.children("option");
            console.log(options);
            $parent = select.parent();

            $parent.on("click",'.continue', function () {
                console.log(select);
                select.val($(this).attr("value"));
                if($(this).attr("next")=="submit"){
                    $(this).parents("form").submit();
                }
            });

            var el_next = select.attr("next");
            $.each(options, function (index, value) {
                var el_value = $(value).attr("value");
                var el_text = $(value).text();
                var new_el = '<div class="target-block"><div class="target-text">'+el_text+'</div><div class="continue next-w" next="'+el_next+'" value="'+el_value+'"></div></div>';
                $parent.append(new_el);
            });
        })
    };
})(jQuery);