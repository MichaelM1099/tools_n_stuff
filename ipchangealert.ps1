# define the URL of the ip checking service
$ipifyUrl = "https://api.ipify.org"
$ipFilePath = ".\ip.txt"
$smtpServer = "smtp.office365.com(orwhateveryoursmtpserveris)"
$smtpPort = 587
$smtpUsername = "logs@emaildomain.com"
$smtpPassword = "passwordinquotes"
$fromEmail = "logs@emaildomain.com"
$toEmail = "recipientemailaddress"

# sendemail
function Send-Email {
    param (
        [string]$subject,
        [string]$body
    )

    $smtp = New-Object Net.Mail.SmtpClient($smtpServer, $smtpPort)
    $smtp.EnableSsl = $true
    $smtp.Credentials = New-Object System.Net.NetworkCredential($smtpUsername, $smtpPassword)

    $message = New-Object Net.Mail.MailMessage($fromEmail, $toEmail)
    $message.Subject = $subject
    $message.Body = $body

    $smtp.Send($message)
}

# check if ip.txt exists in the same folder as script and read the stored IP
if (Test-Path $ipFilePath) {
    $storedIP = Get-Content $ipFilePath
} else {
    $storedIP = $null
}

# request publicIP from ipwebsite
$publicIP = Invoke-RestMethod -Uri $ipifyUrl

# print the public IP
Write-Host "Your public IP address is: $publicIP"

# save the current IP to ip.txt
$publicIP | Set-Content $ipFilePath

# compare with stored IP and send email if they don't match
if ($storedIP -ne $null -and $publicIP -ne $storedIP) {
    $subject = "Public IP Address Change"
    $body = "Your public IP address has changed from $storedIP to $publicIP."
    Send-Email -subject $subject -body $body
}
