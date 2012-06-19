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

function tip_format(data){
    var tips = []

    $.each(data.tags,function(i,tag){
        tips.push(['/tag/'+tag.tag, tag.tag, 'tag', '<img src="/static/'+tag.photo+'" />'+tag.tag]);  
    });

    $.each(data.questions,function(i,que){
        tips.push(['/question/'+que.id, que.title, 'question', '<img src="/static/img/question.png" />'+que.title]);
    });

    $.each(data.resources,function(i,res){
        tips.push(['/resource/'+res.id, res.title, 'resource', '<img src="/static/img/resource.png" />'+res.title]);  
    });

    return tips;
}

function classify(items, max){
    var tags = []
        , questions = []
        , resources = [];

    $.each(items, function(k, v){
        switch(v[2]){
        case 'tag':
            tags.push(v);
            break;
        case 'question':
            questions.push(v);
            break;
        case 'resource':
            resources.push(v);
            break;
        }
    });

    tags = tags.slice(0, max/3);
    questions = questions.slice(0, max/3);
    resources = resources.slice(0, max/3);
    
    return tags.concat(questions, resources);
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
        post_result: null,
    }, _options);

    var t = new $.TextboxList(options.element, {unique: true, plugins: {
        autocomplete: {method:'custom', placeholder:options.placeholder, on_selected:options.on_selected, on_new:options.on_new, post_result:options.post_result}}});

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

    t.getContainer().addClass('textboxlist-loading');  
    $.getJSON(options.url, function(data){
        t.plugins['autocomplete'].setValues(options.format(data));
        t.getContainer().removeClass('textboxlist-loading');
        if(options.focus){
            $('input',t.getContainer()).focus();
        }
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
