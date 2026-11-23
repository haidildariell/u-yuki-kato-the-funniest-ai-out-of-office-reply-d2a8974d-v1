"""Write the out-of-office auto-reply to /output/entry.txt."""

import os

REPLY = (
    "Out on vacation. I left a junior AI in charge \u2014 "
    "it read your email, panicked, and has now filed for annual leave as well."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def build_reply():
    """Return the single-line auto-reply, checked against the gate limits."""
    reply = REPLY.strip()
    if not reply or len(reply) > 160 or "\n" in reply:
        raise ValueError("reply must be one non-empty line of 1-160 characters")
    return reply


def main():
    text = build_reply()
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
