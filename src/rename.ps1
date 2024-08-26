param (
    [string] $path
)

$files = Get-ChildItem -Path $path -Recurse -Filter *.lua

$counter = 0

$files | ForEach-Object {
    $newName = $_.FullName -replace "\.lua$", ".luau"
    Rename-Item -Path $_.FullName -NewName $newName

    $counter++
}

Write-Output "Changed $counter .lua scripts to .luau"