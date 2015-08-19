$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};

    $("#messageform").on("submit", function() {
	newMessage($(this));
	return false;
    });
    $("#messageform").on("keydown", function(e) {
        console.log(e.keyCode);
	if (e.keyCode == 13 && e.ctrlKey) {
            var val = $("#message").val();
            $("#message").val(val + '\n');
	}
        else if (e.keyCode == 13) {
	    newMessage($(this));
	    return false;
	}
    });
    $("#message").select();
    updater.poll();
});

function newMessage(form) {
    var message = form.formToDict();
    var submit_btn = form.find("input[type=submit]");
    submit_btn.prop('disabled', true)
    $.post(url_new_message, message, function(response) {
	updater.showMessage(response);
	if (message.id) {
	    form.parent().remove();
	} else {
	    form.find("input[type=text]").val("").select();
            submit_btn.prop('disabled', false)
	}
        $("#message").val('');
    })
    .fail(function(response) {
        window.location.replace(url_failed_authorization); //'/chats3');
    });
}

jQuery.fn.formToDict = function() {
    var fields = this.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
	json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

var updater = {
    errorSleepTime: 100,
    cursor: null,

    poll: function() {
	var args = {};
	if (updater.cursor) args.cursor = updater.cursor;
	$.post(url_update_messages,
                $.param(args), updater.onSuccess
                ).fail(updater.onError);
    },

    onSuccess: function(response) {
	try {
	    updater.newMessages(response);
	} catch (e) {
	    updater.onError();
	    return;
	}
	updater.errorSleepTime = 100;
	window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
	updater.errorSleepTime *= 2;
	console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
	window.setTimeout(updater.poll, updater.errorSleepTime);
    },

    newMessages: function(response) {
	if (!response.messages) return;
	updater.cursor = response.cursor;
	var messages = response.messages;
	updater.cursor = messages[messages.length - 1].id;
	console.log(messages.length, "new messages, cursor:", updater.cursor);
	for (var i = 0; i < messages.length; i++) {
	    updater.showMessage(messages[i]);
	}
    },

    showMessage: function(message) {
	var existing = $("#m" + message.id);
	if (existing.length > 0) return;
	var node = $(message.me_html);
	node.hide();
	$("#inbox").append(node);
	node.slideDown();
    }
};
