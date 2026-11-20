checker runs first          -> mypy / pyright / tsc before pytest, not after
zero errors                 -> fix or waive with a logged reason, never silence
no new untyped boundaries   -> public signatures typed, nullables explicit

gates: 3, all enforced, none skipped
