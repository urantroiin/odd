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
        return ~item.toLowerCase().indexOf(query.toLowerCase())
    }

    , sorter: function (items, query) {
        var beginswith = []
            , caseSensitive = []
            , caseInsensitive = []
            , item

            while (item = items.shift()) {
                if (!item[1].toLowerCase().indexOf(query.toLowerCase())) beginswith.push(item)
                else if (~item[1].indexOf(query)) caseSensitive.push(item)
                else caseInsensitive.push(item)
            }

        return beginswith.concat(caseSensitive, caseInsensitive)
    }
}

$.TextboxList.Autocomplete.Methods.custom = {
    filter: function(items, query, insensitive, max){
        items = $.grep(items, function (item) {
            return searcher.matcher(item[1], query)
        })

        items = searcher.sorter(items, query)

        return items.slice(0, max);
    }
    , highlight: function(element, query, insensitive, klass){
        var regex = new RegExp('(<[^>]*>)|(\\b'+ query.replace(/([-.*+?^${}()|[\]\/\\])/g,"\\$1") +')', insensitive ? 'ig' : 'g');
        return element.html(element.html().replace(regex, function(a, b, c, d){
            return (a.charAt(0) == '<') ? a : '<strong class="'+ klass +'">' + c + '</strong>'; 
        }));
    }
};
