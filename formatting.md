Every function must have this header:
##
 # Description of the functions purpose.
 # The file path to the function.
##

Every block of code must have a description of what it does.

Long execute commands must be nested like this:
execute as @a[tag=dummy] run \
    Logic 1
    Logic 2
    Logic 3

Name formatting goes:
Tags = SCREAMING_SNAKE_CASE
Teams = SCREAMING_SNAKE_CASE
Scoreboards = namespace. + camelCase
Static score = # + kebab-case
Dynamic score = $ + kebab-case
Timing score = % + kebab-case

GOOD and BAD file management:

GOOD
datapackauthor/
└── function/
    └── namespace/
        ├── init/
        │   ├── scoreboards/
        │   │    └── create.mcfunction
        │   └── init.mcfunction
        ├── main.mcfunction
        └── reset.mcfunction

BAD
namespace/
└── function/
    ├── create.mcfunction
    ├── init.mcfunction
    ├── main.mcfunction
    └── reset.mcfunction


# By Mythorical
