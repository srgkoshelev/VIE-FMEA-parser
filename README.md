# README #

### Small utility to match instrument numbers from T&I VIE list with numbers from appropriate P&ID


#### Regex to parse instrumentation names, e.g. PT/PI/PS-3113-(A) ###

The inferred convention for the IB-1 names is:

- Prefix no longer than two groups of additional letter name plus slash sign e.g. YCV/YIC/
    - Prefixes are a capturing group in regex
    - Prefix names are limited to 4 characters
    - Prefixes (either one ore several) are returned as a tuple
- Base name - 4 letter name of the instrument
    - Base name is capturing group in regex
- Basic separator - most used are - and space " ", although some more exotic will fit as well, e.g. underscore, slash, EOL. No separator case is also included
- Instrumentation number - up to 4 digits; capturing group in regex
- Suffix separator - similar to basic separator case except for EOL and space.
    - Also works with suffix with brackets, e.g. 1758(A) but won't work with separator + bracket, e.g. 1758-(A)
- Suffix is handled similar to prefixes
    - Allowable suffixes include up to 3 groups of 3 letters/digits (ABC, Alt) with **/** or **-** as separator, e.g. A/2X-Alt