# JSON_FORMAT for Server Client Interactions

Version 2
>{
>    'status':'status',
>    'opperation':'opperation',
>    'ID':id,
>    'payload':'payload'
>}

## Status:
 Status defines the current status between the server and client.

good: good request, further information to read
done: good request, no further information
bad: bad request, redo

repeat: Previous message needs to be repeated, not implemented

## ID:
 A client ID which is given by the client when communicating with the server
 Server responses may not include ID
 
## Payload:
 Anything, we do not care.

