# JSON_FORMAT for Server Client Interactions

Version 1
>{
>    'status':'status',
>    'ID':id,
>    'payload':'payload'
>}

## Status:
 Status defines the current status between the server and client.
 
 configure: To be used when the server and client need to exhange keys, will also establish a mailbox for the client on the server if one hadn't existed prior. Configure may also be sent if server recieves a communication that it cannot decrypt. Example: Server goes down, client remains up. Client messages server an encrypted message, server responds with status configure.

good: Encryptions are secure, no action needs to be taken

repeat: Previous message needs to be repeated

## ID:
 A client ID which is given by the client when communicating with the server
 Server responses may not include ID
 
## Payload:
 Anything, we do not care.

