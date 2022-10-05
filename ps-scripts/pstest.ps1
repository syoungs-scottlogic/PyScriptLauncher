$newItems = New-Object System.Collections.ArrayList
$hashTable = @{}

$runCheck = aws ec2 describe-instances --profile sl --query 'Reservations[*].Instances[*].[InstanceId, Tags[?Key==`Name`].Value | [0]]' --output text

$runCheck | foreach{$newItems = $_.split(); $hashTable.Add("$($newItems[0])", "$($newItems[1])") }

return $hashTable
#return aws describe-instance-status --profile sl