/*
   Script: TextboxList.Autocomplete.Binary.js
   TextboxList Autocomplete binary search extension

   Authors:
   Guillermo Rauch

   Note:
   TextboxList is not priceless for commercial use. See <http://devthought.com/projects/jquery/textboxlist/>
   Purchase to remove this message.
   */

var searcher =  {
    matcher: function (item, query) {
        return ~item.toLowerCase().indexOf(query.toLowerCase());
    }
    , sorter: function (items, query) {
        var beginswith = []
            , caseSensitive = []
            , caseInsensitive = []
            , item;

            while (item = items.shift()) {
                if (!item[1].toLowerCase().indexOf(query.toLowerCase())) beginswith.push(item);
                else if (~item[1].indexOf(query)) caseSensitive.push(item);
                else caseInsensitive.push(item);
            }

        return beginswith.concat(caseSensitive, caseInsensitive);
    }
    
    , highlight: function(html, query, hit_class){
        var regex = new RegExp('(<[^>]*>)|(\\b'+ query.replace(/([-.*+?^${}()|[\]\/\\])/g,"\\$1") +')', 'ig');
        return html.replace(regex, function(a, b, c, d){
            return (a.charAt(0) == '<') ? a : '<strong class="'+ hit_class +'">' + c + '</strong>'; 
        });
    }
};

$.TextboxList.Autocomplete.Methods.custom = {
    filter: function(items, query, insensitive, max, post_result){
        items = $.grep(items, function (item) {
            return searcher.matcher(item[1], query);
        })

        items = searcher.sorter(items, query);

        if(post_result){
            items = post_result(items, max);
        }

        return items.slice(0, max);
    }
    , highlight: function(element, query, insensitive, hit_class){
        return element.html(searcher.highlight(element.html(), query, hit_class));
    }
};
