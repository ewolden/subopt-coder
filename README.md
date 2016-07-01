# subopt-coder
A simple DHCP sub-option encoder/decoder

The script takes as input one of these arguments:
- A HEX string of the DHCP sub-options 
  - For example: subopt-coder.py 0113687474703a2f2f736f6d652e75726c2e636f6d0215736f6d652d6d6f72652d696e666f726d6174696f6e
- A list of DHCP options and their values
  - For example: subopt-coder.py 01 http://some.url.com 02 some-more-information

All the options entered will then be printed as both HEX and ASCII values. 
