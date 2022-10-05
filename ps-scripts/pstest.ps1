#Set-ExecutionPolicy RemoteSigned
$newItems = New-Object System.Collections.ArrayList
$hashTable = @{}

Write-Host "trying check"
$runCheck = aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, Tags[?Key==`Name`].Value | [0]]' --output text --profile sl

$runCheck | foreach{$newItems = $_.split(); $hashTable.Add("$($newItems[0])", "$($newItems[1])") }

# Put results into file to import into python.
$json = $hashTable | ConvertTo-Json
$json | Out-File ".\data\InstanceResults.json"

#return aws describe-instance-status --profile sl