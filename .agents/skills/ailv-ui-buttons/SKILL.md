---
name: ailv-ui-buttons
description: "Dialogs read in order, so the primary action goes last — anywhere else invites the misclick."
sources:
  - title: Apple Human Interface Guidelines
    url: https://developer.apple.com/design/human-interface-guidelines
helper: scripts/helper.py
example: examples/output.md
---

# Place dialog buttons

`ailv-ui-buttons` (Place dialog buttons): Dialogs and modals put the primary action last in reading order — farthest right in left-to-right locales, mirrored for right-to-left — with the dismissive action (Cancel, Close) immediately before it. Page-level forms are the exception: left-align the button row with the form itself. Never style a secondary action to rival the primary, and never park a destructive action beside the primary — separate it by space or into another region. Label every button with the action alone — a short verb first (Copy, Save, Send), never a sentence; the surrounding text carries the instruction, the button carries the verb. Build for thumbs: targets at least 44px, primary actions go full-width on narrow screens, and destructive actions stay clear of thumbs that slip.

## Checks

- primary last in reading order in dialogs
- dismissive immediately before primary
- destructive separated from primary
- labels are verbs, not sentences
- targets at least 44px, full-width primary on narrow screens
