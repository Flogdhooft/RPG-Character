# Python RPG Character Generator

A **Python script** built from a [freeCodeCamp](https://www.freecodecamp.org/) practice project to reinforce core Python concepts and algorithm design. This project was self-designed to master strict input validation, guard clauses, conditional logic, and custom visual stat rendering. RPG Character Generator allows users to create character profiles while enforcing strict point allocation and naming rules.

## Key Features

* **Strict Input Validation :**
  * Ensures character names are non-empty strings, up to 10 characters, and without spaces.
  * Catches invalid data types for stats using `isinstance()` checks.
  * Enforces stat boundaries (each stat must be between `1` and `4`).
* **Point Budget System :** Enforces strict point-budget distribution (starting total must equal exactly `7` points).
* **Visual Stat Bar Rendering :** Formats output using custom progress dots (`●` and `○`) scaled over a 10-point visual meter.
* **Guard Clause Pattern :** Clean, early-return architecture for clear error reporting and readable control flow.

## Concepts & Technologies Applied

* **Python 3**
* **Type & Value Checking :** Validation with `isinstance()`, string method `.count()`, and comparison operators.
* **String Manipulation & Formatting :** Dynamic ASCII-style bar generation using string multiplication and f-strings.
* **Guard Clauses & Defensive Programming :** Handling invalid states early to keep core logic clean.

---

## Usage Example

```text
# Function Call
print(create_character('ren', 4, 2, 1))

# Console Output
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## Code Structure Example

Excerpt from the script handling validation checks and visual stat bar formatting in `create_character()`:

```python
def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    if len(character_name) <= 0:
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if character_name.count(' '):
        return 'The character name should not contain spaces'
```
