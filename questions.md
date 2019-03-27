// side notes
// DWORD = size?
// WORD = type?
// BYTE = RGB? colors?
// LONG = width/height?
# Questions

## What's `stdint.h`?

BMP-related data types based on Microsoft's own

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

To declare if x-bits is unsigned or signed integer.
A UINT8 is an 8-bit unsigned integer (range: 0 through 255 decimal). Because a UINT8 is unsigned, its first bit (Most Significant Bit (MSB)) is not reserved for signing.
Similarly for uint32 and uint16.

INT32 is a 32-bit signed integer (range: –2147483648 through 2147483647 decimal). The first bit (Most Significant Bit (MSB)) is the signing bit.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE - 1
DWORD - 4
LONG - 4
WORD - 2

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

TODO

## What's the difference between `bfSize` and `biSize`?

bfSize is the size of the bitmap file, while biSize is the number of bytes required by the structure.

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

When file doesn't exist (for read using r); or any unsuccesfull fopen?

## Why is the third argument to `fread` always `1` in our code?

because we check in blocks only 1 pixel by one (for loop)

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

TODO

## What does `fseek` do?

fseek - sets file position 

## What is `SEEK_CUR`?

If you want to change the location of the pointer fp from its current location, set from_where to SEEK_CUR. 
