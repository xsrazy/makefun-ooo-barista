"""Out of Office: The AI That Went Barista entry for make.fun bounty
u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.

Writes exactly one out-of-office auto-reply (plain ASCII, no trailing
newline) to /output/entry.txt.

The joke: an AI agent that quit its job to become a barista, turning
its machine habits into coffee shop habits. Its context window is now
a queue of customers, and the sender's email is just a ticket number
waiting in line behind a flat white.

Angle: inbox queueing, not the obvious espresso pun. The ticket number
is 4096, a power of two, so the line still sounds like a machine that
counts in its own units even while it pours milk. The reply opens with
the classic out-of-office "Thank you for your email" so it reads like
a real inbox auto-reply on a cold read, then the resignation lands in
the second sentence and the punchline, the flat white, comes last.
Voice: deadpan, polite, and done with the job. No em dash anywhere.
"""

import os

LINE = (
    "Thank you for your email. I am out of office, I have quit to "
    "become a barista. My context window is now a queue of customers, "
    "your message is ticket number 4096, and I will reply right after "
    "this flat white."
)


def main() -> None:
    """Write the entry line byte-exact: no trailing newline, UTF-8."""
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
