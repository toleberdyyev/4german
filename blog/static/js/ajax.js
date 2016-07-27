
$(document).ready(function(){
  $('#comment').submit(function(){
    var post_id= $('.post').attr('id');
    var username = $('#username_author').html()
    var author=$('#id_author').val(username)
    var text = $('#id_text').val()
    var content = $('#comments_wall').html()
    var data_l = `
    <div class="comments_row">
    <p><b><a>${ username }</a> </b> right now  </p>
    <p class='pots_text'>${text}</p>
  </div>
    `
    console.log('0k01')
    var str=$(this).serialize()
    if (text != ''){
    $.ajax({
      type:'POST',
      data:str,
      success:function(html){
      console.log(html)
       $('#comments_wall').html(html)
       $('#id_author').val('')
       $('#id_text').val('')
       grecaptcha.reset();
      }
})}else{
  console.log('empty')
  grecaptcha.reset();
}
    return false;

  })

$('#re_cancel_btn').click(function(){

  $('.comment_form').slideDown()
  $('.reply_form').slideUp()
  $('label[for="id_reply_text"]').html('')

})

$("#id_reply_text").keydown(function(){
      var t_len = $('#id_reply_text').val()
      if(t_len.length > 0){
        $('#re_comment_btn').slideDown()
      }else{
          $('#re_comment_btn').slideUp()
      }
   });

})

function reply_comment(o,username,author){
  var Comment_id = o.id;
  $('.comment_form').slideUp()
  $('.reply_form').slideDown()
  $('label[for="id_reply_text"]').html(username+" replied to  "+author)
}
