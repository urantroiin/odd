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

function tag_format(data){
    var tags = []
    $.each(data.tags,function(i,t){
        tags.push([t.tag, t.tag, null, '<img src="/static/'+t.photo+'" />'+t.tag]);
    });
    return tags;
}

function textbox(_options) {
    var options = $.extend({
        element: '',
        url: '',
        format: function(data){return data;},
        placeholder: '',
        init_values: [],
        empty_submit: false,
        on_empty: null,
        on_bitBoxAdd: null,
        focus: false,
        on_selected: null,
        on_new: null,
    }, _options);

    var t = new $.TextboxList(options.element, {unique: true, plugins: {
        autocomplete: {method:'custom', placeholder:options.placeholder, on_selected:options.on_selected, on_new:options.on_new}}});

    $.each(options.init_values, function(i,v){
        t.add(v[0], v[1]);
    });
   
    if(options.empty_submit){
        t.addEvent('empty', function(){
            $(options.element).parent('.edit-form').ajaxSubmit({
                success: success
            });
        });
    }

    if(options.on_empty){
        t.addEvent('empty', options.on_empty);
    }
    
    if(options.on_bitBoxAdd){
        t.addEvent('bitBoxAdd', options.on_bitBoxAdd);
    }

    if(options.focus){
        $('input',t.getContainer()).focus();
    }

    t.getContainer().addClass('textboxlist-loading');  
    $.getJSON(options.url, function(data){
        t.plugins['autocomplete'].setValues(options.format(data));
        t.getContainer().removeClass('textboxlist-loading');
    }); 

    return t;
}

/*
 * editable
 * */
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
