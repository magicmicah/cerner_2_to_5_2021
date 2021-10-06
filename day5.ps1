# Invoke-Command loop in Powershell
# cerner_2tothe5th_2021
# Sometimes you have to resort to powershell cause you're iterating through a list of servers. In the ScriptBlock, do anything you want. Add your own hosts to the $servers variable. GLHF.


$servers = @('list', 'of', 'servers')

foreach ($server in $servers)
{
    Invoke-Command -ComputerName $server -ScriptBlock {Write-Output "do stuff"}
}