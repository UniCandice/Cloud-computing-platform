function initial()
{
	var mainmenu = document.getElementById("mainmenu");
	var lis = mainmenu.getElementsByTagName("li");
	for (var i=0; i<lis.length; i++)
	{
		lis[i].onmouseover = function ()
		{
			var uls = this.getElementsByTagName("ul");
			if (uls.length > 0)
			{
				uls[0].className = "show";
			}
		}

		lis[i].onmouseout = function ()
		{
			var uls = this.getElementsByTagName("ul");
			if (uls.length > 0)
			{
				uls[0].className = "hide";
			}
		}
	}
}

if (window.attachEvent)
    window.attachEvent("onload", initial);

