$(document).ready(function() {

    $(document).on('click', '.add', function (e){
        e.preventDefault();
        addSubForm(this);
        return false;
    });

    $(document).on('click', '.delete', function(e){
        e.preventDefault();
        deleteSubForm(this);
        return false;
    });

    function addSubForm(btn) {
        var prefix = $(btn).data("prefix");
        var settings = getFormSetSettings(prefix);
        var formSetCount = getFormSetCount(prefix);
        var parent = $(btn).closest('section[role="' + prefix + '"]');

        if (formSetCount < settings['max-num-forms'].val()){
            var block = $(parent).children('.block-wrapper:first').clone(false).get(0);

            // Insert it after the last form
            $(block).removeAttr('id').hide().insertAfter($(parent).children('.block-wrapper:last')).slideDown(300);

            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            //$(".errorlist", parent).remove();
            //$(parent).children().removeClass("error");

            // Remove old wrapper class and add new
            //$(block).removeClass('form-' + prefix + '-' + formFormSetCount).addClass('form-' + prefix + '-' + (formFormSetCount + 1));

            // Change delete button form id
            $(block).find(".delete").attr("data-form-id", (settings['counter'].val()));

            // Relabel or rename all the relevant bits
            $(block).children().children().each(function () {
                updateElementIndex(this, prefix, settings['counter'].val());
                $(this).val("");
            });

            // Add an event handler for the delete item/form link
            $(block).find(".delete").click(function () {
                return deleteSubForm(this, prefix);
            });

            // Update the total form count and counter
            settings['counter'].val(formSetCount + 1);
            settings['total-forms'].val(formSetCount + 1);
        } else {
            alert("Sorry, you can only enter a maximum of ten items.");
        }
    };

    function deleteSubForm(btn) {
        var prefix = $(btn).data("prefix");
        var settings = getFormSetSettings(prefix);
        var formSetCount = getFormSetCount(prefix);

        if (formSetCount > settings['min-num-forms'].val()) {
            // Delete the item/form
            $(btn).parents('.block-wrapper').remove();
            // Update the total number of forms
            settings['total-forms'].val(formSetCount - 1);
        } else {
            alert("You have to enter at least one todo item!");
        }
    };

    function getFormSetSettings(prefix) {
        return {
            'total-forms': $('#id_' + prefix + '-TOTAL_FORMS'),
            'initial-forms': $('#id_'+ prefix + '-INITIAL_FORMS'),
            'min-num-forms': $('#id_' + prefix + '-MIN_NUM_FORMS'),
            'max-num-forms': $('#id_' + prefix + '-MAX_NUM_FORMS'),
            'counter': $('input[name="' + prefix + '-counter"]')
        };
    };

    function getFormSetCount(prefix) {
        return $('section[role="' + prefix + '"] > .block-wrapper').length;
    }

    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+-)');
        var replacement = prefix + '-' + ndx + '-';

        if ($(el).attr("for")) {
            $(el).attr("for", $(el).attr("for").replace(id_regex,
        replacement));
        }

        if (el.id) {
            el.id = el.id.replace(id_regex, replacement);
        }

        if (el.name) {
            el.name = el.name.replace(id_regex, replacement);
        }
    }
});