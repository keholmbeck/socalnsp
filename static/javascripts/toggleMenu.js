
function toggleMenu( me )
{
    menuIconDiv = me.parentElement;
    menubarDiv  = menuIconDiv.parentElement;
    sidebarDiv  = menubarDiv.parentElement;
    parentDiv   = sidebarDiv;
    
    // Main section: do not display when menu is toggled. //
    mainSection = document.getElementsByTagName('section')[0];
    
    if( mainSection.style.display == "none" )
    {
        parentDiv.style.height     = "90px";
        document.body.style.overflow = "auto";
        mainSection.style.display    = "block";
    }
    else
    {
        parentDiv.style.height       = "100%";
        /*document.body.style.overflow = "hidden";*/
        mainSection.style.display    = "none";
    }
}