$(document).on('click', '#add-button', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "cart-add" %}',
        data: {
            product_id: $('#add-button').val(),
            product_quantity: $('#select option:selected').text(), 
            csrfmiddlewaretoken: "{{csrf_token}}",
            action: 'POST'
        },
        success: function(json){
            console.log(json)
           
       
        },
        error: function(xhr, errmsg, err){
        }
        
    });
})
console.log("This is base js")