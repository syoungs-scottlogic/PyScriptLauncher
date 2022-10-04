$runCheck = aws ec2 describe-instances --filters "Name=tag:owner,Values=syoungs" --profile sl
$data = $runCheck | ConvertFrom-Json
$instances = @()

Write-Host ($instances)

#return aws describe-instance-status --profile sl