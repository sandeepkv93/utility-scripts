title = document.getElementById("course-title").children[0].innerHTML;
modules = document.getElementsByClassName("modules");
res = "Course Title: "+title+"\n";
n = 1;
m = 1;
for(i = 0; i< modules[0].children.length; i++)
{
    res += "["+m+"] "+modules[0].children[i].children[0].children[0].innerHTML+"\n";    
    for(j=0; j < modules[0].children[i].children[1].children.length; j++) 
    {
        res += n+". "+(modules[0].children[i].children[1].children[j].children[1].innerHTML)+"\n";
        n++;
    }
    m++;
    res +="\n";
}
