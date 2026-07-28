# AXIS Compiler Grammar

The AXIS DSL grammar defines how architectural instructions are parsed.

## Tokens
- IDENTIFIER
- NUMBER
- VECTOR3
- KEYWORD_MOV
- KEYWORD_PUSH
- KEYWORD_SIGNAL
- KEYWORD_COMPUTE

## Grammar Rules

program      → statement*
statement    → mov_stmt | push_stmt | signal_stmt | compute_stmt

mov_stmt     → "MOV" VECTOR3
push_stmt    → "PUSH" NUMBER
signal_stmt  → "SIGNAL" IDENTIFIER
compute_stmt → "COMPUTE" IDENTIFIER

