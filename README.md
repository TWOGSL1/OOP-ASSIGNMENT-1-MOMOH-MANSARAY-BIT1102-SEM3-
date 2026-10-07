# Open-Field Crop Yield Monitor

A small Python command-line project for recording crop yield by field plot. It demonstrates core OOP concepts for PROG211 Object-Oriented Programming 1. All records use fictional, non-personal plot IDs; the program keeps data in memory for one run and does not save personal information.

## Requirements

- Python 3.8 or later
- No third-party packages

## Run

```bash
python crop_yield_monitor.py
```

Choose `1` to add a plot, `2` to list records, `3` to update a plot's yield, and `4` to exit. Area is in hectares and yield is in tonnes. Yield per hectare is calculated automatically.

## Example session

```text
OPEN-FIELD CROP YIELD MONITOR
1. Add plot  2. Display plots  3. Update yield  4. Exit
Choose 1-4: 1
Non-personal plot ID (for example F-001): F-001
Crop name: Rice
Area in hectares: 2
Yield in tonnes (0 if not measured): 5
Plot record added.
Choose 1-4: 2
PLOT | CROP | AREA | TOTAL YIELD | YIELD PER HECTARE
F-001 | Rice | 2.00 ha | 5.00 tonnes | 2.50 tonnes/ha
```

## OOP and assignment criteria

- `CropPlot` and `FarmRegistry` are two domain classes with attributes and methods.
- Objects are created and the registry coordinates interaction between them.
- `FarmRegistry.plots` is the single data structure used to hold multiple records: a dictionary keyed by unique plot ID.
- Instance methods: `update_yield`, `yield_per_hectare`, `display_info`, and registry operations.
- Class method: `CropPlot.from_default_crop` creates an object using the shared crop default.
- Static method: `CropPlot.validate_measurements` checks measurements without needing an object.
- Input checks reject non-numeric, negative, zero-area, and duplicate-ID entries.

## Digital Public Goods alignment

- **Open source:** source is plain Python and intended for a public GitHub repository. Add a suitable open-source license (for example, MIT) before publishing.
- **Inclusive and accessible:** menu options are numbered, prompts use plain language, and the project requires no graphical interface or paid software.
- **Privacy-respecting:** it requests a field code, crop and aggregate measurements only; do not enter names, phone numbers, precise farmer location, or other personal data. Data is not persisted.
- **Modular and reusable:** model classes separate field logic from the menu; measurement validation and yield calculation can be reused.

## Repository submission checklist

1. Include this README and `crop_yield_monitor.py` in your GitHub repository.
2. Add your lecturer as a repository collaborator using the address/instructions given in class.
3. Capture genuine screenshots of the program running, including adding a plot, listing it, and updating yield. Insert them into the hardcopy report.
4. Replace the student-information placeholders in the report before printing. Follow the brief's stated font, size, line spacing and alignment.

## Scope

This is a teaching prototype, not an agronomic advisory tool. Yield values are entered by a user and are not verified against field sensors or official records. Records disappear when the program exits.
