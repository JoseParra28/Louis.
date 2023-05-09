$(document).on('click', '#add-button', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '{% url "cart-add" %}',
        data: {
            product_id: $('#add-buttton').val(),
            product_quantity: $('#select option:selected').text(),
            csrfmiddlewaretoken: "{{ csrf_token }}",
            action: 'post'
        },
        success: function(json){
            console.log(json)

        },
        error : function (xhr, errmsg, err){

        },
    });
})
console.log("this is working")