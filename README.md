# Search

Search.py searches through the raw binary or raw data for the given text or hex and print the memory address at which data is stored.

Since, the raw_dump could be large in size nearly in GB,

So I, have read the data in chunks of (2**24)bytes so as to avoid Memory error.

Exceptions, I took

The code does not handle if the half of data(that we want to search) is overlap in first chunk and other half in other chunk.

Incase, You want to optimize or improve the Code. Please feel free to fork and make the changes.
