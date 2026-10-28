# Python RPG Character Generator

A **Python script** built from a *[freeCodeCamp](https://www.freecodecamp.org/learn/python-v9/lab-rpg-character/build-an-rpg-character)* practice project to reinforce core Python concepts and algorithm design. This project was self-designed to master strict input validation, guard clauses, conditional logic, and custom ASCII-style stat visualization. RPG Character Generator allows users to create character profiles while enforcing strict point allocation and naming rules.

---

## Key Features

- **Strict Input Validation :**
  - Ensures character names are non-empty strings, under 10 characters, and without spaces.
  - Catches invalid data types for stats using isinstance() checks.
  - Enforces stat boundaries (each stat must be between 1 and 4).
- **Point Budget System :** Enforces strict point-budget distribution (starting total must equal exactly 7 points).
- **Visual Stat Bar Rendering :** Formats output using custom progress dots (● and ○) scaled over a 10-point visual meter.
- **Guard Clause Pattern :** Clean, early-return architecture for clear error reporting and readable control flow.

---

## Concepts & Technologies Applied

- **Python 3**
- **Type & Value Checking :** Validation with isinstance(), string method .count(), and comparison operators.
- **String Manipulation & Formatting :** Dynamic ASCII generation using string multiplication and f-strings.
- **Guard Clauses & Defensive Programming :** Handling invalid states early to keep core logic clean.

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
