# Generate a new GUID (UUID)
$guid = [System.Guid]::NewGuid()

# Convert the GUID to a byte array
$guidBytes = $guid.ToByteArray()

# Encode the byte array to a Base64 string
$base64EncodedGuid = [System.Convert]::ToBase64String($guidBytes)

# Display the Base64 encoded GUID
Write-Host "Generated GUID: $guid"
Write-Host "Base64 Encoded GUID: $base64EncodedGuid"