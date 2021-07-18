function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function removeNotification(url, notificationId) {
    console.log(notificationId)
	const csrftoken = getCookie('csrftoken');
	let xmlhttp = new XMLHttpRequest();

	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == XMLHttpRequest.DONE) {
			if (xmlhttp.status == 200) {
				const currentCounter = parseInt(document.getElementById("dropdownMenuButton").innerText.replace(" ", ""))
				const newCounter = currentCounter - 1
				document.getElementById("dropdownMenuButton").innerText = newCounter
				document.getElementById(notificationId).remove();
			} else {
				alert('There was an error');
			}
		}
	};
    console.log(url)
    xmlhttp.open("DELETE", url, true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xmlhttp.send();
}

console.log('tester')
