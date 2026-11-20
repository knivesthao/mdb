---
name: ailv-ui-widgets
description: "Ten widgets cover most interface work in any framework — each pins the shape agents get wrong."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Common widgets: library first, pinned shape

`ailv-ui-widgets` (Common widgets: library first, pinned shape): Never hand-build these ten — pick your ecosystem's stocked library (names per framework live in ailv-ui-platform-picks), build the pinned shape, and read only the named leaves. Data table → ailv-code-perf, ailv-code-reuse: page on the server where one exists, otherwise paginate client-side; render only the visible window. Multi-step wizard → ailv-ui-forms, ailv-ui-behavior: one state object at the wizard root, validate each step on exit. Combo and autocomplete → ailv-ui-forms, ailv-ui-behavior: debounce typing, abort the stale fetch. Calendar and date picker → ailv-ui-behavior, ailv-code-reuse: derive highlights from two boundary dates, never per-cell state. Modal, dialog, drawer → ailv-ui-behavior, ailv-code-reuse: trap focus inside, return it on close, unmount when shut. Chat and feed → ailv-code-perf, ailv-code-reuse: append-only updates, pin scroll to the newest message, unsubscribe on unmount. Kanban drag-drop → ailv-code-reuse, ailv-ui-behavior: columns hold card-id arrays, reorder by index splice, never mutate in place. Rich text editor → ailv-code-reuse: leave the editor uncontrolled, sync content on change only, never mirror keystrokes in component state. Media player → ailv-ui-behavior, ailv-code-reuse: drive sliders through a direct element handle, never rerender per frame. Accordion and tree sidebar → ailv-ui-behavior, ailv-ui-nav: one expanded id in state, never a boolean per item. Humans get the library's accessible piece with real labels and visible states; agents keep small typed pieces, colocated state, and stable keys around it. Each widget gets its phone shape: tables scroll inside a stocked region (never the page), dialogs become bottom sheets, menus open on tap — verify every pinned shape at 360px. Skip everything else.

## Checks

- library picked before hand-building
- widget built in the pinned shape
- only named leaves read per widget
- controls labeled with visible states
- phone shape verified at 360px per widget
