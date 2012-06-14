function trim(str){
    return str.replace(/(^\s*)|(\s*$)/g, "");
}

function fail(request){
    alert('您的操作没有成功')
}

function success(data){
    if(data.errno=='FAIL'){
        alert('您的操作没有成功')
        return
    }
    window.location.reload(true)
}

function tagbox(input_id, tags) {
    if(t) return;
        
    t = new $.TextboxList(input_id, {unique: true, plugins: {autocomplete: {placeholder:'搜索:标签'}}});

    $.each(tags, function(i,tag){
        t.add(tag,tag);
    });
   
    t.addEvent('empty', function(bitBox){
        $(input_id).parent('form').ajaxSubmit({
            success: success
        });
    });

    $('input',t.getContainer()).focus();

    t.getContainer().addClass('textboxlist-loading');  
    $.getJSON("{{ url_for('tag.obj') }}", function(data){
        var tags = new Array()
        $.each(data.tags,function(i,t){
            tags.push(new Array(t.tag, t.tag, null, '<img src="/static/'+t.photo+'" />'+t.tag));
        });

        t.plugins['autocomplete'].setValues(tags);
        t.getContainer().removeClass('textboxlist-loading');
    }); 
}

$(function(){
    $('.editable').hover(function(){
        $('.edit', this).fadeIn('fast');
    },function(){
        $('.edit', this).fadeOut('fast');
    });

    $('.editable .edit').click(function(){
        var edited = $(this).parents('.edited');
        var edit_form = edited.siblings('.edit-form')
        var edited_item = $(this).siblings('.edited-item');
        var edit_item = edit_form.find('.edit-item');
        var edit_cancel = edit_form.find('.edit-cancel');

        edited.hide('fast');
        edit_form.show('fast');
        edit_item.val(edited_item.text())
        edit_cancel.click(function(){
            edit_form.hide('fast');
            edited.show('fast');
        })
    });

    $('.edit-form').ajaxForm({
        complete: success
    });

    $('.ajax-form').ajaxForm({
        'complete': success
    });
});
