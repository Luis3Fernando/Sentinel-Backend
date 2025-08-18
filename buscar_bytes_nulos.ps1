Get-ChildItem -Recurse -Filter *.py | ForEach-Object {
    $bytes = [System.IO.File]::ReadAllBytes($_.FullName)
    if ($bytes -contains 0) {
        Write-Output "Archivo corrupto: $($_.FullName)"
    }
}
