function signInCallback(authResult) {
	if (authResult["code"]) {
		$("#loginForm").css("display", "none");

		$.ajax({
			type: "POST",
			url: "/gconnect?state={{ STATE }}",
			contentType: "application/octet-stream; charset=utf-8",
			data: authResult["code"],
			success: function (data) {
				if (data) {
					$("#result").html("<div style="margin: 40px auto; width: 600px; text-align: center">" + "Login successful!</br>" + data + "</br>redirecting</div>");
					setTimeout(function () {
						window.location.href = "/catalog";
					}, 3000);
				} else if (authResult["error"]) {
					console.log("There was an error: ", authResult["error"]);
				} else {
					$("#result").text("Failed to make a server side call. Check your configuration and console")
				}
			}
		})
	}
}