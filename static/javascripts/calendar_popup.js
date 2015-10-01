function toggle_on(div_id)
{
	var el = document.getElementById(div_id);
	el.style.display = 'block';
}

function toggle_off(div_id)
{
	var el = document.getElementById(div_id);
    el.style.display = 'none';
}

function popup(windowname)
{
    var el1 = document.getElementById(windowname);
    var el2 = document.getElementById('blanket');
    
    var isShown = (el1.style.display == 'block');
    
    if( isShown )
    {
        toggle_off('blanket');
        toggle_off(windowname);
    }
    else
    {
        // Open calendar in new window if the window size is not big enough
        if( window.innerWidth < 1000 || window.innerHeight < 500 )
        {
            var googleCalendar = "https://www.google.com/calendar/embed?src=socalnspweb%40gmail.com&ctz=America/Los_Angeles";
            window.location.href = googleCalendar;
            return;
        }
        
        toggle_on('blanket');
        toggle_on(windowname);
    }
}

window.onload = function()
{
    document.getElementById('blanket').onclick = function(e)
    {
        // Should only be called when 'blanket' is shown
        if(e.target != document.getElementById('content-area'))
        {
            popup('popUpDiv');          
        }
    }
};